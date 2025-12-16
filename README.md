
# SaaS Web Audit Platform (FastAPI + Railway)

A multi-tenant SaaS platform to audit websites across Technical, SEO, Content, UX, Performance, Security, and Compliance metrics. Built with FastAPI, SQLAlchemy (async), Celery + Redis, Alembic, and PostgreSQL on Railway.

## Features
- Multi-tenant (organization-based) with RBAC: Super Admin, Admin, User, Viewer
- JWT auth, email verification placeholder, bcrypt password hashing
- 50 audit metrics scaffold with sample implementations
- Row-Level Security (RLS) for per-organization isolation in PostgreSQL
- Async FastAPI API with background Celery workers for audits
- Alembic migrations and RLS policy migration
- Dockerized and Railway-ready
- Minimal React frontend (Vite + Tailwind) with dashboards

## Quick Start (Railway)
1. **Create Railway project** and add services:
   - Web (Docker) → runs FastAPI `uvicorn app.main:app` on port 8000
   - Worker (Docker) → runs Celery `celery -A app.workers.celery_app.celery_app worker --loglevel=INFO -Q audits`
   - PostgreSQL (Managed)
   - Redis (Managed)

2. **Set environment variables** in Web & Worker:
```
DATABASE_URL=postgresql://USER:PASSWORD@HOST:PORT/DBNAME?sslmode=require
SECRET_KEY=your-fastapi-secret
JWT_SECRET=your-jwt-secret
EMAIL_API_KEY=your-sendgrid-or-ses-key
REDIS_URL=redis://:PASSWORD@HOST:PORT/0
ENV=production
```
> Railway usually injects `DATABASE_URL` automatically for Postgres. Keep `?sslmode=require`.

3. **Deploy** Web & Worker services using the provided `Dockerfile`.

4. **Run migrations** (from Web service shell or CI):
```
cd backend
alembic upgrade head
```

5. **Apply RLS policies** (after initial schema migration):
```
cd backend
alembic upgrade head  # includes RLS policies in migration 0002
```

6. **Test**
- Hit `/api/v1/healthz`
- Register/login, create organization & website
- Trigger an audit run `/api/v1/audits/{website_id}/run`
- View metrics `/api/v1/audits/{website_id}/latest`

## Local Development (optional)
```
cp .env.example .env
docker compose up --build
```

## Frontend
- Located in `frontend/` (Vite + React + Tailwind)
- Configure `VITE_API_BASE` in `.env` or update in `src/services/api.ts`

## Notes
- Alembic uses synchronous `psycopg2` driver for migrations; the app uses async `asyncpg`.
- RLS relies on setting `app.current_organization_id` per request.
- Email verification and advanced metrics are scaffolded; customize as needed.

## License
MIT


## Advanced Features Added
- Email verification (SMTP via SendGrid)
- Admin panel endpoints (users, thresholds, subscription)
- Organization settings (branding)
- PDF report generation (ReportLab) automatically after audits
- Celery beat weekly scheduling to queue audits for all active websites
- GitHub Actions workflow for Railway deployment (requires `RAILWAY_TOKEN` secret)

### Run Alembic migrations
```
cd backend
alembic upgrade head  # applies 0001, 0002, 0003
```

### Celery services on Railway
Create two worker services:
- **Worker**: `celery -A app.workers.celery_app.celery_app worker --loglevel=INFO -Q audits`
- **Beat** (optional): `celery -A app.workers.celery_app.celery_app beat --loglevel=INFO`

### Email setup
Configure SMTP variables in Railway:
```
EMAIL_API_KEY=your-sendgrid-api-key
SMTP_HOST=smtp.sendgrid.net
SMTP_PORT=587
SMTP_USER=apikey
```

