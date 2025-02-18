import pytest
import environ

# Initialize and load environment variables
@pytest.fixture(scope='session', autouse=True)
def load_env_variables():
    env = environ.Env()
    environ.Env.read_env()  # Reads from your .env file
    # Optionally, you can assert or log the values to verify they were loaded
    assert env("EMAIL") is not None, "USERNAME is not set in the .env file"
    assert env("USER_PWD") is not None, "USER_PWD is not set in the .env file"
