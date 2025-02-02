from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import database as db
import time

cur = db.cur
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

def budget_bytes(url):
    # 1. Initialize and run the headless site
    driver.get(url)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # 2. Scrape the recipe title
    title = soup.find(class_="entry-title")
    print(title)

    # TODO VVVV
    # 3. Scrape the recipe ingredients
    # ingredients_ul = soup.find('ul', class_="wprm-recipe-ingredients").parent.find_next_sibling()
    # for list_item in ingredients_ul.findall('li'):


        # print(list_item)
        # db.new_ingredients(1, list_item.get_text())

    # 4. Scrape the recipe steps

    # 5. Scrape the recipe nutrition

    # 6. Scrape the recipe photo


    print("Scraped and stored the data from budgetbytes.com")
    driver.close()  # Close the driver instance


def oh_snap_macros(url):
    # Same as above function but specific to this domain's needs
    print("Scraped and stored the data from ohsnapmacros.com")

