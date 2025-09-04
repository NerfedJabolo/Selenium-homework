from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://quotes.toscrape.com/")

quotes = driver.find_elements("class name", "text")
authors = driver.find_elements("class name", "author")
for quote, author in zip(quotes, authors):
    print(f"{quote.text} - {author.text}")

driver.quit()