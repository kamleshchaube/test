from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from app.core.config import settings

# Sync database setup
engine = create_engine(
    str(settings.DATABASE_URL),
    pool_pre_ping=True,
    pool_recycle=300,
    pool_size=20,
    max_overflow=0,
    echo=False  # Set to True for SQL debugging
)

# Async database setup
async_engine = create_async_engine(
    str(settings.DATABASE_URL).replace("postgresql://", "postgresql+asyncpg://"),
    pool_pre_ping=True,
    pool_recycle=300,
    pool_size=20,
    max_overflow=0,
    echo=False
)

# Create SessionLocal class (sync)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create AsyncSessionLocal class (async)
AsyncSessionLocal = sessionmaker(
    async_engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)

# Create Base class for models
Base = declarative_base()

def get_database_url():
    """Get the database URL"""
    return str(settings.DATABASE_URL)

def create_database():
    """Create all database tables"""
    Base.metadata.create_all(bind=engine)

def drop_database():
    """Drop all database tables"""
    Base.metadata.drop_all(bind=engine)

def get_db():
    """
    Dependency function to get database session (sync)
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def get_async_session():
    """
    Dependency function to get async database session
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()

# Alternative naming for compatibility
get_async_db = get_async_session