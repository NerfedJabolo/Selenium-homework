from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# set up Chrome
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 20)

try:
    # open Google
    driver.get("https://www.google.com/")

    # accept cookies if asked
    try:
        consent_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="W0wltc"]/div')))
        consent_btn.click()
    except:
        pass  # no consent popup

    # find the search box
    searchbox = wait.until(EC.element_to_be_clickable((By.XPATH, '//textarea[@name="q"]')))
    searchbox.send_keys("Sten Kahu")
    searchbox.send_keys(Keys.RETURN)  # press Enter

    # wait for results
    wait.until(EC.presence_of_element_located((By.ID, "search")))
    time.sleep(2)

    # save screenshot
    driver.save_screenshot("./screenshots/found.png")

finally:
    driver.quit()
