# Mistral AI Toolkit

> **Unmaintained.** Use [`mistralai`](https://github.com/mistralai/client-python), Mistral's official Python SDK.

I've always preferred pair programming with LLMs from the terminal over copy-pasting from browser chats. Web UIs hit rate limits, lose context across tabs, and break flow when I'm moving code back and forth. When Mistral opened their API early 2024, the first-party Python SDK was barebones. I wanted streaming, JSON mode, system prompts, and both chat/text modes behind a single CLI and Python entry. So I built this for myself.

Python wrapper and CLI for Mistral's open and closed models.

## Install

```bash
git clone https://github.com/ramonclaudio/mistral-ai-toolkit.git
cd mistral-ai-toolkit
pip install -r requirements.txt
```

## Configuration

Get an API key at https://mistral.ai/. Set via env var, `.env`, or pass directly:

```bash
export MISTRAL_API_KEY=your_api_key
```

## CLI

```bash
# Chat mode
python cli.py --chat

# Text mode
python cli.py --text --prompt "Which one is heavier, a pound of iron or a kilogram of feathers?"
```

Type `exit` or `quit` to leave chat.

## Python

```python
from mistral import Chat
Chat().run()

from mistral import Text
Text().run(prompt="Your question here")
```

## Options

| Description | CLI | Python |
| --- | --- | --- |
| Chat mode | `--chat` | `Chat()` |
| Text mode | `--text` | `Text()` |
| API key | `--api_key` | `api_key=` |
| Model | `--model` | `model=` |
| Prompt | `--prompt` | `prompt=` |
| Streaming | `--stream` | `stream=True` |
| JSON mode | `--json` | `json=True` |
| System prompt | `--system_prompt` | `system_prompt=` |
| Max tokens | `--max_tokens` | `max_tokens=` |
| Temperature | `--temperature` | `temperature=` |
| Top-p | `--top_p` | `top_p=` |
| Random seed | `--random_seed` | `random_seed=` |
| Safe prompt | `--safe_prompt` | `safe_prompt=True` |

## Models

| Model | Max tokens |
| --- | --- |
| `open-mistral-nemo` | 128000 |
| `open-mistral-7b` | 32000 |
| `open-mixtral-8x7b` | 32000 |
| `open-mixtral-8x22b` | 64000 |
| `mistral-small-latest` | 32000 |
| `mistral-medium-latest` | 32000 |
| `mistral-large-latest` | 32000 |

## License

MIT
