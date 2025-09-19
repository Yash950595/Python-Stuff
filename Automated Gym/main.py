from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

URL = "https://appbrewery.github.io/gym/"
email = "yashpatil0710@gmail.com"
password = "yash_007"
name = "Yash"

chrome = webdriver.ChromeOptions()
chrome.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome)
driver.get(URL)

wait = WebDriverWait(driver, 10)

login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]')))
login_button.click()

fill_email = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="email-input"]')))
fill_email.clear()
fill_email.send_keys(email)

fill_password = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="password-input"]')))
fill_password.clear()
fill_password.send_keys(password)

click_submit = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submit-button"]')))
click_submit.click()

# Check if login failed:
try:
    user_not_found = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="error-message"]')))
    if user_not_found.is_displayed():
        print("User not found, switching to registration...")

        account_register = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="toggle-login-register"]')))
        account_register.click()

        insert_name = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="name-input"]')))
        insert_name.clear()
        insert_name.send_keys(name)

        insert_email = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="email-input"]')))
        insert_email.clear()
        insert_email.send_keys(email)

        insert_password = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="password-input"]')))
        insert_password.clear()
        insert_password.send_keys(password)
except TimeoutException:
    print("Login successful, no error message found.")

register_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submit-button"]')))
register_button.click()

schedule=wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="schedule-page"]')))

driver.quit()
