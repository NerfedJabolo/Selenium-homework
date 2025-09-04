from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://the-internet.herokuapp.com")

# navigate to "checkboxes" page, check both checkboxes if not already checked, navigate back to home page
driver.find_element("link text", "Checkboxes").click()
checkboxes = driver.find_elements("xpath", '//*[@id="checkboxes"]/input')
for checkbox in checkboxes:
    if not checkbox.is_selected():
        checkbox.click()
time.sleep(5)  # Optional: wait a bit to see the checkboxes being checked
driver.back()