# Add a new recipe to the database

from urllib.parse import urlparse   # For pulling domain names from urls
import scrape_domains, database as db

c = db.cur

# Get the domain of a url
def get_domain(url):
    domain = urlparse(url).netloc
    return domain   # ex. url 'https://www.website.com/home_page/test' returns as domain 'www.website.com'

# Runs specific scraping function based on the domain name
def pick_domain(url):
    domain = get_domain(url)    # Returns the domain name from the url
    match domain:
        case "www.budgetbytes.com" : scrape_domains.budget_bytes(url),
        case "ohsnapmacros.com": scrape_domains.oh_snap_macros(url),

def new_recipe(url):
    domain = get_domain(url)

    c.execute("SELECT domain_name FROM domains")
    domains = c.fetchall()
    c.execute("SELECT url FROM recipes")
    urls = c.fetchall()
    domains_list = [item[0] for item in domains]
    urls_list = [item[0] for item in urls]


    if url not in urls_list and domain in domains_list:
        pick_domain(url)   # Add new recipe data to the db
    elif url not in urls_list and domain not in domains_list:
        print ("This website cannot be properly accessed. Contact admin.")
    else:
        print("This recipe is already in the database.\n")

