import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestExceptions:
    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()
        wait = WebDriverWait(driver, 10)
        row_2_input_element = wait.until(
            ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input"))
        )
        # Verify Row 2 input field is displayed
        assert (
            row_2_input_element.is_displayed()
        ), "Row 2 input should be displayed, but it's not"

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_element_not_interacterable_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()
        wait = WebDriverWait(driver, 10)
        row_2_input_element = wait.until(
            ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input"))
        )
        row_2_input_element.send_keys("Sushi")
        driver.find_element(By.NAME, "Save").click()
        confirmation_element = driver.find_element(By.ID, "confirmation")
        assert (
            confirmation_element.text == "Row 2 was saved"
        ), "Confirmation message is incorrect"
