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

# Prices of products
prices = soup.find_all("h4",class_ = "pull-right")
prices_list = []

for i in prices:
    price = i.text
    prices_list.append(price)

# Description of products
desc = soup.find_all("p",class_ = "description")
desc_list = []

for i in desc:
    description = i.text
    desc_list.append(description)

# Number of reviews of products
reviews = soup.find_all("p",class_ = "review-count")
reviews_list = []

for i in reviews:
    review = i.text
    reviews_list.append(review)

df = pd.DataFrame({"Product Name":product_name, "Price":prices_list, "Description":desc_list, "Reviews":reviews_list})
df.to_csv("product_details.csv")