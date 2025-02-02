import sqlite3

# connect to this database
con = sqlite3.connect("websites.db")
cur = con.cursor()

def make_tables():
    # RECIPES
    cur.execute('''CREATE TABLE IF NOT EXISTS recipes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    url TEXT NOT NULL,
                    name TEXT NOT NULL
                )''')

    # INGREDIENTS
    cur.execute('''CREATE TABLE IF NOT EXISTS ingredients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    recipe_id INTEGER NOT NULL,
                    ingredient TEXT NOT NULL,
                    FOREIGN KEY (recipe_id) REFERENCES recipes (id)
                )''')

    # RECIPE STEPS
    cur.execute('''CREATE TABLE IF NOT EXISTS steps (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    recipe_id INTEGER NOT NULL,
                    step_number INTEGER NOT NULL,
                    step_description TEXT NOT NULL,
                    FOREIGN KEY (recipe_id) REFERENCES Recipes (id)
                )''')

    # DOMAINS
    cur.execute('''CREATE TABLE IF NOT EXISTS domains (
                    domain_name TEXT
                    )''')

    con.commit()


def new_recipe(url, name):
    cur.execute('''INSERT IF NOT EXISTS INTO recipes (url, name) VALUES (?, ?)''', (url, name))
    con.commit()

def new_ingredients(recipe_id, ingredient):
    cur.execute('''INSERT OR IGNORE INTO ingredients (recipe_id, ingredient) VALUES (?, ?)''', (recipe_id, ingredient))
    con.commit()

def new_steps(recipe_id, step_number, step_description):
    cur.execute('''INSERT OR IGNORE INTO steps (recipe_id, step_number, step_description) VALUES (?, ?, ?)''', (recipe_id, step_number, step_description))
    con.commit()

def new_domain(domain_name):
    cur.execute('''INSERT OR REPLACE INTO domains (domain_name) VALUES (?)''', (domain_name,))
    con.commit()



