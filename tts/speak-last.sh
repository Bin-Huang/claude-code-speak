#!/bin/bash
# Read the last assistant text block from the current Claude Code transcript aloud.
# Usage:
#   speak-last.sh                        # auto-locate transcript from $PWD
#   speak-last.sh <transcript.jsonl>     # explicit transcript path
#
# Dependencies:
#   - edge-tts  (pip install edge-tts, or pipx install edge-tts)
#   - afplay    (built into macOS)

set -u

VOICE="en-US-AriaNeural"
RATE="+0%"

if ! command -v edge-tts >/dev/null 2>&1; then
  echo "[tts] edge-tts not found in PATH. Install with: pipx install edge-tts" >&2
  exit 1
fi

if [ -n "${1:-}" ] && [ -f "$1" ]; then
  TRANSCRIPT="$1"
else
  SLUG=$(pwd | sed 's|/|-|g')
  PROJDIR="$HOME/.claude/projects/$SLUG"
  TRANSCRIPT=$(ls -t "$PROJDIR"/*.jsonl 2>/dev/null | grep -v subagents | head -1)
fi

if [ -z "${TRANSCRIPT:-}" ] || [ ! -f "$TRANSCRIPT" ]; then
  echo "[tts] no transcript found for $(pwd)" >&2
  exit 1
fi

TEXT=$(python3 "$(dirname "$0")/extract-last.py" "$TRANSCRIPT")
if [ -z "$TEXT" ]; then
  echo "[tts] no readable text in last assistant message" >&2
  exit 0
fi

MP3=$(mktemp -t tts-XXXXXX).mp3
trap 'rm -f "$MP3"' EXIT

edge-tts --voice "$VOICE" --rate="$RATE" --text "$TEXT" --write-media "$MP3" >/dev/null 2>&1
afplay "$MP3"
