#!/usr/bin/env python3
"""Build an explicitly selected plugin archive from the release source."""
import hashlib
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

repo = Path(__file__).resolve().parents[1]
plugin = repo / "plugins" / "dialogue-memories"
manifest = json.loads((plugin / ".codex-plugin" / "plugin.json").read_text())
files = [plugin / ".codex-plugin" / "plugin.json"]
for name in ("dialogue-memory", "dialogue-making", "dialogue-legacy", "dialogue-fiction"):
    files.extend([plugin / "skills" / name / "SKILL.md", plugin / "skills" / name / "agents" / "openai.yaml"])
if (plugin / "assets").exists():
    files.extend(sorted((plugin / "assets").glob("*.png")))
entries = {f.relative_to(plugin).as_posix(): f for f in files}
for name in ("PRIVACY.md", "LICENSE", "TERMS.md"):
    if (repo / name).is_file():
        entries[name] = repo / name
out = repo / "dist"
out.mkdir(exist_ok=True)
archive = out / f"dialogue-memories-{manifest['version']}.zip"
with ZipFile(archive, "w", ZIP_DEFLATED) as z:
    for name, path in sorted(entries.items()):
        if path.is_symlink() or not path.is_file():
            raise ValueError(f"Not a regular release file: {name}")
        info = ZipInfo(name, (2026, 9, 18, 0, 0, 0))
        info.compress_type = ZIP_DEFLATED
        info.external_attr = 0o100644 << 16
        z.writestr(info, path.read_bytes())
checks = {name: hashlib.sha256(path.read_bytes()).hexdigest() for name, path in sorted(entries.items())}
with ZipFile(archive) as z:
    assert z.namelist() == sorted(entries)
    for name, path in entries.items():
        assert z.read(name) == path.read_bytes()
(out / "manifest.json").write_text(json.dumps({"version": manifest["version"], "files": checks, "archive_sha256": hashlib.sha256(archive.read_bytes()).hexdigest()}, indent=2) + "\n")
print(f"Built {archive.name}: {len(entries)} files")
