from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
time.sleep(2)
input_username = driver.find_element(By.XPATH , "//input[@name='user-name']")
input_username.send_keys("standard_user")
time.sleep(1)

input_password = driver.find_element(By.XPATH , "//input[@name = 'password']")
input_password.send_keys("secret_sauce")
login_btn = driver.find_element(By.XPATH , "//input[@name = 'login-button']")
time.sleep(1)


login_btn.click()
time.sleep(1)


