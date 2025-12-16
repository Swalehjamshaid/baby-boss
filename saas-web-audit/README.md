
# SaaS Web Audit Platform (FastAPI + Railway)

This repository contains a multi-tenant SaaS platform to audit websites across Technical, SEO, Content, UX, Performance, Security, and Compliance metrics. Built with FastAPI, SQLAlchemy (async), Celery + Redis, Alembic, and PostgreSQL on Railway.

## Highlights
- 50 audit metrics scaffold
- PostgreSQL Row-Level Security (RLS) for tenant isolation
- Celery background workers + weekly scheduler
- PDF report generation with ReportLab
- Seed + Reset scripts for demo data
- React (Vite + Tailwind) minimal UI

## Environment Variables
```
DATABASE_URL=postgresql://USER:PASSWORD@HOST:PORT/DBNAME?sslmode=require
SECRET_KEY=your-fastapi-secret
JWT_SECRET=your-jwt-secret
REDIS_URL=redis://:PASSWORD@HOST:PORT/0
EMAIL_API_KEY=your-sendgrid-api-key
SMTP_HOST=smtp.sendgrid.net
SMTP_PORT=587
SMTP_USER=apikey
ENV=production
```

## Migrations
```
cd backend
alembic upgrade head
```

## Services (Railway)
- Web: `uvicorn app.main:app --host 0.0.0.0 --port 8000`
- Worker: `celery -A app.workers.celery_app.celery_app worker --loglevel=INFO -Q audits`
- Beat (optional): `celery -A app.workers.celery_app.celery_app beat --loglevel=INFO`

### Reports Location Update
Generated PDF reports are saved under `templates/Reports/` (e.g., `templates/Reports/audit_<RUN_ID>.pdf`).
The HTML template is at `templates/Reports/report_template.html`.

### Email Templates Location Update
Email templates are located in `templates/Email/`:
- `verification.html`
- `report_ready.html`

## Demo Data: Seed Script
```
export DATABASE_URL=postgresql://USER:PASSWORD@HOST:PORT/DBNAME?sslmode=require
python backend/scripts/seed.py
```

## Reset Demo Data
```
export DATABASE_URL=postgresql://USER:PASSWORD@HOST:PORT/DBNAME?sslmode=require
python backend/scripts/reset.py --dry-run   # preview
python backend/scripts/reset.py --confirm   # execute
```
