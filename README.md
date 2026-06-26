# QA Automation Portfolio Project

![Portfolio QA Tests](https://github.com/MittenzDev/qa-automation-portfolio/actions/workflows/tests.yml/badge.svg)

This project is a lightweight QA automation framework built with **Python, Playwright, and Requests**, designed to validate both:

- UI content (portfolio pages)
- Link integrity (internal + external URLs)
- Automated reporting via HTML
- CI execution using GitHub Actions

---

## What this project does

This framework automatically:

### Link Validation
- Crawls all links from a live website using Playwright
- Checks each link using HTTP requests
- Applies rules for internal vs external URLs
- Ignores known-safe or irrelevant links (e.g. LinkedIn, login pages)
- Detects broken links and categorizes failures

### Portfolio Content Validation
- Validates blog/project pages
- Checks that:
  - Titles exist
  - Content exists and is not empty
  - Pages are structurally valid

### Reporting
- Generates a `report.html` file after every test run
- Displays:
  - URL
  - HTTP status
  - Pass/Fail result
- Includes summary statistics

---

## Architecture

This project follows a lightweight framework structure with:
- **Test Layer (Playwright + Pytest)**: Separates test execution (Playwright/Pytest) from validation logic (Requests-based checks)
- **Validation Layer (Requests)**: HTTP checks and rule enforcement
- **Framework Layer**: Reusable modules (`link_checker`, `report_generator.py`)
- **Reporting Layer**: Generates HTML test reports (`report.html`)
- **CI Layer (GitHub Actions)**: Automated execution and artifact upload

---

## Project Structure

```bash
PytestPython/
│
├── framework/
│   ├── link_checker.py
│   ├── report_generator.py
│
├── tests/
│   ├── test_links.py
│   ├── test_portfolio.py
│
├── report.html (generated)
├── requirements.txt
├── .github/workflows/tests.yml
```
---

## How to run locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
```
### 2. Install Playwright browsers

Install required browser dependencies:
```bash
playwright install --with-deps
```
### 3. Run tests
```bash
pytest -s
```
---

## Output

After running tests, an HTML report (`report.html`) is generated.

It includes:
- Total links tested
- Passed / failed count
- Color-coded results
- Full URL list

---

## GitHub Actions

Every push or pull request automatically:

- Runs all tests
- Executes Playwright browser automation
- Generates report.html
- Uploads it as an artifact

You can find it under:

GitHub → Actions → Latest Run → Artifacts

---

## Key Technologies
* Python
* Playwright
* Requests
* Pytest
* GitHub Actions

---

## Author

Juan Torres
QA Automation Engineer Portfolio Project
