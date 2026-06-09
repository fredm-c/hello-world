# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

A Python full-stack web application built with FastAPI (backend + server-side rendering via Jinja2 templates). The app serves HTML pages and is structured to grow into a full website or API service.

## Stack

- **Backend / server**: FastAPI + Uvicorn
- **Templating**: Jinja2 (server-side rendered HTML)
- **Testing**: pytest + HTTPX `TestClient`
- **Linting / formatting**: Ruff

## Development setup

```bash
pip install -r requirements.txt -r requirements-dev.txt
```

## Commands

```bash
# Run development server (auto-reloads on file changes)
uvicorn app.main:app --reload

# Run all tests
pytest

# Run a single test
pytest tests/test_main.py::test_index

# Lint
ruff check .

# Auto-fix lint issues
ruff check . --fix
```

## Architecture

```
app/
├── main.py          # FastAPI app instance; mounts static files, registers routers
├── routes/          # APIRouter modules — add routers here, include them in main.py
├── templates/       # Jinja2 HTML templates; base.html is the shared layout
└── static/
    ├── css/style.css
    └── js/main.js
tests/               # pytest suite; uses FastAPI's synchronous TestClient
```

**Adding a new page/route**: Create a module in `app/routes/`, define an `APIRouter`, then call `app.include_router(...)` in `app/main.py`. Return a `TemplateResponse` for HTML pages or a plain dict/Pydantic model for JSON endpoints.

**Templates**: All page templates extend `base.html` using `{% extends "base.html" %}`. Pass data to templates via the context dict in `TemplateResponse`.

**Static assets**: Anything in `app/static/` is served at `/static/...`. Reference them as `/static/css/style.css` in HTML.
