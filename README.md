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

# Copy environment file and configure AWS credentials
cp .envrc.example .envrc
# Edit .envrc with your AWS credentials

# Allow direnv to load environment variables
direnv allow

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
├── .chalice/
│   └── config.json     # Chalice configuration
├── tests/
│   ├── __init__.py
│   └── test_app.py     # Basic tests
├── .envrc.example      # Environment variables template
├── .gitignore
├── .python-version     # Python version for uv
├── LICENSE             # MIT License
├── README.md
├── app.py              # Main application
├── pyproject.toml      # Project configuration
└── requirements.txt    # Lambda dependencies
```
