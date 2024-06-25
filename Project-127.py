from selenium import webdriver 
from bs4 import BeautifulSoup
import time 
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars"

# Webdriver
service = webdriver.EdgeService(executable_path="C:/Users/seanl/OneDrive/Desktop/Coding/Sean Code/PRO/Projects 102+/Project-127Web_Scrapping/msedgedriver.exe")
browser = webdriver.Edge(service=service)
browser.get(START_URL)

scraped_data = []
stars_data = []
temp_list = []

#Define Data Scrapping Method
def scrape():
    soup = BeautifulSoup(browser.page_source, "html.parser")
    
    bright_star_table = soup.find("table", attrs={"class", "wikitable sortable sticky-header jquery-tablesorter"})

    table_body = bright_star_table.find("tbody")

    table_rows = table_body.find_all("tr")

    for row in table_rows:
        table_cols = row.find_all("td")
        #print(table_cols)
        temp_list = []

        for col_data in table_cols:
            #print(col_data.text)
            data = col_data.text.strip()

            temp_list.append(data)

        scraped_data.append(temp_list)

scrape()

headers = ["Star_name", "Visual_Magnitude", "Bayer_Designation", "Distance", "Spectral_Type", "Celestial_Hemisphere"]

for i in range(0, len(scraped_data)):
    Star_names = scraped_data[0][i+2]
    Visual_Magnitude = scraped_data[0][i+1]
    Bayer_Designation = scraped_data[0][i+3]
    Distance = scraped_data[0][i+4]
    Spectral_Type = scraped_data[0][i+5]
    Celestial_Hemisphere = scraped_data[0][i+6]

    required_data = [Star_names, Visual_Magnitude, Bayer_Designation, Distance, Spectral_Type, Celestial_Hemisphere]
    stars_data.append(required_data)

star_df_1 = pd.DataFrame(stars_data, columns=headers)

star_df_1.to_csv("scraped_data.csv", index=True, index_label="id")

print(f"This is scraped Data {scraped_data}")