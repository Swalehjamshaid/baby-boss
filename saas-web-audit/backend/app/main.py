
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.routes import health, auth, websites, audits, reports

app = FastAPI(title="SaaS Web Audit Platform")
app.add_middleware(CORSOMiddleware:=CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"], allow_credentials=True)

app.include_router(health.router, prefix="/api/v1", tags=["health"])
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(websites.router, prefix="/api/v1/websites", tags=["websites"])
app.include_router(audits.router, prefix="/api/v1/audits", tags=["audits"])
app.include_router(reports.router, prefix="/api/v1/reports", tags=["reports"])
