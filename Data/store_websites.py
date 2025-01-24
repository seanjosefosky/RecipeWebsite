import pandas as pd


site = input("What is your website? ")
sheet = "websites.csv"

def store_website(x):
    print(f"\'{x}\' has been stored.")

store_website(site)