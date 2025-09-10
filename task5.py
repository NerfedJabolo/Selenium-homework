from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Configure Chrome options
options = Options()
# Keep the browser window open after script ends (detach = True)
options.add_experimental_option("detach", True)

# Launch Chrome with the given options
driver = webdriver.Chrome(options=options)

# Open the test site's homepage
driver.get("https://the-internet.herokuapp.com")

# Navigate to the "Checkboxes" page by clicking the link
driver.find_element("link text", "Checkboxes").click()

# Find all checkboxes inside the div with id="checkboxes"
checkboxes = driver.find_elements("xpath", '//*[@id="checkboxes"]/input')

# Loop through each checkbox
for checkbox in checkboxes:
    # If the checkbox is not already checked, click it
    if not checkbox.is_selected():
        checkbox.click()

# Pause so you can visually confirm that both checkboxes are selected
time.sleep(5)

# Navigate back to the homepage
driver.back()
