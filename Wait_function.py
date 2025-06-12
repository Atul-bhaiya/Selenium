import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://demoqa.com/alerts")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# ✅ Wait for the alert button to be clickable and click it
alert_btn = wait.until(EC.element_to_be_clickable((By.ID, "alertButton")))
alert_btn.click()

# ✅ Switch to alert and accept it
alert = driver.switch_to.alert
alert.accept()

# ✅ Optional: wait and close the browser
time.sleep(5)
driver.quit()

