import pytest
import sys
from pathlib import Path

# Add app to path for testing
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Test configuration
TEST_DATABASE_URL = "sqlite:///./test_salescrm.db"

print("🧪 Test package initialized")
print(f"📁 Project root: {project_root}")
print(f"🗄️  Test database: {TEST_DATABASE_URL}")

__all__ = []