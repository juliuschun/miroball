<div align="center">

# MiroBall

**Swarm Intelligence Simulation Engine for Quantitative Finance**

[![CI](https://github.com/juliuschun/miroball/actions/workflows/ci.yml/badge.svg)](https://github.com/juliuschun/miroball/actions/workflows/ci.yml)
[![Docker](https://img.shields.io/badge/Docker-Build-2496ED?style=flat-square&logo=docker&logoColor=white)](https://github.com/juliuschun/miroball/pkgs/container/miroball)
[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-blue.svg)](LICENSE)

</div>

## Overview

MiroBall is a multi-agent swarm intelligence engine that creates high-fidelity parallel digital worlds from seed information (breaking news, policy drafts, financial signals). Thousands of autonomous agents — each with independent personality, long-term memory, and behavioral logic — interact freely within the simulation to surface emergent group dynamics.

> **Input:** Upload seed material (data reports, scenarios) and describe your prediction needs in natural language.
>
> **Output:** A detailed prediction report and a deeply interactive digital world you can explore.

## Architecture

```
MiroBall/
├── backend/          # Flask API + Anthropic LLM + OASIS simulation
│   ├── app/
│   │   ├── api/      # REST endpoints (graph, simulation, report)
│   │   ├── services/ # Core business logic
│   │   └── utils/    # LLM client, logger, helpers
│   └── tests/        # pytest test suite
├── frontend/         # Vue.js 3 + D3.js visualization
└── .github/workflows # CI/CD (test + Docker build)
```

## Quick Start

### Prerequisites

- Python 3.11+, [uv](https://docs.astral.sh/uv/)
- Node.js 18+
- Anthropic API access (or Max subscription)
- [Zep](https://www.getzep.com/) API key (for memory graph)

### Setup

```bash
# Clone
git clone https://github.com/juliuschun/miroball.git
cd miroball

# Configure
cp .env.example .env
# Edit .env with your keys

# Install & run
npm run setup:all
npm run dev
```

Backend runs on `http://localhost:5001`, frontend on `http://localhost:3000`.

### Docker

```bash
docker compose up -d
```

## CI/CD

The project includes two GitHub Actions workflows:

| Workflow | Trigger | What it does |
|----------|---------|-------------|
| **CI** (`ci.yml`) | Push/PR to `main` | Backend tests (pytest) + Frontend build + Docker build test |
| **Docker Image** (`docker-image.yml`) | Tag push or manual | Build & push to GHCR |

## Key Differences from MiroFish

MiroBall is a fork of [MiroFish](https://github.com/666ghj/MiroFish) with the following changes:

- **LLM Backend**: Switched from OpenAI-compatible API to **Anthropic SDK** direct calls (Claude models)
- **Focus**: Tailored for quantitative finance and market simulation use cases
- **CI/CD**: Added comprehensive test suite and GitHub Actions pipeline
- **Branding**: Renamed to MiroBall throughout the codebase

## License

AGPL-3.0 — see [LICENSE](LICENSE) for details.

Based on [MiroFish](https://github.com/666ghj/MiroFish) by the MiroFish Team, powered by [OASIS](https://github.com/camel-ai/oasis).
