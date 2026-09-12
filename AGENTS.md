# Game development skills

Maintain three independent, portable skills. Keep the user's description in their own
words, and keep the HTML review before any new game implementation. Do not apply that
game-building checkpoint recursively when editing these skills or their review kit.
The demo-video skill records existing games without restarting game-design intake.
It owns its capture guidance and optional media inspector; do not mirror the HTML
review kit into it. Separate technical media checks from visual, motion and audio review.

The general skill owns shared review resources. After changing those resources run
`python package_skills.py --sync-shared`; the open-world copies are checked mirrors.
Run `python verify_public.py` before a commit or publication. CI runs the same command.
Generated ZIPs and the blank example must match their sources. Regenerate the example
with `python verify_public.py --refresh-example` after an intentional template change.

Use Python 3.13.7 for release verification. Keep maintained source below 300 nonblank
lines; the generated standalone example and its history are documented exceptions.
There are no third-party Python dependencies or automatic external requests in the kit.
The optional video inspector needs installed FFprobe/FFmpeg; public tests use synthetic
metadata and mocks, so CI does not certify live engine recording or video appearance.

The public repository includes only portable source, blank examples, synthetic tests
and distribution files. Private research, user transcripts, project-specific examples,
local evaluation records and workstation configuration stay outside the public payload.
The verifier rejects unexpected tracked paths. Review the exact Git tree before pushing.
Do not commit or publish without user authorization. For a bad public release, stop
distribution and correct it in a new commit; changing visibility cannot recall copies.
