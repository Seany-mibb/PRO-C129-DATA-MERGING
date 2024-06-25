from selenium import webdriver 
from bs4 import BeautifulSoup
import time 
import pandas as pd
import requests

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

browser = webdriver.Edge()
listables = []

def scrape(hyperlink):
    page = requests.get(hyperlink)
    soup = BeautifulSoup(page.text, "html.parser")
    all_tables = soup.find_all("table", attrs={"class", "wikitable sortable"})
    total_tables = len(all_tables)
    table_rows = all_tables[1].find_all("tr")

    for i in table_rows:
        try:
            table_data = i.find_all("td")
            row = [j.text.rstrip() for j in table_data]
            listables.append(row)
        except:
            listables.append("Unkown")
    print(listables)
scrape(START_URL)

star_name = []
radius = []
mass = []
distance = []

for i in range(1, len(listables)):
    star_name.append(listables[i][0])
    radius.append(listables[i][9])
    mass.append(listables[i][8])
    distance.append(listables[i][5])

#For the csv
headers = ["star_name", "radius", "mass", "distance"]
new_planet_df_1 = pd.DataFrame(list(zip(star_name, radius, mass, distance)),columns = headers)
new_planet_df_1.to_csv('C-128Web_Scrapping2.csv',index=True, index_label="id")