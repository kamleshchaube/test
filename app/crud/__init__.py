# Import all CRUD modules
try:
    from app.crud import user
    print("✅ User CRUD loaded")
except ImportError:
    print("⚠️  User CRUD not available")

try:
    from app.crud import lead
    print("✅ Lead CRUD loaded") 
except ImportError:
    print("⚠️  Lead CRUD not available")

try:
    from app.crud import account
    print("✅ Account CRUD loaded")
except ImportError:
    print("⚠️  Account CRUD not available")

try:
    from app.crud import contact
    print("✅ Contact CRUD loaded")
except ImportError:
    print("⚠️  Contact CRUD not available")

try:
    from app.crud import opportunity
    print("✅ Opportunity CRUD loaded")
except ImportError:
    print("⚠️  Opportunity CRUD not available")

try:
    from app.crud import activity
    print("✅ Activity CRUD loaded")
except ImportError:
    print("⚠️  Activity CRUD not available")

try:
    from app.crud import product
    print("✅ Product CRUD loaded")
except ImportError:
    print("⚠️  Product CRUD not available")

try:
    from app.crud import quote
    print("✅ Quote CRUD loaded")
except ImportError:
    print("⚠️  Quote CRUD not available")

try:
    from app.crud import project
    print("✅ Project CRUD loaded")
except ImportError:
    print("⚠️  Project CRUD not available")

__all__ = []