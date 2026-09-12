# Game Development Skills

Three reusable skills that help an AI coding assistant plan a game, build and test it, and direct a video showing what it can do.

A skill is a folder of instructions and supporting files that an assistant can load for a task. It guides how the assistant asks questions, makes decisions, uses development tools and checks its work. It is not a game engine, a game template or a separate application.

## The skills

| Skill | Best used for |
|---|---|
| **Evidence-led game development** | Games of any genre, engine or platform. It covers discovery, planning, scope, implementation, playtesting, presentation and proportionate engineering. |
| **Open-world game development** | Games with exploration, travel and worlds that remember what happens, including how people and places behave beyond the player's view. |
| **Automated game demo video** | Existing games that need a demo, trailer, walkthrough or showreel. The assistant chooses shots, operates the game and cameras, records takes, edits the film and checks the export. |

Each works alone. Combine the first two for an open-world project needing the broader workflow; together they produce one introduction, questionnaire and plan. Use the video skill independently whenever an existing game is ready to show.

They are for solo creators, small teams and developers who want practical AI assistance with clear control over authorship, scope and evidence.

## Planning and building a game

The skill introduces the process and starts an adaptive questionnaire. Your prompt need not repeat the workflow. It asks a few questions at a time and reuses earlier answers.

You must write the description of your game. The skill preserves that description word for word. Asking the assistant to “choose for me” lets it recommend implementation details; it does not delegate authorship of the game description. If the description is missing, game-specific planning and building wait until you supply it.

The questions cover experience, format, controls, audience, session length, challenge, recovery, presentation, accessibility, content boundaries and the first useful milestone. Player age and gaming experience remain separate from difficulty and access needs. The open-world skill adds relevant questions about travel, density, guidance, persistence and the longer arc.

The answers become a working brief and standalone HTML game plan. It begins with your unchanged description, then shows proposed decisions, alternatives, first build, exclusions, checks, risks and open questions in plain language. When comparisons help, the assistant researches two to four relevant games or techniques from official or authoritative sources. It separates sourced facts from the lesson proposed for your game.

You can review and edit the HTML plan before any game is built. Changes that affect what will be built create a revised plan. Building starts only after you explicitly approve the current version. The page prepares a reply for you to return in chat; clicking a button does not send it automatically.

