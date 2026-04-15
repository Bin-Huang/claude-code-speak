---
description: Stop any ongoing /speak playback
allowed-tools:
  - Bash(pkill:*)
---

Run the following Bash command immediately, then reply with only the single character 🔇. Do not explain, summarize, or read any files.

```bash
pkill -f speak-last.sh; pkill -f 'afplay .*/tts-'; pkill -f 'edge-tts .*tts-'; true
```
