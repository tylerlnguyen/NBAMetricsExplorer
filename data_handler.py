import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Set Constants
DRIVER_PATH = '/Users/tyler/Documents/chromedriver-mac-arm64/chromedriver'

def wait_for_element(driver, timeout):
    """
    Wait for the presence of any element on the webpage.
    """
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*')))
    except TimeoutException as e:
        print(f"Error: {e}. Unable to wait for {timeout} seconds.")

def extract_data_table(driver):
    """
    Extract a data table from the webpage's source code.
    """
    try:
        return pd.read_html(driver.page_source)[3]
    except IndexError as e:
        print(f"Error: {e}. Unable to extract data table.")
        return pd.DataFrame()

def close_driver(driver):
    """
    Close the WebDriver session.
    """
    driver.close()

def get_data():
    """
    Scrape player statistics from an NBA team's webpage and return the data as a pandas DataFrame.
    """
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    driver.get("https://www.nba.com/stats/team/1610612746/players-traditional?LastNGames=15")

    # Wait for 5 seconds for the presence of any element
    wait_for_element(driver, timeout=5)

    # Extract data table
    df_stats = extract_data_table(driver)

    # Close WebDriver
    close_driver(driver)

    return df_stats
