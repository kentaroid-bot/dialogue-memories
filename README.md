# Dialogue Memories

**Share a memory. Become the heart of a story.**

Turn conversations into stories about experiences, creative work, lives, and imagined worlds. Start with a trip, an ordinary day, or a moment you want to keep. You do not need an outline.

[日本語](README.ja.md)

> “I want to preserve a memory from a trip, but where should I start?”

## Start with Memory

Memory is the everyday starting point. Talk naturally, including through voice input, and shape what you share into a readable piece. Choose your own first-person voice or a third-person, documentary-like portrait. A draft can bring back another detail; keep talking and revise until the piece feels complete.

Three other skills are included for when you want a different form. You can stay with Memory for everyday use.

| Skill | What you can make | Try saying |
|---|---|---|
| [Memory](plugins/dialogue-memories/skills/dialogue-memory/SKILL.md) | Travel stories, personal recollections, firsthand reports | “Turn yesterday’s experience into a short piece with me at its center.” |
| [Making](plugins/dialogue-memories/skills/dialogue-making/SKILL.md) | The decisions and doubts behind creative work | “Help me tell the story behind what I made.” |
| [Legacy](plugins/dialogue-memories/skills/dialogue-legacy/SKILL.md) | A person’s life in their characteristic words and everyday scenes | “I want to preserve stories about my mother’s younger days.” |
| [Fiction](plugins/dialogue-memories/skills/dialogue-fiction/SKILL.md) | Stories grown from an experience or an idea | “I want to write a story, but I don’t yet know what about.” |

Making and Legacy default to third person and can switch to first person at your request. Fiction can develop with you or take the lead when you want a complete story. None of these forms needs a lesson or an uplifting ending.

The instructions are in English. You can talk and write in your preferred language; English and Japanese examples have been tried.

## Version 0.1.0

This repository contains the English initial release. An OpenAI submission draft has been created; a directory listing will be linked here once it is published.

For Codex, add this repository as a marketplace, then install its plugin:

```sh
codex plugin marketplace add https://github.com/kentaroid-bot/dialogue-memories.git
codex plugin add dialogue-memories@dialogue-memories
```

Start a new task and select Dialogue Memories. The repository marketplace and OpenAI directory are separate distribution sources.

The plugin source is in `plugins/dialogue-memories/`. Build a ZIP with Python 3:

```sh
python3 scripts/package.py
```

The result is `dist/dialogue-memories-0.1.0.zip`. Only the plugin files and accompanying public documentation selected by the packaging script are included.

## Your stories stay yours to handle

“Memories” describes the writing material. This plugin does not provide persistent memory or automatic archiving. It bundles writing instructions, with no developer-operated server, external account connection, or telemetry. Your host application processes the conversation under its own settings and policies.

Writing a piece does not itself authorize publishing it. Review personal details and other people’s experiences before sharing. Please keep private stories out of public support issues. See [privacy and data handling](PRIVACY.md).

## Background and support

Created by [Kentaro Takemura / monku.ai](https://monku.ai/), growing from the approach behind [Dialogue Skills](https://github.com/kentaroid-bot/dialogue-skills). Dialogue Memories works independently; Dialogue Skills is not required.

For questions or problems, [open a GitHub issue](https://github.com/kentaroid-bot/dialogue-memories/issues). Use a fictional or anonymized example. See [release validation](docs/validation.md) for the scope of the checks.
