# claude-code-speak

A `/speak` slash command for [Claude Code](https://claude.com/claude-code) that reads the last assistant reply aloud. **No TTS API key required.**

Useful when you'd rather listen than read — long explanations, background while you work, accessibility, or language practice.

macOS only.

## Install

The simplest way is to hand this repo to Claude Code and ask it to install. Paste this into a Claude Code session:

> Please install https://github.com/Bin-Huang/claude-code-speak by cloning it to a temp dir, then copying `commands/speak.md` to `~/.claude/commands/speak.md` and the `tts/` directory to `~/.claude/tts/`. Then `chmod +x ~/.claude/tts/speak-last.sh`. Also check with `command -v edge-tts` whether the dependency is installed, and give me the install command if it's missing.

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

## Configuration

Set environment variables in your shell (e.g. `~/.zshrc`) to override defaults:

| Variable            | Default              | Notes                                       |
| ------------------- | -------------------- | ------------------------------------------- |
| `CLAUDE_TTS_VOICE`  | `en-US-AriaNeural`   | Voice name                                  |
| `CLAUDE_TTS_RATE`   | `+0%`                | e.g. `+10%`, `-20%`                         |

Some popular voices:

- English: `en-US-AriaNeural`, `en-US-GuyNeural`, `en-GB-SoniaNeural`
- 中文: `zh-CN-XiaoxiaoNeural`, `zh-CN-YunxiNeural`, `zh-TW-HsiaoChenNeural`
- 日本語: `ja-JP-NanamiNeural`
- Español: `es-ES-ElviraNeural`

Run `edge-tts --list-voices` to see the full list.

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
