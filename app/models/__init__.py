from app.models.base import BaseModel

# Core CRM Models
from app.models.user import User
from app.models.lead import Lead
from app.models.account import Account
from app.models.contact import Contact
from app.models.opportunity import Opportunity
from app.models.activity import Activity

# Product & Pricing Models
from app.models.product import Product
from app.models.rate_card import RateCard
from app.models.rate_card_item import RateCardItem
from app.models.customer_rate_card import CustomerRateCard
from app.models.purchase_cost import PurchaseCost
from app.models.exchange_rate import ExchangeRate

# Quote Models
from app.models.quote import Quote
from app.models.quote_item import QuoteItem

# Project & Service Delivery Models  
from app.models.project import Project
from app.models.project_line_item import ProjectLineItem
from app.models.project_history import ProjectHistory
from app.models.project_delivery_log import ProjectDeliveryLog

# Campaign Models
from app.models.campaign import Campaign

# History & Tracking Models
from app.models.stage_history import StageHistory

print("✅ All SalesSpark CRM models loaded successfully")

__all__ = [
    "BaseModel",
    # Core CRM
    "User", "Lead", "Account", "Contact", "Opportunity", "Activity",
    # Products & Pricing  
    "Product", "RateCard", "RateCardItem", "CustomerRateCard", "PurchaseCost", "ExchangeRate",
    # Quotes
    "Quote", "QuoteItem", 
    # Projects
    "Project", "ProjectLineItem", "ProjectHistory", "ProjectDeliveryLog",
    # Campaigns
    "Campaign",
    # History
    "StageHistory"
]