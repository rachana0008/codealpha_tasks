import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://quotes.toscrape.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = []
authors = []

for item in soup.find_all("span", class_="text"):
    quotes.append(item.text)

for item in soup.find_all("small", class_="author"):
    authors.append(item.text)

data = pd.DataFrame({
    "Quote": quotes,
    "Author": authors
})

data.to_csv("quotes.csv", index=False)

print("Data saved successfully!")