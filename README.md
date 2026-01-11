# chalice-uv-template

AWS Chalice project template with uv

## Requirements

- Python 3.13+
- [uv](https://github.com/astral-sh/uv)
- AWS CLI (configured)

## Setup

```bash
# Install dependencies
uv sync

# Install dev dependencies
uv sync --extra dev
```

## Development

```bash
# Run locally
uv run chalice local

# Run tests
uv run pytest

# Lint
uv run ruff check .

# Type check
uv run mypy .
```

## Deployment

```bash
# Deploy to AWS
uv run chalice deploy

# Delete deployment
uv run chalice delete
```

## Project Structure

```
.
├── app.py              # Main application
├── requirements.txt    # Lambda dependencies
├── pyproject.toml      # Project configuration
└── .chalice/
    └── config.json     # Chalice configuration
```
