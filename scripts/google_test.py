import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Ensure screenshots directory exists
os.makedirs("screenshots", exist_ok=True)

# Set up Chrome in headless mode
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    # Visit Google
    driver.get("https://www.google.com")

    # Find the search box and type text
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Hello from Selenium!")
    search_box.send_keys(Keys.RETURN)

    # Take screenshot
    driver.save_screenshot("screenshots/google.png")

finally:
    driver.quit()
