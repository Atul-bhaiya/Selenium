from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time



#Task 1
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver,10)
driver.get("https://demoqa.com/upload-download")
driver.maximize_window()
file_path = "C:\\Users\\Atul\\OneDrive\\Desktop\\Hii.txt.txt"
upload_input = driver.find_element(By.ID, "uploadFile")
upload_input.send_keys(file_path)
uploaded_file = driver.find_element(By.ID, "uploadedFilePath")
print("✅ Upload Confirmation:", uploaded_file.text)
time.sleep(2)
driver.quit()
