import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
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
        if 'link' not in df.columns:
            raise KeyError("Column 'link' not found in the CSV file.")
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

    # Function to check class on a page
    def check_class_on_page(url, class_name):
        # Set up the WebDriver (assuming using Chrome)
        chrome_options = Options()
        # Comment out the headless option to see the browser window
        # chrome_options.add_argument("--headless")  # Run headless Chrome to not open a window
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        driver_path = '/Users/edekeulenaar/Code/chromedriver'  # Specify the path to your ChromeDriver
        service = Service(driver_path)
        
        driver = webdriver.Chrome(service=service, options=chrome_options)

        try:
            driver.get(url)
            time.sleep(3)  # Wait for the page to load completely

            try:
                element = driver.find_element(By.CLASS_NAME, class_name)
                inner_html = element.get_attribute('innerHTML')
                
                # Parse the inner HTML to extract text and links
                soup = BeautifulSoup(inner_html, 'html.parser')
                texts = [span.get_text() for span in soup.find_all('span')]
                links = [a['href'] for a in soup.find_all('a', href=True)]
                
                result_text = ' '.join(texts).strip()
                result_links = ' '.join(links).strip()
                
                if result_text or result_links:
                    return result_text + ' ' + result_links
                else:
                    return "Online"
            except Exception as e:
                return "Online"
        finally:
            driver.quit()

    # Process each URL and save results
    current_date = datetime.now().strftime("%Y-%m-%d")

    for index, row in df.iterrows():
        url = row['link']
        result = check_class_on_page(url, 'css-175oi2r r-1ny4l3l')
        df.at[index, 'Status'] = result
        df.at[index, 'Date scraped'] = current_date
        df.at[index, 'driver'] = 'Chrome'
        print(f"{url} - {result}")  # Debugging statement to ensure processing

        # Save the updated DataFrame to the CSV file immediately
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
    mode = 'file'  # Change to 'file' if processing a single file
    path = '/path/to/your/file/or/folder/here'  # Update this to your specific file or folder path. On MacOS, select a file or folder in the Finder and press the option-key while right-clicking and choose Copy "selected item" as pathname.

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
