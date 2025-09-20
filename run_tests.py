import os
import sys
import subprocess

def setup_test_environment():
    test_env = os.environ.copy()
    test_env.update({
        "ENVIRONMENT": "testing",
        "DATABASE_URL": "postgresql://postgres:password@localhost:5432/salescrm_test",
        "SECRET_KEY": "test-secret-key-only-for-testing",
        "DEBUG": "false"
    })
    return test_env

def run_tests(test_type="all", coverage=True, verbose=True):
    cmd = ["python", "-m", "pytest"]
    
    if verbose:
        cmd.append("-v")
    
    if coverage:
        cmd.extend([
            "--cov=app",
            "--cov-report=term-missing",
            "--cov-report=html:htmlcov"
        ])
    
    env = setup_test_environment()
    
    print("Running " + test_type + " tests...")
    
    result = subprocess.run(cmd, env=env)
    
    if result.returncode == 0:
        print("All tests passed!")
    else:
        print("Some tests failed!")
        sys.exit(1)

if __name__ == "__main__":
    run_tests()