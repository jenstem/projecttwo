import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)

# Test if website is accessible or not by uncommenting first
# print(r)

soup = BeautifulSoup(r.text, "html.parser")

# Names of products
names = soup.find_all("a",class_ = "title")
print(names)
product_name = []

for i in names:
    name = i.text
    product_name.append(name)