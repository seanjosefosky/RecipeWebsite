import database as db
import newrecipe

def main():
    db.make_tables()
    db.new_domain("www.budgetbytes.com")

    newrecipe.new_recipe(input("What's your recipe url? "))

    # Copy this for testing
    # https://www.budgetbytes.com/bacon-spinach-pasta-parmesan/

if __name__ == "__main__":
    main()