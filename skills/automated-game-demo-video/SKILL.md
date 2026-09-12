---
name: automated-game-demo-video
description: Direct and produce demo videos, gameplay trailers, walkthroughs and showreels from an existing game. Use when the user wants the assistant to explore a game, select shots, operate gameplay or cameras, record takes, edit footage and verify an exported video. Adapt to browser, native, mobile, 2D, 3D and engine capture tools actually available; includes repeatable recording and technical video checks.
---

# Automated game demo video

Act as director, player, camera operator and editor. Deliver footage of the actual
game, chosen to explain its appeal, with a repeatable way to record it again.
The creator should not have to prescribe camera coordinates, every button press,
the shot list or the verification steps.

## Introduce and scope the film

On activation, briefly explain the premise in ordinary language: you will explore
the game, choose a sequence that shows what players do, take control using the
tools available, rehearse and record, edit the film, and check the exported result.
Explain that scouting and a short trial can avoid wasted captures and repeated
work; token, time and rendering savings depend on the project and are not guaranteed.
Then act on the request. A minimal invocation must start this workflow unaided.

Read the existing brief, project instructions and available build. Preserve the
creator's game description and established claims. You may write shot directions
and factual captions from observed features; do not invent their game concept,
features, release status or marketing promises. This skill works alone. Recording
an existing game does not trigger a new-game questionnaire or design approval.

Reuse supplied audience, destination, length, orientation, sound and must-show
preferences. Ask only for missing information that changes the film materially.
Otherwise state practical defaults and proceed: for an unspecified short desktop
demo, start around 45–60 seconds, landscape, 1080p at 30 fps, with game sound if
available. Adapt these to a portrait mobile game, pixel art, text-heavy game,
accessibility needs or a request for an uncut demonstration. Do not silently drop
requested sound or substitute a different deliverable.

Distinguish a request for a plan from a request to make the video. For the latter,
continue through capture and export when tools permit; a storyboard or script alone
is unfinished. Creating local recording artifacts is in scope. Uploading, publishing,
paid assets, production changes or involving other players requires relevant authority.

## 1. Discover the game and a workable control route

Inspect the actual engine/build, startup commands, capture/replay tools, test hooks,
save boundaries, supported inputs, cameras, sound and available runtime surfaces.
Run or inspect the game and try the core action before choosing its best shots.
Use a fresh guest/profile, disposable save copy or isolated capture build so that
recording cannot replace the creator's progress or modify a live economy.

Read [control and capture](references/control-and-capture.md) only for the relevant
engine and route. Prefer an existing replay, cinematic tool, gameplay API or test
controller; use permitted browser/device/computer interaction where appropriate.
Use the real gameplay implementation for featured actions and observe their result.
Small, isolated capture hooks are useful when existing controls cannot do the job.
Do not build a general automation framework or rewrite the game to make a trailer.

Discover capabilities rather than assuming this host can control every device or
engine. A skill grants no tools or permissions. If a necessary capability is missing,
state the exact gap and prepare the closest useful local artifact or recording route.
Do not describe a plan, still images or a preview as a completed video. Never bypass
a platform restriction by switching to an unapproved control backend.

Record which mode each shot uses: normal play, staged setup with real mechanics,
cinematic animation/FX, or offline rendering. A scripted enemy, granted inventory,
camera teleport or high-quality offline render changes what the footage can prove.
Keep those facts with the footage; make material staging clear in delivery notes and
in the film when the audience could otherwise infer a false gameplay claim.

## 2. Scout and direct

Read [shot direction](references/shot-direction.md). Choose a small number of
distinct things the game actually lets a player experience. Show the strongest
moment early, orient the viewer, show input → action → consequence, then end with
a satisfying outcome or accurate invitation. Include the player's usable view.
Scale the number and length of shots to the request; do not fill time with repeated
orbits or rapid cuts that hide the mechanic.

Inspect candidate views at the start, action peak and end. Check subject visibility,
camera clipping, readable interface and room for captions at the delivery aspect
ratio. Select shots yourself from this evidence. Retain a short shot plan using
[the reusable template](assets/shot-plan-template.md), or the project's existing
equivalent. Explain the chosen sequence concisely and continue unless the user
requested approval or a material creative decision remains unresolved.

