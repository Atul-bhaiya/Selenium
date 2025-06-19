import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver , 10)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
heading = driver.find_element(By.ID , "tinymce").text
#print("Heading : ",heading)
textarea = driver.find_element(By.ID , "tinymce")
textarea.send_keys(Keys.CONTROL + "a") #select all
textarea.send_keys(Keys.BACKSPACE) #delete all text
textarea.send_keys("Automation testing by Atul bhaiya ")
driver.switch_to.default_content()
time.sleep(2)
driver.quit()
