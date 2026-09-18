# Working on Dialogue Memories

Read README.md and docs/validation.md first. The release source is plugins/dialogue-memories/. Keep Memory as the everyday entry point; Making, Legacy, and Fiction are optional forms. Do not add a mandatory menu or sequence.

Preserve the English instructions' intent and gentle procedural tone. Making and Legacy default to third person until the user chooses another perspective. Distinguish memories from invented fiction, the subject from the narrator, and writing from permission to publish.

When working within the Monku_AI layout, read ../../workspace/README.md, ../../workspace/catalog.yaml, and ../../workspace/principles.md if present. Before a remote update, follow ../../workspace/agents/workflows/repository-update-check.md. Standalone clones must not pretend unavailable private files were read.

Keep conversation logs, personal drafts, machine-specific paths, credentials, and internal operating records out of the repository and release ZIP. If a local DESK.md exists, read it; it must remain ignored and untracked.

Use scripts/package.py to build the selected release files. Verify skill contents against the tested source and validate the final package. Do not equate repository publication, successful installation, submission, approval, and directory publication. Record each state separately.
