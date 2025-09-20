This repository contains an end-to-end automation testing framework built using Python, Selenium, and Pytest.
It follows a Page Object Model (POM) design pattern, ensuring scalability, maintainability, and reusability of test scripts.

📂 Project Structure
PythonSelenium/
│── .venv/                  # Virtual environment (ignored in repo)
│
├── Data/                   # Test data files
│   └── test_e2eTestFramework.json
│
├── E2ETest/                # End-to-End test cases
│   ├── Reports/            # Pytest reports storage
│   ├── conftest.py         # Pytest fixtures & configurations
│   ├── e2eTestDemo.py      # Sample end-to-end test
│   ├── test_e2eTestFramework.py
│   └── test_sortTable.py
│
├── PageObject/             # Page Object Model (POM) classes
│   ├── checkout.py
│   ├── login.py
│   └── shop.py
│
├── Utils/                  # Utility functions & helpers
│   ├── browserUtils.py
│
├── .gitignore              # Git ignore file

🚀 Features
✅ Built on Pytest (lightweight & powerful test runner)
✅ Implements Page Object Model (POM) for test maintainability
✅ Supports Data-Driven Testing (JSON/Excel)
✅ Generates HTML Reports for test execution results
✅ Custom utilities & wrappers for browser handling
✅ Modular and reusable test design

📌 Best Practices Followed
✅Page Object Model (POM) for better test maintainability
✅Fixtures in conftest.py for setup & teardown
✅Data-driven approach using JSON & Excel files
✅Separation of concerns: Tests, PageObjects, Data, and Reports
✅Parallel execution with pytest-xdist
✅Integration with CI/CD pipelines (Jenkins/GitHub Actions)
✅Cross-browser execution (Chrome, Firefox, Edge, etc.)

🔗 Connect with Me
If you find this framework useful or would like to collaborate, feel free to connect with me on www.linkedin.com/in/shanmugammv
