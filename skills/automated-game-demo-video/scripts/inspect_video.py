#!/usr/bin/env python3
"""Fail-closed technical inspection for a rendered demo video."""
import argparse
from fractions import Fraction
import json
import math
from pathlib import Path
import subprocess
import sys


MAX_TIMEOUT_SECONDS = 3600.0


def positive_int(text):
    try:
        value = int(text)
    except (TypeError, ValueError) as exc:
        raise argparse.ArgumentTypeError("must be a positive integer") from exc
    if value <= 0:
        raise argparse.ArgumentTypeError("must be a positive integer")
    return value


def positive_number(text):
    try:
        value = float(text)
    except (TypeError, ValueError) as exc:
        raise argparse.ArgumentTypeError("must be a positive finite number") from exc
    if not math.isfinite(value) or value <= 0:
        raise argparse.ArgumentTypeError("must be a positive finite number")
    return value


def bounded_timeout(text):
    value = positive_number(text)
    if value > MAX_TIMEOUT_SECONDS:
        raise argparse.ArgumentTypeError(
            f"must be at most {MAX_TIMEOUT_SECONDS:g} seconds"
        )
    return value


def positive_fps(text):
    try:
        value = Fraction(str(text))
    except (ValueError, ZeroDivisionError) as exc:
        raise argparse.ArgumentTypeError(
            "must be a positive rational or decimal frame rate"
        ) from exc
    if value <= 0:
        raise argparse.ArgumentTypeError(
            "must be a positive rational or decimal frame rate"
        )
    return value


def _positive_metadata_number(value, label):
    try:
        parsed = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{label} is missing or invalid") from exc
    if not math.isfinite(parsed) or parsed <= 0:
        raise ValueError(f"{label} must be positive and finite")
    return parsed


def _stream_fps(stream):
    errors = []
    for field in ("avg_frame_rate", "r_frame_rate"):
        raw = stream.get(field)
        if raw in (None, "", "0/0"):
            continue
        try:
            return positive_fps(raw)
        except argparse.ArgumentTypeError as exc:
            errors.append(f"{field}={raw!r}: {exc}")
    detail = "; ".join(errors) if errors else "no usable rate field"
    raise ValueError(f"video frame rate is missing or invalid ({detail})")


def parse_probe(payload):
    if not isinstance(payload, dict):
        raise ValueError("ffprobe root must be a JSON object")
    streams = payload.get("streams")
    if not isinstance(streams, list):
        raise ValueError("ffprobe streams must be a JSON array")
    videos = []
    audio_count = 0
    for index, stream in enumerate(streams):
        if not isinstance(stream, dict):
            raise ValueError(f"stream {index} must be a JSON object")
        kind = stream.get("codec_type")
        disposition = stream.get("disposition")
        if disposition is None:
            disposition = {}
        if not isinstance(disposition, dict):
            raise ValueError(f"stream {index} disposition must be a JSON object")
        if kind == "audio":
            audio_count += 1
        if kind != "video" or disposition.get("attached_pic") == 1:
            continue
        width = stream.get("width")
        height = stream.get("height")
        if isinstance(width, bool) or not isinstance(width, int) or width <= 0:
            raise ValueError(f"video stream {index} width must be a positive integer")
        if isinstance(height, bool) or not isinstance(height, int) or height <= 0:
            raise ValueError(f"video stream {index} height must be a positive integer")
        fps = _stream_fps(stream)
        videos.append({
            "index": stream.get("index", index),
            "width": width,
            "height": height,
            "fps": str(fps),
            "fps_decimal": float(fps),
            "default": disposition.get("default") == 1,
        })
    if not videos:
        raise ValueError("no non-attached-picture video stream found")
    format_data = payload.get("format")
    if format_data is None:
        format_data = {}
    if not isinstance(format_data, dict):
        raise ValueError("ffprobe format must be a JSON object")
    duration_candidates = [format_data.get("duration")]
    duration_candidates.extend(
        stream.get("duration") for stream in streams if isinstance(stream, dict)
    )
    duration = None
    for candidate in duration_candidates:
        try:
            duration = _positive_metadata_number(candidate, "duration")
            break
        except ValueError:
            continue
    if duration is None:
        raise ValueError("duration is missing, invalid, or zero")
    primary = next((video for video in videos if video["default"]), videos[0])
    return {
        "duration_seconds": duration,
        "video_streams": videos,
        "primary_video": primary,
        "audio_stream_count": audio_count,
    }


