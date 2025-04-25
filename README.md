Test runs:  
[![UI tests](https://github.com/qaherasymchuk/selenium-pytest-example/actions/workflows/example_selenium_tests.yml/badge.svg)](https://github.com/qaherasymchuk/selenium-pytest-example/actions/workflows/example_selenium_tests.yml)

Demo:
![Demo](assets/demo.gif)

# 📦 Selenium with Pytest-BDD Example

This project demonstrates how to use **Selenium** for browser automation together with **pytest** and **pytest-bdd** for behavior-driven development (BDD) testing in Python.


## 🧪 Testing

### ✅ Behavior-Driven Tests
- **Framework**: [pytest-bdd](https://github.com/pytest-dev/pytest-bdd)
- **Feature files**: `tests/search/features/*.feature`
- **Step definitions**: `tests/search/step_defs/*.py`

### ✅ Classic Pytest Tests
- Examples like `tests/test_open_video.py`

### 🧷 Fixtures
Defined in `tests/conftest.py`, including Selenium WebDriver setup with support for:
- `chrome`
- `firefox`
- `ie`
- `safari`
- `mobile_emulator` (e.g., iPhone 12 Pro)

## 🗂️ Logs and Screenshots

All logs, HTML dumps, and screenshots are automatically saved during test execution in:


These files are helpful for debugging failed tests and visual verification.

## 🚀 How to Run

1. **Install dependencies**
    ```bash
    pipenv install
    ```

2. **Set the browser to use**
    ```bash
    export BROWSER=chrome  # or firefox, mobile_emulator, etc.
    ```

3. **Run all tests**
    ```bash
    pipenv run pytest
    ```

## 📚 Tech Stack

- 🐍 Python
- 🧪 pytest
- 🧬 Selenium WebDriver
- 🧾 pytest-bdd
- 🏗 Page Object Model
