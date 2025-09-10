# Selenium Automation Tasks

This repository contains five Selenium automation tasks demonstrating browser interaction, element handling, and basic web scraping.

---

## Task Overview

### 1. Google Search Screenshot (`task1.py`)
- **Purpose:** Searches for a name on Google and saves a screenshot of the results.
- **How it works:**
  - Opens Google, accepts cookies if prompted.
  - Types `"Sten Kahu"` into the search box and presses Enter.
  - Waits for results and saves a screenshot (`found.png`).

### 2. Quotes Scraper (`task2.py`)
- **Purpose:** Scrapes quotes and authors from the first page of [Quotes to Scrape](https://quotes.toscrape.com/).
- **How it works:**
  - Finds all quotes (`span.text`) and authors (`small.author`).
  - Prints each quote-author pair to the console.

### 3. Add/Remove Elements (`task3.py`)
- **Purpose:** Automates adding and removing elements on [Add/Remove Elements](https://the-internet.herokuapp.com/add_remove_elements/).
- **How it works:**
  - Clicks the "Add Element" button 5 times.
  - Clicks each "Delete" button to remove added elements.

### 4. Login Automation (`task4.py`)
- **Purpose:** Automates login on [Login Page](https://the-internet.herokuapp.com/login) and prints the result message.
- **How it works:**
  - Enters credentials (`tomsmith / SuperSecretPassword!`).
  - Clicks "Login" and prints the flash message.

### 5. Checkbox Automation (`task5.py`)
- **Purpose:** Checks all checkboxes on the [Checkboxes page](https://the-internet.herokuapp.com/checkboxes).
- **How it works:**
  - Navigates to the page.
  - Checks any unchecked boxes.
  - Returns to the homepage.

---

## Key Concepts Demonstrated
- Locating elements (`find_element`, `find_elements`)
- Clicking buttons and links
- Typing into input fields
- Form submission
- Checking element state (`is_selected`)
- Waiting for elements (`time.sleep` or `WebDriverWait`)
- Taking screenshots (`save_screenshot`)
- Browser navigation (`driver.back`)

---

## Setup
1. Install required packages:
```bash
pip install selenium webdriver-manager
```
2. Make sure Google Chrome is installed.
3. Run any task using Python:
```bash
python task[1-5].py
```