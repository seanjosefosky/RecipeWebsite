import sqlite3

# connect to this database
con = sqlite3.connect("websites.db")
cur = con.cursor()

url = "https://www.budgetbytes.com/bacon-spinach-pasta-parmesan/"
name = "Bacon Spinach Pasta Parmesan"

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

# Add information to 'recipes' table using external variables
cur.execute('''INSERT OR IGNORE INTO recipes (url, name) VALUES (?, ?)''', (url, name))

con.commit()


