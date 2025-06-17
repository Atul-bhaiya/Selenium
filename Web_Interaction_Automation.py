from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


#Task 1
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver,10)
driver.get("https://demoqa.com/modal-dialogs")
modal_Btn = driver.find_element(By.ID , "showSmallModal")
driver.execute_script("arguments[0].scrollIntoView();", modal_Btn)

modal_Btn.click()
modal_body = driver.find_element(By.CLASS_NAME,"modal-body")
print("Modal Text : ", modal_body.text)
modal_body_close = driver.find_element(By.ID , "closeSmallModal")
time.sleep(2)

driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_alert")
driver.maximize_window()
driver.switch_to.frame("iframeResult")
iframe = driver.find_element(By.TAG_NAME , "button")
iframe.click()

time.sleep(2)
alert = driver.switch_to.alert
print("🚨 Alert Text:", alert.text)
alert.accept()
driver.switch_to.default_content()
time.sleep(3)
driver.quit()