[Download the blank review example](https://github.com/jamescockburn47/game-development-skills/raw/refs/heads/main/examples/public/design-review.html) and open it in a browser to try the format. It begins with space for your own description and cannot approve a build.

After approval, the assistant builds the smallest playable section that can test the central idea. It may cover controls, feedback, a meaningful decision, connected systems, a setback and recovery.

Checks match the claim: direct tests for rules and saved progress, the running game for controls and connected features, and visual or audio inspection for presentation. Actual play remains necessary for feel, clarity and enjoyment. A successful build or an attractive screenshot does not prove a good game. Failed or incomplete checks stay visible.

The HTML plan remains a living project record. It is revisited after meaningful milestones, playtests, decisions and handoffs, recording evidence and anything needing another look. Routine progress inside approved scope continues; a material change returns to review.

## Making a demo video

Ask for a video and the assistant acts as director, player, camera operator and editor. It explores the existing game, chooses moments that explain its appeal, and shows what a player does and what happens as a result. You can specify length, audience, format or must-show features; you do not have to choose every shot or repeat the workflow in your prompt.

It first records a short trial to check control, framing, timing and sound. It then records separate takes, makes the edit, and checks the finished file. The delivery includes the video, a poster or contact sheet, a short shot plan and instructions for recording it again after the game changes. It uses an isolated session or save where possible to protect your progress.

The method draws on practical experience recording several games: cinematic camera tours, real gameplay demonstrations, repeatable frame-by-frame capture, editing and final-file checks. It preserves lessons from failed captures too, including old weather leaking into a new shot, animation advancing twice, and a recording failing while its preview keeps playing.

It adapts to browser, native, mobile, 2D and 3D games through the tools the assistant actually has. Engine recorders, replays, game controls and screen recording are possible routes. Landscape, portrait and other exports depend on available encoders and playback support. It cannot grant control of an inaccessible device or promise every engine and format has been tested.

The skill distinguishes ordinary play, staged starting conditions, cinematic effects and offline rendering. A polished film must not imply that granted resources were earned or that offline footage proves real-time performance. Technical checks catch problems such as the wrong dimensions, missing audio or a damaged file; watching and listening remain separate checks. Recording an existing game does not restart the game-design questionnaire, and making a video does not authorize publishing it.

## Scope and practical limits

The workflow identifies the hardest uncertain part, tests it with a small experiment and revises before adding dependent content. Focused fixes reuse the brief. Planning-only requests remain planning-only.

The skills also cover practical engineering: respecting an existing project, keeping rules and progress consistent, protecting saves, finding slowdowns and making checks repeatable. More consequential changes receive more scrutiny. The assistant handles these choices without turning the questionnaire into a technical exam.

The assistant uses the tools available to it to read and change project files, run the game, inspect the result, find slow parts and review its work. The skills include no engine and grant no unavailable tools, accounts, paid services or permission to publish. Some checks need a real device or a human player; the skills cannot guarantee fun.

Reusing a brief, testing small ideas and reading the relevant project information can reduce avoidable rework and token use. Questions, checks and coordination also have a cost, so efficiency depends on the project and is not guaranteed.

## Install and use

The simplest route in Codex is to ask it to install the skill from this repository, naming `skills/evidence-led-game-development`, `skills/open-world-game-development` or `skills/automated-game-demo-video`. For manual installation, copy each complete skill folder to the location your assistant reads:

| Assistant | Personal skills | Project skills |
|---|---|---|
| Codex | `~/.agents/skills/` | `.agents/skills/` |
| Claude Code | `~/.claude/skills/` | `.claude/skills/` |

Start a new session if a newly created skills directory is not detected. See [Codex skills](https://learn.chatgpt.com/docs/build-skills) and [Claude Code skills](https://code.claude.com/docs/en/skills).

For Claude chat or Cowork, upload one individual ZIP from `dist/` through **Customize → Skills → Create skill → Upload a skill**, then enable it. See [Claude's skill installation guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

Example prompts for Codex:

```text
Use $evidence-led-game-development. I want to make a game.
```

```text
Use $open-world-game-development. I want to make an open-world game.
```

```text
Use $automated-game-demo-video. Make a one-minute demo of this game; choose the shots.
```

In Claude Code, use `/evidence-led-game-development`, `/open-world-game-development` or `/automated-game-demo-video`, followed by your request. Name the first two together when you want their combined workflow. Add your game description, preferences or a real scope limit such as “planning only”; you do not need to repeat the skill's built-in steps.

The ready-to-share archives are:

- [`evidence-led-game-development.zip`](https://github.com/jamescockburn47/game-development-skills/raw/refs/heads/main/dist/evidence-led-game-development.zip)
- [`open-world-game-development.zip`](https://github.com/jamescockburn47/game-development-skills/raw/refs/heads/main/dist/open-world-game-development.zip)
- [`automated-game-demo-video.zip`](https://github.com/jamescockburn47/game-development-skills/raw/refs/heads/main/dist/automated-game-demo-video.zip)
- [`game-development-skills.zip`](https://github.com/jamescockburn47/game-development-skills/raw/refs/heads/main/dist/game-development-skills.zip) for all three filesystem skill folders together

The skills use the documented `SKILL.md` format and relative files. Their Claude compatibility is based on format and content inspection; it has not been established by a Claude runtime test.

## Technical details

The review document uses schema version 3. Approval and change-request responses use schema version 2. Earlier plan formats can be read for continuity but cannot authorize a new build. The offline Python builder creates the HTML plan, archived revisions and integrity hashes; preparing or downloading a response does not submit it to the assistant.

The repository contains `skills/`, four packaged archives in `dist/`, a blank demonstration at `examples/public/design-review.html`, `package_skills.py`, the public verifier `verify_public.py`, synthetic local checks in `public_tests/`, and `.github/workflows/verify.yml`. The packaging and verification tools use the Python standard library and are tested with Python 3.13.7. Package with `python package_skills.py` and run the canonical public check with:

```bash
python verify_public.py
```

The video skill includes engine-routing guidance, a reusable shot-plan template and `scripts/inspect_video.py`. The inspector needs installed FFprobe and, for a full decode, FFmpeg; it makes no automatic downloads. It checks requested metadata and decode success, while explicitly leaving visual, motion and audio-content judgments unassessed. Run it with `--help` for options. Capture adapters remain specific to the game and its available tools.

The inspector was also checked locally with FFmpeg/FFprobe 7.1.1 against generated clips and an existing game film. A valid clip passed; wrong duration, missing required sound and truncated media failed. This verifies the media checker, not every engine's recording route.

The checks cover structure, references, shared files, packaging, offline review behavior and video-inspector failure cases. Pinned CI rebuilds and compares the ZIPs and public sample, then runs focused synthetic tests, including mocked media-tool responses; it does not record games. Private evaluation records are not published. Model behavior still varies by host and model, sourced comparisons remain limited by available research access, and no structural check can prove universal compliance or game quality.
