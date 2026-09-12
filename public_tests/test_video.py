"""Public tests for the portable demo-video inspector."""
import argparse
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "automated-game-demo-video" / "scripts" / "inspect_video.py"
SPEC = importlib.util.spec_from_file_location("public_video_inspector", SCRIPT)
video = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(video)


def probe_payload(*, width=1920, height=1080, fps="60/1", duration="10", audio=True):
    streams = [{
        "index": 0,
        "codec_type": "video",
        "width": width,
        "height": height,
        "avg_frame_rate": fps,
        "r_frame_rate": fps,
        "disposition": {"default": 1, "attached_pic": 0},
    }]
    if audio:
        streams.append({"index": 1, "codec_type": "audio", "duration": duration})
    return {"streams": streams, "format": {"duration": duration}}


def completed(payload, returncode=0, stderr=""):
    return subprocess.CompletedProcess([], returncode, json.dumps(payload), stderr)


class ParseTests(unittest.TestCase):
    def test_attached_picture_is_not_a_video_program(self):
        payload = probe_payload()
        payload["streams"][0]["disposition"]["attached_pic"] = 1
        with self.assertRaisesRegex(ValueError, "non-attached-picture"):
            video.parse_probe(payload)

    def test_zero_invalid_and_missing_metadata_fail_closed(self):
        variants = [
            probe_payload(width=0),
            probe_payload(height=-1),
            probe_payload(fps="0/0"),
            probe_payload(duration="nan"),
            {"streams": "not-an-array", "format": {"duration": "1"}},
            {"streams": [dict(probe_payload()["streams"][0], disposition="bad")],
             "format": {"duration": "1"}},
            {"streams": probe_payload()["streams"], "format": "bad"},
        ]
        for payload in variants:
            with self.subTest(payload=payload), self.assertRaises(ValueError):
                video.parse_probe(payload)

    def test_fps_accepts_rational_and_decimal_but_rejects_nonpositive(self):
        self.assertEqual(str(video.positive_fps("30000/1001")), "30000/1001")
        self.assertEqual(str(video.positive_fps("29.97")), "2997/100")
        for raw in ("0", "0/0", "-24", "nan"):
            with self.subTest(raw=raw), self.assertRaises(argparse.ArgumentTypeError):
                video.positive_fps(raw)


class InspectorTests(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.media = Path(self.folder.name) / "demo.webm"
        self.media.write_bytes(b"synthetic-test-placeholder")

    def tearDown(self):
        self.folder.cleanup()

    def test_valid_video_passes_without_disclosing_its_parent_directory(self):
        responses = [completed(probe_payload()), subprocess.CompletedProcess([], 0, "", "")]
        with mock.patch.object(video.subprocess, "run", side_effect=responses) as run:
            result = video.inspect_media(self.media, width=1920, height=1080,
                                         fps="60", duration=10, audio="required", decode=True)
        self.assertTrue(result["technical"]["pass"])
        self.assertTrue(result["technical"]["decode"]["pass"])
        self.assertEqual(result["media"], self.media.name)
        self.assertNotIn(str(self.media.parent), str(result))
        self.assertEqual(run.call_args_list[0].args[0][-1], str(self.media.resolve()))
        self.assertEqual(result["content_assessment"]["motion_quality"], "unassessed")

    def test_tool_error_redacts_the_input_directory(self):
        response = subprocess.CompletedProcess([], 1, "", f"Cannot read {self.media.resolve()}")
        with mock.patch.object(video.subprocess, "run", return_value=response):
            result = video.inspect_media(self.media)
        self.assertFalse(result["technical"]["pass"])
        self.assertIn(self.media.name, result["technical"]["errors"][0])
        self.assertNotIn(str(self.media.parent), str(result))

    def test_requested_metadata_mismatch_is_a_failure(self):
        with mock.patch.object(video.subprocess, "run", return_value=completed(probe_payload())):
            result = video.inspect_media(
                self.media, width=1280, height=720, fps=video.positive_fps("30"), duration=8
            )
        self.assertFalse(result["technical"]["pass"])
        self.assertEqual(len(result["technical"]["errors"]), 4)
        self.assertEqual(result["content_assessment"]["visual_quality"], "unassessed")

    def test_required_audio_missing_is_a_failure(self):
        with mock.patch.object(
            video.subprocess, "run", return_value=completed(probe_payload(audio=False))
        ):
            result = video.inspect_media(self.media, audio="required")
        self.assertFalse(result["technical"]["pass"])
        self.assertIn("audio is required", result["technical"]["errors"][0])

    def test_full_decoder_failure_is_reported_and_uses_no_output_file(self):
        responses = [
            completed(probe_payload()),
            subprocess.CompletedProcess([], 1, "", "corrupt frame"),
        ]
        with mock.patch.object(video.subprocess, "run", side_effect=responses) as run:
            result = video.inspect_media(self.media, decode=True)
        self.assertFalse(result["technical"]["pass"])
        self.assertFalse(result["technical"]["decode"]["pass"])
        decode_command = run.call_args_list[1].args[0]
        self.assertIn("-xerror", decode_command)
        self.assertEqual(decode_command[-3:], ["-f", "null", "-"])

    def test_probe_timeout_fails_closed_without_attempting_decode(self):
        with mock.patch.object(
            video.subprocess,
            "run",
            side_effect=subprocess.TimeoutExpired(["ffprobe"], 2),
        ) as run:
            result = video.inspect_media(self.media, decode=True, timeout=2)
        self.assertFalse(result["technical"]["pass"])
        self.assertIn("timed out", result["technical"]["errors"][0])
        self.assertIsNone(result["technical"]["decode"]["pass"])
        run.assert_called_once()


if __name__ == "__main__":
    unittest.main(verbosity=2)
