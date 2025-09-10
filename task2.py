from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configure Chrome options
options = Options()
# Keep the browser open after script finishes (detach = True)
options.add_experimental_option("detach", True)

# Launch Chrome with the given options
driver = webdriver.Chrome(options=options)

# Open the target website
driver.get("https://quotes.toscrape.com/")

# Find all elements that contain quotes (span elements with class="text")
quotes = driver.find_elements("class name", "text")

# Find all elements that contain authors (small elements with class="author")
authors = driver.find_elements("class name", "author")

# Loop through quotes and authors simultaneously and print them
for quote, author in zip(quotes, authors):
    print(f"{quote.text} - {author.text}")

# Close the browser once finished
driver.quit()
