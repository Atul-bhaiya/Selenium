from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://dmytro-ch21.github.io/html/web-elements.html")
time.sleep(1)
driver.maximize_window()
time.sleep(1)

# Locate the dropdown element
dropdown = driver.find_element(By.ID, "carBrands")
select = Select(dropdown)

# Get all available options
all_options = select.options

# Loop through each option and select it
for option in all_options:
    # Get the value attribute of the option
    option_value = option.get_attribute("value")

    # Skip the default/placeholder option if it exists
    if option_value == "":
        continue

    # Select the option by its value
    select.select_by_value(option_value)

    # Print which option was selected
    print(f"Selected: {option.text} (Value: {option_value})")

    time.sleep(1)

driver.quit()



