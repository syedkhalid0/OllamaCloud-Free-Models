# Ollama Cloud Free Models (Archived)

> [!IMPORTANT]
> **Repository Archived, November 2026**
>
> As of **November 9, 2026**, Ollama officially ended its free cloud model tier and transitioned all Free plan accounts to a **Pay-As-You-Go** credit system. Because there are no longer any free models available on Ollama Cloud, automated tracking is no longer needed.
>
> This repository remains public as a historical archive of how Ollama Cloud's free tier worked while it lasted. Thank you to everyone who starred, forked, and used this tracker!

---

## Goodbye & Final Snapshot

While it lasted, this project automatically polled the Ollama Cloud API every 4 hours via GitHub Actions to track which cloud-hosted models could be queried for free without a paid subscription.

On **November 9, 2026**, Ollama announced:
> *"Starting November 9, 2026, Free plan accounts will automatically switch to pay as you go. You add credits and pay only for what you use, with no subscription and no service fees. Nothing changes on other plans, and running models locally on your own computer will always be free."*

### The Last Free Cloud Models (Pre–November 9, 2026)
Before the transition to pay-as-you-go, these were the final cloud models available at no cost:
- `gemma4:31b`
- `gpt-oss:120b`
- `gpt-oss:20b`
- `nemotron-3-super`
- `nemotron-3-ultra`
- `nemotron-3-nano:30b`

---

## Historical `README.md`

> *The sections below are preserved from the active lifecycle of this repository.*

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

<!-- FREE_MODELS_TABLE_END -->

## Paid Models

These models require a paid subscription to access.

<!-- PAID_MODELS_TABLE -->
| Model |
|-------|
| beam |
| clef:27b |
| deepseek-v4-pro:0813 |
| deepseek-v4.1-flash |
| deepseek-v4.1-flash:1017 |
| gemma4:31b |
| glm-5.2 |
| glm-5.3 |
| glm-5.3-flash |
| gpt-oss:120b |
| gpt-oss:20b |
| inkling-2-small |
| kimi-k2.6 |
| kimi-k2.7-code |
| kimi-k3 |
| kimi-k3.1-pro |
| mimo-v2.6-flash |
| mimo-v2.6-pro |
| minimax-m3 |
| minimax-m3.1-flash |
| mistral-large-4 |
| muse-spark-open |
| nemotron-3-super |
| nemotron-3-ultra |
<!-- PAID_MODELS_TABLE_END -->

---

## Contributing

Improvements are welcome! If you'd like to add new features, improve the automation, or fix something, feel free to open a pull request.

## Related

- [Ollama Cloud](https://ollama.com)
- [Ollama GitHub](https://github.com/ollama/ollama)
