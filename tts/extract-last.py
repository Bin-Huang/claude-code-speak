#!/usr/bin/env python3
"""Extract the last assistant text block from a Claude Code transcript JSONL.

The transcript format is one JSON object per line. We walk from the end to find
the most recent message with type="assistant" that contains at least one text
content block, then strip code blocks, links, and other markdown noise that
doesn't read well when spoken aloud.
"""
import json
import re
import sys


def extract_last_text(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in reversed(lines):
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        if obj.get("type") != "assistant":
            continue
        content = obj.get("message", {}).get("content", [])
        if not isinstance(content, list):
            continue
        texts = [
            b.get("text", "")
            for b in content
            if isinstance(b, dict) and b.get("type") == "text"
        ]
        texts = [t for t in texts if t.strip()]
        if texts:
            return texts[-1]
    return None


def clean(text):
    text = re.sub(r"```[\s\S]*?```", " ", text)
    text = re.sub(r"`([^`\n]+)`", r"\1", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"(?:~|\.{1,2})?/[\w.\-]+(?:/[\w.\-]+)+", " ", text)
    text = re.sub(r"^\s*#+\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"\1", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: extract-last.py <transcript.jsonl>")
    raw = extract_last_text(sys.argv[1])
    if not raw:
        return
    cleaned = clean(raw)
    if cleaned:
        print(cleaned)


if __name__ == "__main__":
    main()
