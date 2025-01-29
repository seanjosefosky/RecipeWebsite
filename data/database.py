import sqlite3

# connect to this database
con = sqlite3.connect("websites.db")
cur = con.cursor()

def make_tables():
    # Create a table called 'recipes' storing url and recipe name
    cur.execute('''CREATE TABLE IF NOT EXISTS recipes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    url TEXT NOT NULL,
                    name TEXT NOT NULL
                )''')

    # Create a table called 'ingredients'
    cur.execute('''CREATE TABLE IF NOT EXISTS ingredients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    recipe_id INTEGER NOT NULL,
                    ingredient TEXT NOT NULL,
                    FOREIGN KEY (recipe_id) REFERENCES recipes (id)
                )''')

    # Create a table called 'steps' to store recipe steps
    cur.execute('''CREATE TABLE IF NOT EXISTS steps (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    recipe_id INTEGER NOT NULL,
                    step_number INTEGER NOT NULL,
                    step_description TEXT NOT NULL,
                    FOREIGN KEY (recipe_id) REFERENCES Recipes (id)
                )''')

    con.commit()

# Insert new recipe data
def new_recipe(url, name):
    cur.execute('''INSERT OR IGNORE INTO recipes (url, name) VALUES (?, ?)''', (url, name))

    con.commit()


