import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import shutil
from datetime import datetime
from bs4 import BeautifulSoup
import os

def detect_delimiter(file_path):
    """Detect the delimiter of a CSV file."""
    with open(file_path, 'r') as file:
        first_line = file.readline()
        if '\t' in first_line:
            return '\t'
        elif ',' in first_line:
            return ','
        elif ';' in first_line:
            return ';'
        else:
            return ','  # Default to comma

def process_file(src_path, dest_path):
    print(f"Processing file: {src_path}")
    # Detect delimiter
    delimiter = detect_delimiter(src_path)
    print(f"Detected delimiter: {delimiter}")

    # Copy the file
    shutil.copy(src_path, dest_path)

    # Load the data with the detected delimiter
    try:
        df = pd.read_csv(dest_path, delimiter=delimiter)
        if 'URL' not in df.columns:
            raise KeyError("Column 'URL' not found in the CSV file.")
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return

    # Add columns for 'Status', 'Date scraped', and 'driver' if they don't exist
    if 'Status' not in df.columns:
        df['Status'] = ''
    if 'Date scraped' not in df.columns:
        df['Date scraped'] = ''
    if 'driver' not in df.columns:
        df['driver'] = ''

    def check_class_on_page(driver, url, class_name):
        try:
            driver.get(url)
            try:
                elements = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, class_name))
                )
                texts = []
                for element in elements:
                    inner_html = element.get_attribute('innerHTML')
                    soup = BeautifulSoup(inner_html, 'html.parser')
                    text = ' '.join(soup.stripped_strings)  # Extract all natural language text
                    texts.append(text)
                return ' '.join(texts) if texts else "Online"
            except Exception as e:
                return f"Online"
        except Exception as e:
            return str(e)

    # Set up the WebDriver (assuming using Chrome)
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run headless Chrome to not open a window
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver_path = 'path/to/your/chromedriver'  # Specify the path to your ChromeDriver
    service = Service(driver_path)

    current_date = datetime.now().strftime("%Y-%m-%d")

    print('Running... 🏃')

    # Function to process each row
    def process_row(index, row):
        driver = webdriver.Chrome(options=chrome_options)
        try:
            url = row['URL']
            result = check_class_on_page(driver, url, '.xzueoph.x1k70j0n')
            df.at[index, 'Status'] = result
            df.at[index, 'Date scraped'] = current_date
            df.at[index, 'driver'] = 'Chrome'
            print(f"Processed URL: {url}, Result: {result}")  # Debugging statement to ensure processing
        finally:
            driver.quit()

    print("I don't know where I'm runnin' now, I'm just runnin' on")
    print("runnin' on empty")
    print("Runnin' on, runnin' into the sun")
    print("But I'm runnin' behind")

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(process_row, index, row) for index, row in df.iterrows()]
        for future in as_completed(futures):
            future.result()  # to raise any exceptions

    # Save the updated DataFrame to the CSV file
    df.to_csv(dest_path, index=False, sep=delimiter)
    print(f"Processing complete. Results saved to {dest_path}")

def process_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            src_path = os.path.join(folder_path, filename)
            dest_path = src_path.replace(".csv", "_copy.csv")
            print(f"Processing file: {src_path}")
            process_file(src_path, dest_path)

def main():
    # Specify the mode and path directly in the script
    mode = 'file'  # Write 'folder' if you're processing a folder or 'file' if you're processing a file. 
    path = 'path/to/your/file/or/folder'  # Update this to your specific file or folder path. On MacOS, select a file or folder in the Finder and press the option-key while right-clicking and choose Copy "selected item" as pathname.

    if mode == 'file':
        src_path = path
        dest_path = src_path.replace(".csv", "_copy.csv")
        process_file(src_path, dest_path)
    elif mode == 'folder':
        process_folder(path)
    else:
        print("Invalid mode. Please set 'mode' to 'file' or 'folder'.")

if __name__ == "__main__":
    main()
