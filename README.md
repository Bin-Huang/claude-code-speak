# claude-code-speak

A `/speak` slash command for [Claude Code](https://claude.com/claude-code) that reads the last assistant reply aloud. **No TTS API key required.**

Useful when you'd rather listen than read — long explanations, background while you work, accessibility, or language practice.

macOS only.

## Install

The simplest way is to hand this repo to Claude Code and ask it to install. Paste this into a Claude Code session:

> Please install https://github.com/Bin-Huang/claude-code-speak by cloning it to a temp dir, then copying `commands/speak.md` to `~/.claude/commands/speak.md` and the `tts/` directory to `~/.claude/tts/`. Then `chmod +x ~/.claude/tts/speak-last.sh`. Also check with `command -v edge-tts` whether the dependency is installed, and give me the install command if it's missing. Finally, pick a fitting default voice and update the `VOICE=` line near the top of `~/.claude/tts/speak-last.sh`. To decide the language, look at my 3 most recently modified transcripts under `~/.claude/projects/*/*.jsonl` and check what language I typed in the `user` messages — don't rely on the language of this instruction. Run `edge-tts --list-voices` to see options.

Or install manually:

```bash
git clone https://github.com/Bin-Huang/claude-code-speak.git
cd claude-code-speak
mkdir -p ~/.claude/commands ~/.claude/tts
cp commands/speak.md ~/.claude/commands/
cp tts/speak-last.sh tts/extract-last.py ~/.claude/tts/
chmod +x ~/.claude/tts/speak-last.sh

# one small dependency; nothing else to configure
pipx install edge-tts   # or: pip install --user edge-tts
```

## Usage

In any Claude Code session, type:

```
/speak
```

Claude replies with 🔊 and you hear the previous message played back.

## Voice

To change the voice, edit the `VOICE=` line at the top of `~/.claude/tts/speak-last.sh`. Run `edge-tts --list-voices` to see the full list.

## Troubleshooting

`/speak` runs in the background and suppresses output, so if you hear nothing you won't see why. Run the script directly to see the error:

```bash
~/.claude/tts/speak-last.sh
```

Common causes: `edge-tts` not installed, or no transcript found for the current working directory.

## Uninstall

```bash
rm ~/.claude/commands/speak.md
rm -r ~/.claude/tts
```

## License

MIT — see [LICENSE](LICENSE).
