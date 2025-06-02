from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
#driver.get("https://googled.com")
driver.get("https://www.saucedemo.com/")
input_Username = driver.find_element(By.NAME , "user-name")
password_input = driver.find_element(By.NAME, "password")  # Change 'password' as needed
input_Username.send_keys("standard_user")
time.sleep(2)
password_input.send_keys("secret_sauce")
time.sleep(2)
Login_button= driver.find_element(By.NAME , "login-button")
Login_button.click()


#driver.get("https://chatgpt.com")
time.sleep(2)
driver.quit()