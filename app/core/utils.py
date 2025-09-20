import re
import hashlib
import secrets
from typing import Any, Dict
from datetime import datetime, date
from decimal import Decimal

def generate_id(prefix: str = "") -> str:
    """Generate a unique ID with optional prefix"""
    random_part = secrets.token_hex(8)
    if prefix:
        return prefix + "_" + random_part
    return random_part

def validate_email(email: str) -> bool:
    """Validate email address format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def format_currency(amount: float, currency: str = "USD") -> str:
    """Format amount as currency"""
    currency_symbols = {
        "USD": "$",
        "EUR": "€", 
        "GBP": "£",
        "INR": "₹"
    }
    
    symbol = currency_symbols.get(currency, currency)
    return symbol + str(amount)