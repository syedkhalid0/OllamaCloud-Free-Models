# Ollama Cloud Free Models

A curated list of free models available on [Ollama Cloud](https://ollama.com). This repository automatically tracks which models are accessible for free.

## Overview

Ollama Cloud offers both free and paid AI models. This project monitors and lists all models that can be used without payment. The data is updated automatically every 4 hours via GitHub Actions.

## Files

| File | Description |
|------|-------------|
| `models.json` | List of models in JSON format |
| `models.csv` | List of models in CSV format |

## Usage

```bash
# Fetch models.json directly
curl https://raw.githubusercontent.com/syedkhalid0/OllamaCloud-Free-Models/main/models.json
```

Or,
```bash
# Filter free models
curl -s https://raw.githubusercontent.com/syedkhalid0/OllamaCloud-Free-Models/main/models.json | jq '.[] | select(.isFree == true)'
```

## Automation

This repository uses GitHub Actions to fetch the latest model data from Ollama Cloud API every 4 hours. The workflow automatically updates `models.csv` and `models.json` with the current free/paid status of each model.

---

## Free Models

These models are available at no cost. No subscription is required (you only need a free Ollama Cloud account with an API key).

<!-- FREE_MODELS_TABLE -->
| Model |
|-------|
| gemma4:31b |
| gpt-oss:120b |
| gpt-oss:20b |
| minimax-m2.5 |
| minimax-m3 |
| nemotron-3-nano:30b |
| nemotron-3-ultra |
<!-- FREE_MODELS_TABLE_END -->

## Paid Models

These models require a paid subscription to access.

<!-- PAID_MODELS_TABLE -->
| Model |
|-------|
| deepseek-v4-flash |
| deepseek-v4-pro |
| glm-5.1 |
| glm-5.2 |
| kimi-k2.5 |
| kimi-k2.6 |
| kimi-k2.7-code |
| minimax-m2.7 |
| mistral-large-3:675b |
| nemotron-3-super |
| qwen3.5:397b |
<!-- PAID_MODELS_TABLE_END -->

---

## Contributing

Improvements are welcome! If you'd like to add new features, improve the automation, or fix something, feel free to open a pull request.

## Related

- [Ollama Cloud](https://ollama.com)
- [Ollama GitHub](https://github.com/ollama/ollama)
