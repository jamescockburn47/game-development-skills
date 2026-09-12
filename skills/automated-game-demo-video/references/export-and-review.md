# Export, inspect and repeat

Keep a unique run directory containing the shot plan, explicit takes, edit list,
technical results, representative frames and final master. Preserve originals; use
new output names. Store enough build/configuration information to repeat the shoot
without including credentials or unrelated private data. Retain only useful evidence;
avoid dumping every frame by default when storage cost has no benefit.

## Assemble and deliver

Choose frame rates, dimensions and codec from the requested destination and the
actual game. Confirm current destination requirements when relevant. A browser or
native game can produce different delivery formats; changing the extension does not
convert a container or codec. Use installed tools and verify support locally.

For a common shareable SDR master, MP4 with H.264/yuv420p and AAC when sound is
included is a practical starting point. Use WebM, MOV, an image sequence, a looping
GIF or another format when the brief calls for it and tools support it. GIF cannot
carry sound. Transparency and HDR require an appropriate codec, player and verified
colour handling; do not silently flatten them. Pixel art needs appropriate scaling.

An edit list identifies shot/take, in/out, caption, audio and any transition. Sum
trimmed lengths and subtract transition overlap to compute final duration. For a
fixed-step job, derive frame counts from the chosen rational frame rate. Avoid adding
another rate conversion merely to make metadata read correctly. Keep cuts simple
unless transitions help the story. Provide a poster chosen from the delivered film.

Capture game audio explicitly. An audio stream can contain silence; verify audible
content and alignment with visible events. Avoid clipping, abrupt cutoffs and music
that masks important feedback. Do not add a microphone by default. Rights and user
authorization apply to music, voices and third-party footage; no external assets are
needed simply to make a demo. Report deliberate silence and any inaccessible audio.

Use FFmpeg subprocess arguments as a list where scripting, bounded execution and
explicit output paths. Wait for successful encoder exit after closing its input;
preserve stderr for diagnosis without leaking private context. Clean up owned jobs
on failure. Write a new output and verify it before replacing an approved master.

## Technical checks

If Python and FFprobe/FFmpeg are installed, from this skill's folder run:

```text
python scripts/inspect_video.py path/to/master.mp4 --width 1920 --height 1080 --fps 30 --duration 60 --audio required --decode
```

Choose expectations from the actual brief. Use `--audio forbidden` for an intentionally
silent film; `optional` checks neither requirement. Run `--help` for tool path and
timeout overrides. The helper reads the media and emits JSON; it does not edit it or
install tools. Missing tools, malformed metadata and failed requested checks fail.
It reports frame-rate metadata (average where available), not observed frame pacing or a guarantee
of constant frame rate. Its duration tolerance allows normal container rounding.
Reports identify the input by filename; keep the exact take mapping in the run plan.

Check the exact master and its selected takes, not whichever file is newest nearby.
For exact frame-budget jobs, also count decoded frames with FFprobe and compare the
timeline. A full FFmpeg decode catches corruption metadata alone cannot. Expected
dimensions, duration, codec, pixel format, audio layout and file size should match
delivery requirements. The helper covers some of these; inspect other probe fields
or player behaviour where the brief requires them.

## Visual and audio review is separate

Watch the final encoded film at delivery size and in motion. Inspect every cut and
the beginnings, action peaks and endings of takes. Listen to included sound. Record
short verdicts tied to timestamps for:

- **Clarity:** the main action and its result are visible, and captions match them.
- **Composition:** the subject stays in frame without clipping/occlusion; UI and
  text are readable; overlays do not conceal controls or important targets.
- **Motion:** cadence, camera movement, gait and contacts look right; no accidental
  time acceleration, frozen world, doubled updates or repeated frames.
- **Continuity:** loading, teleports, old weather/particles and menus do not leak
  across cuts; montage is not presented as one earned progression.
- **Sound:** intended content is audible, synchronized and balanced, with clean cuts.
- **Faithfulness:** the footage shows this build; staging and offline quality cannot
  be mistaken for unscripted outcomes or measured real-time performance.

Black/freeze detection and frame comparisons can flag review points. They cannot
decide quality: a quiet board game legitimately holds frames, and a smooth 30 fps
file can repeat a stalled frame. Screenshots cannot prove animation or audio quality.
If playback/listening is unavailable, retain exact inspection limits and deliver a
playable file for the missing review rather than claiming it passed.

Keep a short repeat command and which shots depend on changed features. Future
captures should rerun a small trial before reusing a plan against a changed build.
Do not run expensive jobs indefinitely: bound duration, resolution, storage and
concurrency. Use suitable available hardware without disturbing other workloads.

Tool references: [FFmpeg](https://ffmpeg.org/ffmpeg.html) and
[FFprobe](https://ffmpeg.org/ffprobe.html), checked 12 September 2026. Test actual
installed encoders and players; these references do not establish host capability.