## 3. Prove a short take before a full shoot

Capture and export roughly 3–5 seconds containing the hardest representative action,
camera movement, interface and required sound. Inspect this encoded clip, not just
the live window. Name pass/fail criteria: correct build and view, visible action and
result, usable cadence, intended resolution and sound, clean start/stop and safe state.
An attractive orbit with no demonstrated mechanic is an inadequate gameplay demo.

Compare capture behaviour with ordinary play. Confirm one simulation timebase,
correct frame extraction and explicit audio routing. Rehearse loading and streaming
off-camera. A requested 60 fps stream is not evidence of 60 fps gameplay; a fixed-step
render is not a performance benchmark. Use a separate real-time run for that claim.

Budget one trial and one evidence-led correction before reassessing a failed route.
If it still fails, change the capture approach or report the dependency; do not
multiply long captures around an unproved mechanism or reduce the promised outcome
without agreement.

## 4. Record reproducible takes

Use a new run directory, stable shot IDs and explicit take filenames. Record build
revision plus relevant uncommitted state, settings, seed/checkpoint, tool versions,
resolution, simulation rate, capture rate, input sequence and camera path. Keep
secrets and personal data out of recordings and manifests. Capture the intended
build; avoid hot reload changing it halfway through the shoot.

For each take: stage → wait for observable readiness → settle temporal effects →
start capture → operate the game → observe the result → stop and finalize → inspect.
Give readiness waits a timeout. Reset particles, weather, camera smoothing, exposure,
UI, held keys and other prior-shot state. Keep transition/teleport frames outside
the recorded shot. Save before/peak/after frames and brief event evidence where useful.

Use `try/finally` or the engine equivalent to release held inputs, stop tracks and
encoders, remove temporary overrides, and restore all changed session settings.
Snapshot before mutation; restore original values, not guessed defaults. Cleanup
must still run after recorder or download failure. Bound subprocesses and awaits;
close only owned processes. Never silently fall back from failed recording to preview.

Match completion to the exact take: recorder final chunk, engine finished job or
encoder successful exit, then inspect that file. Do not select the newest file in
a shared folder. Respect encoder backpressure and ensure offline output frames are
neither lost nor duplicated. Retake the failed shot rather than the whole film.

## 5. Edit and export

Read [export and review](references/export-and-review.md). Cut around understandable
actions; leave enough time to see their consequences. Keep titles brief and grounded
in the actual build. Balance real game sound where available; use licensed or
user-authorized music only. Mark deliberate silence. Reframe portrait/square variants
so their subjects and essential UI remain visible; do not blindly crop a landscape film.

Keep original takes and a simple ordered edit list. Calculate the final timeline,
including transition overlaps, and export the requested container, codec, aspect,
frame rate and sound configuration supported by available tools. Prefer existing
engine recorders and installed encoders to adding dependencies.

## 6. Check the film, then hand it over

Run technical checks on the final encoded master, including a full decode where
available. The bundled [video inspector](scripts/inspect_video.py) can check duration,
dimensions, reported frame rate, audio-stream presence and decode success using
installed FFprobe/FFmpeg. Its pass is strictly technical; it does not certify motion,
audible content, synchronization, truthful claims or visual quality.

Watch the final film in motion, particularly each cut and action. Inspect first/last
frames and representative action peaks; listen if sound is included. Judge clarity,
framing, pacing, motion, readable text, sound and faithful representation against
the brief. Retain concise verdicts and timestamps; investigate freezes, black frames,
missing reactions and abrupt audio. Static scenes can be intentional. If tools cannot
play/listen or a check is missing, state exactly what was and was not inspected.

Provide the playable/downloadable master, a useful poster or contact sheet, the
short shot/edit plan, repeat command and technical/visual verdicts. State material
staging, offline rendering and remaining gaps. Do not publish without authorization.
Preserve the useful capture hooks and instructions in the project so later builds
can repeat the shoot; rerun affected takes when features or cameras change. A video
demonstrates selected experiences and does not replace game testing or prove fun.
