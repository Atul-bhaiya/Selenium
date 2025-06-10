from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/alerts")

# 1. Simple Alert
driver.find_element(By.ID, "alertButton").click()
alert = driver.switch_to.alert
print("Simple Alert Text:", alert.text)
alert.accept()
time.sleep(1)

# 2. Timer Alert
driver.find_element(By.ID, "timerAlertButton").click()
WebDriverWait(driver, 10).until(EC.alert_is_present())
alert = driver.switch_to.alert
print("Timer Alert Text:", alert.text)
alert.accept()
time.sleep(1)

# 3. Confirmation Alert
driver.find_element(By.ID, "confirmButton").click()
alert = driver.switch_to.alert
print("Confirmation Alert Text:", alert.text)
alert.dismiss()
result = driver.find_element(By.ID, "confirmResult").text
print("Confirmation Result:", result)
time.sleep(1)

# 4. Prompt Alert
driver.find_element(By.ID, "promtButton").click()
alert = driver.switch_to.alert
print("Prompt Alert Text:", alert.text)
alert.send_keys("Atul bhaiya")
alert.accept()
result = driver.find_element(By.ID, "promptResult").text
print("Prompt Result:", result)

time.sleep(2)
driver.quit()


