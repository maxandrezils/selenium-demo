import time
from pytest import mark, param
import pytest
from selenium.webdriver.common.by import By


@mark.login
@mark.negative
class TestNegativeScenarios:
    def setup(self):
        self.wait_time = 2

    @mark.parametrize(
        ("username", "password", "expected_error_message"),
        [
            pytest.param(
                "incorrectUsername",
                "Password123",
                "Your username is invalid!",
                id="incorrectUsername",
            ),
            pytest.param(
                "student",
                "Password",
                "Your password is invalid!",
                id="incorrectPassword",
            ),
        ],
    )
    def test_negative_username(
        self, driver, username, password, expected_error_message
    ):
        """
        It navigates to the test site, enters the username and password, clicks the submit button, and
        then confirms that the error message is displayed
        """
        # 1. Navigate to the test site
        driver.get("https://practicetestautomation.com/practice-test-login")
        # 2. Enter the username
        username_locator = driver.find_element(By.XPATH, "/html//input[@id='username']")
        username_locator.send_keys(username)
        # 3. Enter the password
        password_locator = driver.find_element(By.XPATH, "/html//input[@id='password']")
        password_locator.send_keys(password)
        # 4. Click the submit button
        submit_button_locator = driver.find_element(
            By.XPATH, "/html//button[@id='submit']"
        )
        submit_button_locator.click()
        time.sleep(self.wait_time)
        # 5. Confirm that the error message is displayed.
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error message is not displayed."
        assert (
            error_message_locator.text == expected_error_message
        ), "Error message is not correct."
