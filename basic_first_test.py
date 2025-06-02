from selenium import webdriver
import time



driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")
driver.refresh()
driver.get("https://www.youtube.com/")
time.sleep(1)
driver.back()
driver.quit()