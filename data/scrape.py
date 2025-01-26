# ######################################################################################## #

# This file will contain the main functions to perform
# the scraping portion of the main program.

# What are the different functions of the scraping process?
#   1. Iterate through websites
#   2. Scrape with BeautifulSoup, bs4, possible selenium web driver

# Things we need to pull from websites:
#   - Recipe Names
#   - Recipe ingredients
#   - Recipe instructions
#   - Recipe nutritional information
#   - Photo of the actual meal

# ######################################################################################## #

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode

# Set up the Chrome WebDriver
service = Service('/path/to/chromedriver')  # Replace with the path to your WebDriver


def main():
    driver = webdriver.Chrome(service=service, options=chrome_options)

    urls = ["https://www.budgetbytes.com/bacon-spinach-pasta-parmesan/"]

    for url in urls:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        title = soup.h1.get_text()

        driver.close()
        print(title)


if __name__ == "__main__":
    main()