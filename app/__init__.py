__version__ = "2.0.0"
__title__ = "SalesSpark CRM"
__description__ = "Enterprise Sales Tools & CRM System"
__author__ = "SalesSpark Team"

# Import commonly used modules for easier access
from app.core.config import settings
from app.core.database import get_db

# Package metadata
__all__ = [
    "settings",
    "get_db"
]