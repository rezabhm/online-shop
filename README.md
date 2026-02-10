# B2B Cross-Border Procurement Platform (Django Backend)

Production-minded DRF backend for an enterprise procurement lifecycle from sourcing to delivery.

## Project Structure Tree

```text
.
├── apps/
│   ├── accounts/
│   ├── profiles/
│   ├── catalog/
│   ├── suppliers/
│   ├── marketplace/
│   ├── rfq/
│   ├── messaging/
│   ├── orders/
│   ├── payments/
│   ├── operations/
│   ├── logistics/
│   ├── customs/
│   ├── reviews/
│   ├── notifications/
│   ├── audit/
│   └── common/
├── config/
│   ├── settings/
│   │   ├── base.py
│   │   ├── dev.py
│   │   └── prod.py
│   ├── celery.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── docs/
│   └── architecture.md
├── docker-compose.yml
├── Dockerfile
├── .env.example
├── manage.py
└── requirements.txt
```

## Quick Start

```bash
cp .env.example .env
docker compose up --build
```

## Architecture

See `docs/architecture.md` for:
- architecture overview
- domain model diagram
- app-by-app responsibilities
- state machines
- async flows
- deployment and scalability model

## API Versioning

All APIs are mounted under:

- `/api/v1/`

## Core Sample Endpoints

- `POST /api/v1/auth/token/`
- `POST /api/v1/auth/token/refresh/`
- `GET/POST /api/v1/rfqs/`
- `POST /api/v1/rfqs/{id}/open/`
- `GET/POST /api/v1/orders/`
- `POST /api/v1/orders/{id}/transition/`
- `GET/POST /api/v1/payments/`
- `POST /api/v1/payments/{id}/hold_escrow/`

## Notes

This repository provides a robust structural baseline and core domain entities/services/state transitions suitable for extension into a full enterprise rollout.
