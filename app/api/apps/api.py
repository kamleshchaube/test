from fastapi import APIRouter
from app.api.v1.endpoints import leads, accounts, contacts, opportunities, activities, products

api_router = APIRouter()

# Include all endpoint routers
api_router.include_router(leads.router, prefix="/leads", tags=["leads"])
api_router.include_router(accounts.router, prefix="/accounts", tags=["accounts"])
api_router.include_router(contacts.router, prefix="/contacts", tags=["contacts"])
api_router.include_router(opportunities.router, prefix="/opportunities", tags=["opportunities"])
api_router.include_router(activities.router, prefix="/activities", tags=["activities"])
api_router.include_router(products.router, prefix="/products", tags=["products"])