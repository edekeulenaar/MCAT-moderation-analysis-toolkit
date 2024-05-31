import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
import csv

# Function to log in to TikTok
def login_to_tiktok(driver, username, password):
    driver.get("https://www.tiktok.com/login/phone-or-email/email")
    time.sleep(5)  # Allow time for the page to load

    # Enter username
    try:
        username_input = driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[1]/input')
        username_input.send_keys(username)
    except Exception as e:
        print(f"Error entering username: {e}")
        return False

    # Enter password
    try:
        password_input = driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[2]/div/input')
        password_input.send_keys(password)
    except Exception as e:
        print(f"Error entering password: {e}")
        return False

    # Click on the login button
    try:
        login_button = driver.find_element(By.XPATH, "//button[@data-e2e='login-button']")
        login_button.click()
        time.sleep(5)  # Allow time for the login to process
        
        # Pause to solve CAPTCHA manually
        input("Please solve the CAPTCHA manually and press Enter to continue...")

        return True
    except Exception as e:
        print(f"Error clicking login button: {e}")
        return False

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
    # chrome_options.add_argument("--headless")  # Run headless Chrome to not open a window
    driver = webdriver.Chrome(options=chrome_options)

    # Log in to TikTok
    login_successful = login_to_tiktok(driver, username, password)
    if not login_successful:
        print("Login failed. Exiting.")
        driver.quit()
        return

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
    keywords = ["stopthesteal", "fromtherivertothesea", "cats"]  # Replace with your list of keywords
    output_file = 'output.csv'

    # TikTok login credentials
    username = 'dominiquepierdet@gmail.com'  # Replace with your TikTok username
    password = '497254jhkd^*0'  # Replace with your TikTok password

    process_keywords(keywords, output_file, username, password)
    print(f"Scraping complete. Results saved to {output_file}")
