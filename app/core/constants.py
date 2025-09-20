# Lead Management
class LeadStatus:
    NEW = "new"
    CONTACTED = "contacted"
    QUALIFIED = "qualified"
    CONVERTED = "converted"

class TenderType:
    TENDER = "tender"
    PRE_TENDER = "pre_tender"
    NON_TENDER = "non_tender"

# User Management
class UserStatus:
    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"

class UserRole:
    ADMIN = "admin"
    MANAGER = "manager"
    SALES_REP = "sales_rep"

# Business Constants
class Currency:
    USD = "USD"
    EUR = "EUR"
    GBP = "GBP"
    INR = "INR"

# File Upload Constants
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB