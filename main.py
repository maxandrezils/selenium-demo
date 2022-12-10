import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# 1. Navigate to the test site
driver.get("https://practicetestautomation.com/practice-test-login/")
# 2. Enter the username
username_locator = driver.find_element(By.XPATH, "/html//input[@id='username']")
username_locator.send_keys("student")

# 3. Enter the password
password_locator = driver.find_element(By.XPATH, "/html//input[@id='password']")
password_locator.send_keys("Password123")

# 4. Click the submit button
submit_button_locator = driver.find_element(By.XPATH, "/html//button[@id='submit']")
submit_button_locator.click()
time.sleep(3)

# 5. Confirm that the url is
actual_url = driver.current_url
assert (
    actual_url
    == "https://practicetestautomation.com/practice-test/logged-in-successfully"
)

# 6. Confirm that the text is
text_locator = driver.find_element(By.TAG_NAME, "h1")
actual_text = text_locator.text
assert actual_text == "Logged In Successfully"
log_out_button_locator = driver.find_element(By.LINK_TEXT, "Log out")
assert log_out_button_locator.is_displayed()
