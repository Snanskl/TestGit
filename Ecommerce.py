import bs4 as beautifulsoup
import csv
import requests

page_to_scrape = requests.get("https://webscraper.io/test-sites/e-commerce/allinone")
soup = beautifulsoup.BeautifulSoup(page_to_scrape.content, 'html.parser')

name = soup.find_all('a', attrs = {"class" : "title"} )
price = soup.find_all('h4', attrs = {"class" : "price"} )

file = open("EcommerceDone.csv", "w")
writer = csv.writer(file)
writer.writerow(["Name", "Price"])

for n, p in zip(name, price):
    print(n.text + " - " + p.text)
    print("\n")
    writer.writerow([n.text, p.text])


