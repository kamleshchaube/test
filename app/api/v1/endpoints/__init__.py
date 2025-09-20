# Import all endpoint modules to register routes
try:
    from app.api.v1.endpoints import auth
    print("✅ Auth endpoints loaded")
except ImportError:
    print("⚠️  Auth endpoints not available")

try:
    from app.api.v1.endpoints import leads
    print("✅ Leads endpoints loaded")
except ImportError:
    print("⚠️  Leads endpoints not available")

try:
    from app.api.v1.endpoints import accounts
    print("✅ Accounts endpoints loaded")
except ImportError:
    print("⚠️  Accounts endpoints not available")

try:
    from app.api.v1.endpoints import contacts
    print("✅ Contacts endpoints loaded")
except ImportError:
    print("⚠️  Contacts endpoints not available")

try:
    from app.api.v1.endpoints import opportunities
    print("✅ Opportunities endpoints loaded")
except ImportError:
    print("⚠️  Opportunities endpoints not available")

try:
    from app.api.v1.endpoints import activities
    print("✅ Activities endpoints loaded")
except ImportError:
    print("⚠️  Activities endpoints not available")

try:
    from app.api.v1.endpoints import products
    print("✅ Products endpoints loaded")
except ImportError:
    print("⚠️  Products endpoints not available")

try:
    from app.api.v1.endpoints import quotes
    print("✅ Quotes endpoints loaded")
except ImportError:
    print("⚠️  Quotes endpoints not available")

try:
    from app.api.v1.endpoints import projects
    print("✅ Projects endpoints loaded")
except ImportError:
    print("⚠️  Projects endpoints not available")

try:
    from app.api.v1.endpoints import reports
    print("✅ Reports endpoints loaded")
except ImportError:
    print("⚠️  Reports endpoints not available")

try:
    from app.api.v1.endpoints import admin
    print("✅ Admin endpoints loaded")
except ImportError:
    print("⚠️  Admin endpoints not available")

__all__ = []