
# Playwright Login Test — The Internet Herokuapp

Automated test suite for the login functionality of [The Internet Herokuapp](https://the-internet.herokuapp.com/login) using Playwright and pytest.

---

## Project Structure
```
playwright-herokuapp-login/
│
├── pages/
│   └── login_page.py       # Page Object Model for the login page
│
├── tests/
│   └── test_login.py       # Test cases
│
├── conftest.py             # Shared browser configuration
├── config.py               # URLs and global settings
├── pytest.ini              # pytest configuration
├── requirements.txt        # Python dependencies
└── README.md
```

## Test Cases

| # | Test | Description |
|---|------|-------------|
| 1 | `test_successful_login` | Login with valid credentials and verify redirect to secure area |
| 2 | `test_invalid_username` | Login with invalid username and verify error message |
| 3 | `test_invalid_password` | Login with invalid password and verify error message |

---

## Prerequisites

- Python 3.9+
- Google Chrome browser

---

## Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install
```

---

## Running the Tests

### Run all tests
```bash
pytest tests/ -v
```

### Run a specific test
```bash
pytest tests/test_login.py::TestLogin::test_successful_login -v
```

### Run in random order
```bash
pytest tests/ -v -p randomly
```

### Repeat the same random order
```bash
pytest tests/ -v --randomly-seed=last
```

### Run only failed tests from last run
```bash
pytest tests/ -v --last-failed
```

---

## Expected Output
```
tests/test_login.py::TestLogin::test_successful_login PASSED
tests/test_login.py::TestLogin::test_invalid_username PASSED
tests/test_login.py::TestLogin::test_invalid_password PASSED

====== 3 passed in 8.23s ======
```

---

## Dependencies

| Package | Purpose |
|---|---|
| `playwright` | Browser automation |
| `pytest` | Test framework |
| `pytest-playwright` | Playwright integration with pytest |
| `pytest-randomly` | Runs tests in random order |
