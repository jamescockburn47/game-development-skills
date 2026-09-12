# Control and capture routes

These are routes to investigate, not a claim every host has them. Check the project
version, installed tools and local help before using version-sensitive APIs. Prefer
the narrow existing tool that can control and record this game. Preserve host access
rules. Do not evade restricted computer control with a different backend.

## Separate three small responsibilities

Use existing equivalents of: stage a reproducible starting state; drive gameplay and
camera; record and finalize output. A short engine-specific script is often enough.
Readiness should observe the loaded scene/player/camera and required assets. A fixed
sleep alone cannot prove loading is finished. Bound waits and record failures.

Operate actual gameplay inputs or domain actions, including their normal cooldowns,
collision, transactions and consequences. Teleporting between shots is staging;
overriding player positions during a locomotion shot can fabricate movement. Record
camera overrides, AI pauses, resource grants and simulated network partners. Avoid
recording against live accounts, public matches or cloud saves without authority.

## Browser games

Use an available browser automation tool and observed UI or a documented project
handle. A clean browser context can isolate local storage, cookies and saves, but
does not by itself isolate server-side changes. Fix the build, viewport, device scale,
renderer buffer and camera aspect; CSS dimensions alone do not establish resolution.

Choose capture bounds deliberately:

- Canvas capture records the canvas; DOM menus, captions and overlays require a
  page/window capture or deliberate composition. A canvas stream is video only;
  route permitted game audio explicitly if required.
- Real-time MediaRecorder should select a supported MIME/codec and await final data
  after stopping. Listen for errors, stop tracks, and await the specific download or
  file finalization with a timeout. Never turn recorder failure into silent preview.
- Offline frame extraction can capture the composited page, with numbered images
  or a pipe to an encoder. Respect backpressure; advance the simulation before each
  intended output frame and wait for that frame to render. Record audio on the same
  timeline or choose a real-time method when that cannot be achieved.

User gestures may be needed for pointer lock, focus or audio. Detect and perform them
through permitted interaction. Avoid hard-coded hot-reload/network blocking that also
breaks real gameplay; use a stable preview build and isolated services where appropriate.

## Engines and native builds

| Environment | Candidate route and boundary |
|---|---|
| Unity | Existing gameplay/replay automation plus Recorder or Timeline. Recorder captures Editor Play mode, not a standalone Player. Packaged-game demonstrations need a suitable build/window recorder or another verified integration. |
| Unreal | Existing game automation plus Sequencer/Movie Render Queue for cinematic jobs. Runtime rendering needs supported project/plugin setup. A rendered sequence alone does not prove playable behaviour or packaged performance. |
| Godot | Existing scripts/input plus Movie Maker for offline video/audio. Check writer support in the installed build; output may need transcoding. Quit gracefully so the container/audio finalize. |
| Other native / custom engines | Prefer existing replay, debug camera, screenshot/image-sequence or capture integrations. Otherwise use permitted app input with an installed recorder. Verify actual capture area and audio, not just a successful launch. |
| Mobile / console / remote device | Use an authorized emulator/device route, platform recorder or capture hardware already available. Match the target input and orientation. If control/capture is inaccessible, deliver the prepared sequence and exact missing prerequisite. |

For a GUI-only game, controlled input plus screen recording can still work. Inspect
current UI state before acting, maintain focus and checkpoints, and tolerate loading
variability with observed conditions. Do not invent an engine API from its name.

## Timing: one simulation, one recorded timeline

For real-time capture, allow the normal game loop to run. Check the result for stalls,
missed inputs and dropped or repeated frames; requested output fps is just a setting.
For offline capture, use the engine's own fixed-step movie/replay support where possible.
If introducing a small stepping hook, suspend the normal loop and advance physics,
animation, camera, effects, UI and relevant timers coherently. For example, a 60 Hz
simulation feeding 30 fps video normally needs two simulation substeps per output
frame, with audio advanced to match. Compare motion to normal play before a long shoot.

Freezing `Date.now()` does not freeze animation driven by the rAF timestamp,
`performance.now()`, a shader clock, physics or network time. Conversely, calling the
normal frame loop and a second animation tick can advance gait twice. A capture
harness must not manufacture visual defects absent in ordinary play. Use a small
parity trial and an action whose travel/time/contact can discriminate these failures.

Snapshot and restore temporal visual state as well as player state. On every exit,
release input and restore camera, weather, time, quality, adaptive scaling, UI, audio,
autosave and update loops that you changed. Discard an isolated session when that
provides a simpler complete reset. Finalization failure must not prevent cleanup.

## Primary references

Checked 12 September 2026; verify against the actual installed version:

- [MDN canvas captureStream](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/captureStream)
- [MDN MediaRecorder final data and timing](https://developer.mozilla.org/en-US/docs/Web/API/MediaRecorder/dataavailable_event)
- [Unity Recorder 5.1 manual](https://docs.unity3d.com/Packages/com.unity.recorder@5.1/manual/index.html)
- [Unreal Movie Render Queue at runtime](https://dev.epicgames.com/documentation/unreal-engine/movie-render-queue-in-runtime-in-unreal-engine?lang=en-US)
- [Godot Movie Maker](https://docs.godotengine.org/en/stable/tutorials/animation/creating_movies.html)
