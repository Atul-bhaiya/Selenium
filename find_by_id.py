from selenium import webdriver
from selenium.webdriver.common.by import By  # ✅ You need to import 'By'

import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
time.sleep(3)
driver.get("https://www.saucedemo.com/")
username_input = driver.find_element(By.ID , "user-name")
username_input.send_keys("standard_user")

password = driver.find_element(By.ID , "password")
password.send_keys("secret_sauce")

Login_button = driver.find_element(By.ID , "login-button")
Login_button.click()
time.sleep(4)
