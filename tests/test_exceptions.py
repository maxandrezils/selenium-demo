import pytest
from selenium.webdriver.common.by import By


class TestExceptions:
    def test_no_such_element_exception(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        add_button_locator = driver.find_element_by_id(By.ID, "add_btn")
        second_row_locator = driver.find_element(
            By.CSS_SELECTOR, "div:nth-of-type(3) > .row > .input-field"
        )
        assert second_row_locator.is_displayed(), "Second row is not displayed."
