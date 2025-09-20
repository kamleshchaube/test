
# Import all schema modules
try:
    from app.schemas import user
    print("✅ User schemas loaded")
except ImportError:
    print("⚠️  User schemas not available")

try:
    from app.schemas import auth
    print("✅ Auth schemas loaded")
except ImportError:
    print("⚠️  Auth schemas not available")

try:
    from app.schemas import lead
    print("✅ Lead schemas loaded")
except ImportError:
    print("⚠️  Lead schemas not available")

try:
    from app.schemas import account
    print("✅ Account schemas loaded")
except ImportError:
    print("⚠️  Account schemas not available")

try:
    from app.schemas import contact
    print("✅ Contact schemas loaded")
except ImportError:
    print("⚠️  Contact schemas not available")

try:
    from app.schemas import opportunity
    print("✅ Opportunity schemas loaded")
except ImportError:
    print("⚠️  Opportunity schemas not available")

try:
    from app.schemas import activity
    print("✅ Activity schemas loaded")
except ImportError:
    print("⚠️  Activity schemas not available")

try:
    from app.schemas import product
    print("✅ Product schemas loaded")
except ImportError:
    print("⚠️  Product schemas not available")

try:
    from app.schemas import quote
    print("✅ Quote schemas loaded")
except ImportError:
    print("⚠️  Quote schemas not available")

try:
    from app.schemas import project
    print("✅ Project schemas loaded")
except ImportError:
    print("⚠️  Project schemas not available")

__all__ = []