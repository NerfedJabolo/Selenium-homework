from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Configure Chrome options
options = Options()
# Keep the browser open after the script finishes (detach = True)
options.add_experimental_option("detach", True)

# Launch Chrome with the given options
driver = webdriver.Chrome(options=options)

# Open the login page
driver.get("https://the-internet.herokuapp.com/login")

# Locate username and password input fields
username_input = driver.find_element("id", "username")
password_input = driver.find_element("id", "password")

# Enter login credentials
username_input.send_keys("tomsmith")
password_input.send_keys("SuperSecretPassword!")

# Locate and click the "Login" button
driver.find_element("xpath", '//*[@id="login"]/button').click()

# Wait for the next page to load (simple sleep here, could be replaced with WebDriverWait)
time.sleep(5)

# Find and print the login success (or failure) message
success_message = driver.find_element("id", "flash").text
print(success_message)
