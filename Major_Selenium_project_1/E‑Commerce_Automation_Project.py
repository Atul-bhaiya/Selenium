
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import time


#Launch Browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.automationexercise.com/")
wait = WebDriverWait(driver,10)
products_page = driver.find_element(By.XPATH, "//a[@href='/products']")
products_page.click()
Search_product = driver.find_element(By.ID , "search_product")
Search_product.click()
Search_product.send_keys("Tshirt")
Search_product.send_keys(Keys.ENTER)
View_product = driver.find_element(By.XPATH, "//a[@href='/product_details/2']")
driver.execute_script("arguments[0].scrollIntoView(true);", View_product)
time.sleep(1)


View_product.click()
driver.save_screenshot("file.png")
Add_Cart = wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-default cart']")))
Add_Cart.click()

time.sleep(1)
driver.save_screenshot("file.png")
View_Cart = wait.until(ec.element_to_be_clickable((By.LINK_TEXT , "View Cart")))
View_Cart.click()
#driver.save_screenshot("file.png2")
quantity_inputs = driver.find_elements(By.XPATH, "//input[@name='quantity']")
if quantity_inputs:
    quantity_inputs[0].clear()
    quantity_inputs[0].send_keys("2")

driver.save_screenshot("quantity_updated.png")

delete_btn = wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "cart_quantity_delete")))
delete_btn.click()
time.sleep(2)
driver.save_screenshot("cart_after_delete.png")

# Step 8: Close the browser



time.sleep(4)
driver.quit()