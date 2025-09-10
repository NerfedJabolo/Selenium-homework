from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Configure Chrome options
options = Options()
# Keep the browser open after script finishes (detach = True)
options.add_experimental_option("detach", True)

# Launch Chrome with the given options
driver = webdriver.Chrome(options=options)

# Open the test page
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

# Locate the "Add Element" button
add_button = driver.find_element("xpath", '//*[@id="content"]/div/button')

# Click the "Add Element" button 5 times, with a short delay each time
for _ in range(5):
    add_button.click()
    time.sleep(1)

# Locate all "Delete" buttons that were created
remove_buttons = driver.find_elements("xpath", '//*[@id="elements"]/button')

# Click each "Delete" button one by one, with a short delay
for button in remove_buttons:
    button.click()
    time.sleep(1)

# (Optional) Close the browser after the task is done
driver.quit()