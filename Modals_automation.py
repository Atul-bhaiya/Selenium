import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Start the Chrome browser
driver = webdriver.Chrome()

# 2. Open the website
driver.get("https://demoqa.com/modal-dialogs")
driver.maximize_window()  # Makes the window full screen

# 3. Click the "Small Modal" button
small_modal_button = driver.find_element(By.ID, "showSmallModal")
small_modal_button.click()

# 4. Wait for the modal to appear (better than fixed sleep)
time.sleep(1)  # Simple wait (not the best, but okay for learning)

# 5. Get the text inside the modal (correct way)
modal_text = driver.find_element(By.CLASS_NAME, "modal-body").text
print("Modal text:", modal_text)  # Prints the actual modal content

# 6. Click the "Close" button inside the modal
close_button = driver.find_element(By.ID, "closeSmallModal")
close_button.click()

# 7. Wait to see the result before closing
time.sleep(3)

# 8. Close the browser
driver.quit()
