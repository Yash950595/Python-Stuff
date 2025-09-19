from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome=webdriver.ChromeOptions()
chrome.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name=driver.find_element(By.XPATH,value="//input[contains(@class,'form-control') and contains(@class,'top')]")
first_name.send_keys("Yash",Keys.ENTER)

last_name=driver.find_element(By.XPATH,value="//input[contains(@class,'form-control') and contains(@class,'middle')]")
last_name.send_keys("Patil",Keys.ENTER)

email=driver.find_element(By.XPATH,value="//input[contains(@class,'form-control') and contains(@class,'bottom')]")
email.send_keys("yashpatil0710@gmail.com",Keys.ENTER)

signup_button=driver.find_element(By.XPATH,value="//button[text()='Sign Up']")
signup_button.click()

driver.quit()
