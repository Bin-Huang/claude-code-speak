---
description: Read the last assistant reply aloud
allowed-tools:
  - Bash(nohup:*)
---

Run the following Bash command immediately, then reply with only the single character 🔊. Do not explain, summarize, or read any files.

```bash
nohup bash ~/.claude/tts/speak-last.sh >/dev/null 2>&1 &
```
