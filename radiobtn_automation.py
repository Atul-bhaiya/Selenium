from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://dmytro-ch21.github.io/html/web-elements.html")
time.sleep(1)
driver.maximize_window()
time.sleep(1)
radiobtn = driver.find_elements(By.XPATH, "//input[@type ='radio']")
for radio in radiobtn:
    if not radio.is_selected():
        radio.click()
        time.sleep(1)







