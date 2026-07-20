# Software Quality Engineering Project

A complete Software Quality Engineering project demonstrating **Manual Testing**, **UI Automation**, **API Testing**, and **Continuous Integration/Continuous Deployment (CI/CD)**.

---

## Project Description

This project automates testing of the SauceDemo web application and REST APIs using industry-standard testing tools. The test suites are automatically executed through GitHub Actions whenever changes are pushed to the repository.

---

## Technologies Used

- Python
- Selenium WebDriver
- Pytest
- Cypress
- Postman
- Newman
- GitHub Actions
- Chrome Browser

---

## Project Modules

### Selenium Automation
Automated UI testing using Selenium WebDriver and the Page Object Model (POM).

### Cypress Automation
End-to-end web application testing using Cypress.

### API Testing
REST API testing using Postman Collections executed with Newman.

### CI/CD
Automated test execution using GitHub Actions.

---

## Features Tested

### Selenium
- Browser Launch
- Login
- Inventory Page
- Cart
- Checkout
- Logout

### Cypress
- UI Functional Testing
- End-to-End User Flow

### API Testing
- GET All Posts
- GET Single Post
- POST Create Resource
- PUT Update Resource
- DELETE Resource

---

## Project Structure

```
software-quality-engineering-project/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── selenium_automation/
│   ├── pages/
│   ├── tests/
│   ├── utils/
│   ├── requirements.txt
│   └── pytest.ini
│
├── cypress_automation/
│   ├── cypress/
│   ├── cypress.config.js
│   └── package.json
│
├── api_testing/
│   └── Software Quality Engineering API Tests.postman_collection.json
│
└── manual_testing/
```

---

## Running Selenium Tests

```bash
cd selenium_automation

pip install -r requirements.txt

pytest
```

---

## Running Cypress Tests

```bash
cd cypress_automation

npm install

npx cypress run
```

---

## Running API Tests

Install Newman:

```bash
npm install -g newman
```

Run the Postman collection:

```bash
newman run "api_testing/Software Quality Engineering API Tests.postman_collection.json"
```

---

## CI/CD Pipeline

GitHub Actions automatically performs:

- Selenium Automation Tests
- Cypress Automation Tests
- Postman API Tests using Newman

The workflow is triggered on:

- Push to the `main` branch
- Pull Requests to the `main` branch

---

## Repository Highlights

- Selenium Page Object Model (POM)
- Pytest Framework
- Cypress End-to-End Testing
- Postman API Testing
- Newman CLI Integration
- GitHub Actions CI/CD
- Cross-platform automated testing

---

## Author

**Sudeep Bhattarai**

Software Quality Engineering Project