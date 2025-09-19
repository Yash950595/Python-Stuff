from selenium import webdriver
import os
from selenium.webdriver.common.by import By

URL="https://appbrewery.github.io/gym/"
chrome=webdriver.ChromeOptions()
chrome.add_experimental_option("detach",True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome.add_argument(f"--user-data-dir={user_data_dir}")

driver=webdriver.Chrome(options=chrome)
driver.get(URL)

login=driver.find_element(By.XPATH,value='//*[@id="login-button"]')
login.click()









driver.quit()