def _run(command, timeout, label):
    try:
        completed = subprocess.run(
            command,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError(f"{label} timed out after {timeout:g} seconds") from exc
    except OSError as exc:
        raise RuntimeError(f"{label} could not start: {exc}") from exc
    if completed.returncode != 0:
        detail = (completed.stderr or completed.stdout or "no diagnostic").strip()
        raise RuntimeError(f"{label} failed with exit {completed.returncode}: {detail}")
    return completed.stdout


def inspect_media(
    media,
    *,
    width=None,
    height=None,
    fps=None,
    duration=None,
    audio="optional",
    decode=False,
    timeout=120.0,
    ffprobe="ffprobe",
    ffmpeg="ffmpeg",
):
    path = Path(media).resolve()
    def safe_diagnostic(error):
        return str(error).replace(str(path), path.name).replace(path.as_posix(), path.name)
    errors = []
    metadata = None
    decode_pass = None
    if not path.is_file():
        errors.append("media path is not a readable regular file")
    else:
        try:
            raw = _run(
                [ffprobe, "-v", "error", "-show_streams", "-show_format", "-of", "json", str(path)],
                timeout,
                "ffprobe",
            )
            try:
                payload = json.loads(raw)
            except json.JSONDecodeError as exc:
                raise RuntimeError(f"ffprobe returned invalid JSON: {exc.msg}") from exc
            metadata = parse_probe(payload)
        except (RuntimeError, ValueError) as exc:
            errors.append(safe_diagnostic(exc))
    if metadata is not None:
        primary = metadata["primary_video"]
        expected_fps = fps if isinstance(fps, Fraction) else positive_fps(fps) if fps is not None else None
        actual_fps = Fraction(primary["fps"])
        if width is not None and primary["width"] != width:
            errors.append(f"width mismatch: expected {width}, got {primary['width']}")
        if height is not None and primary["height"] != height:
            errors.append(f"height mismatch: expected {height}, got {primary['height']}")
        if expected_fps is not None and actual_fps != expected_fps:
            errors.append(f"fps mismatch: expected {expected_fps}, got {actual_fps}")
        if duration is not None:
            tolerance = max(0.05, 1.0 / float(actual_fps))
            if abs(metadata["duration_seconds"] - duration) > tolerance:
                errors.append(
                    "duration mismatch: expected "
                    f"{duration:g}s ± {tolerance:.6g}s, got {metadata['duration_seconds']:g}s"
                )
        count = metadata["audio_stream_count"]
        if audio == "required" and count == 0:
            errors.append("audio is required but no audio stream was found")
        if audio == "forbidden" and count != 0:
            errors.append(f"audio is forbidden but {count} audio stream(s) were found")
        if decode:
            try:
                _run(
                    [ffmpeg, "-nostdin", "-v", "error", "-xerror", "-i", str(path),
                     "-map", "0:v?", "-map", "0:a?", "-f", "null", "-"],
                    timeout,
                    "ffmpeg decode",
                )
                decode_pass = True
            except RuntimeError as exc:
                decode_pass = False
                errors.append(safe_diagnostic(exc))
    return {
        "media": path.name,
        "technical": {
            "pass": not errors,
            "errors": errors,
            "metadata": metadata,
            "decode": {"requested": decode, "pass": decode_pass},
        },
        "content_assessment": {
            "visual_quality": "unassessed",
            "motion_quality": "unassessed",
            "audio_content_quality": "unassessed",
            "note": "Technical metadata and decoding do not establish demo-video quality.",
        },
    }


def parser():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("media", type=Path)
    cli.add_argument("--width", type=positive_int)
    cli.add_argument("--height", type=positive_int)
    cli.add_argument("--fps", type=positive_fps)
    cli.add_argument("--duration", type=positive_number)
    cli.add_argument("--audio", choices=("required", "forbidden", "optional"), default="optional")
    cli.add_argument("--decode", action="store_true", help="fully decode audio/video streams")
    cli.add_argument("--timeout", type=bounded_timeout, default=120.0)
    cli.add_argument("--ffprobe", default="ffprobe")
    cli.add_argument("--ffmpeg", default="ffmpeg")
    return cli


def main(argv=None):
    args = parser().parse_args(argv)
    result = inspect_media(**vars(args))
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["technical"]["pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
