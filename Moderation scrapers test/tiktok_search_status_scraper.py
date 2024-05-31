import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
import csv

# Function to log in to TikTok
def login_to_tiktok(driver, username, password):
    driver.get("https://www.tiktok.com/login")
    time.sleep(3)  # Allow time for the page to load

    # Assuming login by username and password
    login_method_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Use phone / email / username')]")
    login_method_button.click()
    time.sleep(2)

    # Selecting the "Log in with email/username" option
    login_with_username = driver.find_element(By.XPATH, "//div[contains(text(), 'Use phone / email / username')]")
    login_with_username.click()
    time.sleep(2)

    # Enter username
    username_input = driver.find_element(By.NAME, 'email')
    username_input.send_keys(username)

    # Enter password
    password_input = driver.find_element(By.NAME, 'password')
    password_input.send_keys(password)

    # Click on the login button
    login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Log in')]")
    login_button.click()
    time.sleep(5)  # Allow time for the login to process

# Function to scrape the URL
def scrape_url(url, driver):
    driver.get(url)
    time.sleep(3)  # Allow time for the page to load

    try:
        # Check for css-6ffk2r-DivGuideReminderContent class
        elements = driver.find_elements(By.CLASS_NAME, 'css-6ffk2r-DivGuideReminderContent')
        if elements:
            texts = [element.text for element in elements]
            return ' '.join(texts)

        # Check for search-error-title and search-error-desc classes
        title_elements = driver.find_elements(By.CLASS_NAME, 'search-error-title')
        desc_elements = driver.find_elements(By.CLASS_NAME, 'search-error-desc')
        if title_elements or desc_elements:
            texts = [element.text for element in title_elements + desc_elements]
            return ' '.join(texts)

        # If neither class is found
        return "Normal"
    except Exception as e:
        return f"Error: {e}"

# Function to process keywords and write results to CSV
def process_keywords(keywords, output_file, username, password):
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Setting up the Chrome driver
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run headless Chrome to not open a window
    driver = webdriver.Chrome(options=chrome_options)

    # Log in to TikTok
    login_to_tiktok(driver, username, password)

    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['URL', 'Date', 'Status', 'Driver'])

        for keyword in keywords:
            url = f"https://www.tiktok.com/search?q=%23{keyword}"
            status = scrape_url(url, driver)
            writer.writerow([url, current_date, status, 'Chrome'])
            print(f"Processed URL: {url}, Status: {status}")

    driver.quit()

if __name__ == "__main__":
    # List of keywords to append to the URL
    keywords = ["stopthesteal", "fromtherivertothesea", "freetaiwan"]  # Replace with your list of keywords
    output_file = 'output.csv'

    # TikTok login credentials
    username = 'dominiquepierdet@gmail.com' # Replace with your TikTok username
    password = '497254jhkd^*0'  # Replace with your TikTok password

    process_keywords(keywords, output_file, username, password)
    print(f"Scraping complete. Results saved to {output_file}")
