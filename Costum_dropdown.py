from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://dmytro-ch21.github.io/html/web-elements.html")
time.sleep(1)
driver.maximize_window()
time.sleep(1)

dropdown = driver.find_element(By.ID , "custom-select")
dropdown.click()
time.sleep(3)
select_color = driver.find_element(By.CLASS_NAME , "option")
select_color.click()
time.sleep(5)