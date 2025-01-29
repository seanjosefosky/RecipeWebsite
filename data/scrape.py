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
from selenium.webdriver.chrome.options import Options

urls = ["https://www.budgetbytes.com/bacon-spinach-pasta-parmesan/"]

def main():
    # initialize the chrome driver
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options = chrome_options)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # Iterate through 'urls' and do what's inside the loop to every url
    for url in urls:
        driver.get(url)
        # Get title
        title = soup.h1.get_text()
        # Get 
        print(title)
    driver.close() # Close the driver instance

if __name__ == "__main__":
    main()