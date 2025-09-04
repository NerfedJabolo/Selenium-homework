from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://the-internet.herokuapp.com/login")

# Fill in the login form and submit
username_input = driver.find_element("id", "username")
password_input = driver.find_element("id", "password")
username_input.send_keys("tomsmith")
password_input.send_keys("SuperSecretPassword!")
driver.find_element("xpath", '//*[@id="login"]/button').click()
# if login is successful, print the success message
time.sleep(5)  # Wait for the page to load
success_message = driver.find_element("id", "flash").text
print(success_message)