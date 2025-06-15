from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://duckduckgo.com/")
search_btn = driver.find_element(By.XPATH , "//input[@id = 'searchbox_input']")
search_btn.click()
search_btn.send_keys("chat GPT")
search_btn.submit()
wait = WebDriverWait(driver, 10)

results = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[@data-testid='result-title-a']")))

print("Result 1:", results[0].get_attribute('href'))
print("Result 2:", results[1].get_attribute('href'))
print("Result 3:", results[2].get_attribute('href'))
time.sleep(4)