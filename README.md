# Fleapo
# Fanfix Automation Testing

This project contains automation scripts for testing the Fanfix website using Selenium WebDriver with Python. The tests follow the Page Object Model (POM) design pattern and are organized using the pytest framework.


## Setup Instructions

### Prerequisites

- Python 3.x
- Selenium WebDriver
- Firefox Browser and GeckoDriver

### Installing Dependencies

1. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Tests

1. Ensure GeckoDriver is in your PATH or in the project directory.

2. Run the tests using pytest:
    ```bash
    pytest
    ```
## Test Cases

Test cases are defined in `Fanfix_Test_Cases.xlsx`. The Excel file contains detailed descriptions, steps to execute, expected results, severity, and priority for each test case.

### Example Test Case

**Test Case ID:** TC_001
**Description:** Verify login functionality with valid credentials
**Steps to Execute:**
1. Navigate to the login page
2. Enter valid email and password
3. Click on login button
**Expected Result:** User should be logged in and redirected to the home page
**Severity:** Critical
**Priority:** High

## Adding New Tests

1. Create a new Python file in the `tests` directory or add a new function to the existing `test_fanfix.py` file.
2. Follow the pytest conventions for writing test cases.
3. Use the POM classes to interact with the web elements.

### Example

```python
from pages.login_page import LoginPage
from pages.new_post_page import NewPostPage
from utils.driver_setup import get_driver

def test_create_new_post():
    driver = get_driver()
    login_page = LoginPage(driver)
    new_post_page = NewPostPage(driver)
    
    login_page.login('testqa@mailinator.com', '123456789')
    new_post_page.create_post('This post is done by automation assignment', '/path/to/image.jpg', 5)
    
    assert new_post_page.is_post_created('This post is done by automation assignment')
    driver.quit()


