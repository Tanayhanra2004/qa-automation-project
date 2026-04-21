 QA Automation Framework (Hybrid UI + API)

📌 Overview

This project is an advanced **Hybrid Test Automation Framework** built using Python.
It supports **UI Automation, API Testing, Data-Driven Testing, and CI/CD integration**.

---

 🧰 Tech Stack

* Python
* Selenium WebDriver
* pytest
* Requests (API Testing)
* Allure Reports
* PyYAML (Config Management)
* GitHub Actions (CI/CD)

---

✨ Features

* Page Object Model (POM) design pattern
* UI Automation using Selenium
* API Automation using Requests
* Data-driven testing using JSON
* Config-driven framework (YAML)
* Cross-browser ready structure
* Parallel test execution (pytest-xdist)
* CI/CD integration with GitHub Actions

---

 📁 Project Structure

```
qa-automation-project/
│
├── tests/
│   ├── ui/
│   ├── api/
│
├── pages/
├── api/
├── utils/
├── config/
├── test_data/
├── reports/
├── .github/workflows/
│
├── conftest.py
├── requirements.txt
├── pytest.ini
└── README.md
```

---

 ▶️ How to Run Tests

 Step 1: Create Virtual Environment

```
python -m venv venv
```

Step 2: Activate Environment

```
venv\Scripts\activate
```

 Step 3: Install Dependencies

```
pip install -r requirements.txt
```
 Step 4: Run Tests

```
pytest
```

---

⚡ Run Tests in Parallel

```
pytest -n 2
```

---

📊 Generate Allure Report

```
pytest --alluredir=reports
allure serve reports
```

---

 🌐 Test Applications

* https://www.saucedemo.com/
* https://reqres.in/

---

 🔄 CI/CD Integration

* Automated test execution using GitHub Actions
* Runs tests automatically on every push

---

