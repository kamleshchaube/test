from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.core.config import settings
from app.core.database import engine, Base

# Import all models to ensure tables are created
# This ensures SQLAlchemy knows about all tables
from app.models import (
    user, lead, account, contact, opportunity, 
    activity, product, quote, project
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events"""
    # Startup
    print("🚀 Starting SalesSpark CRM API...")
    
    # Create database tables
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created")
    
    yield
    
    # Shutdown
    print("📴 Shutting down SalesSpark CRM API...")

# Create FastAPI application
app = FastAPI(
    title="SalesSpark CRM API",
    version="2.0.0", 
    description="Enterprise Sales Tools CRM",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
from app.api.v1.api import api_router
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {
        "message": "SalesSpark CRM API v2.0.0 is running",
        "status": "healthy",
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": "2.0.0"}