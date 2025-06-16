from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practicetestautomation.com/practice-test-login/")
wait = WebDriverWait(driver , 10)
Input_Username = driver.find_element(By.ID , "username")
Input_Username.click()
Input_Username.send_keys("student")
time.sleep(1)

Input_Password = driver.find_element(By.ID , "password")
Input_Password.click()
Input_Password.send_keys("Password123")
time.sleep(1)

Submit_Btn = driver.find_element(By.ID , "submit")
Submit_Btn.click()
time.sleep(2)

#Login done lets Logout

Logout = driver.find_element(By.LINK_TEXT, "Log out")
Logout.click()
print("Logout suceessfull ")
time.sleep(3)

driver.quit()


