from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

add_button = driver.find_element("xpath", '//*[@id="content"]/div/button')
for _ in range(5):
    add_button.click()
    time.sleep(1)

remove_buttons = driver.find_elements("xpath", '//*[@id="elements"]/button')
for button in remove_buttons:
    button.click()
    time.sleep(1)