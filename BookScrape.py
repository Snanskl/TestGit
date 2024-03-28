import csv
import os
import requests
from bs4 import BeautifulSoup

#url where we want to scraped from
url = 'http://books.toscrape.com/'

#Getting the page
response = requests.get(url)

#Parsing the page with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')


#We want name of thye book, price, and rating of the book
book_name = soup.find_all('li', attrs = {"class" : "col-xs-6 col-sm-4 col-md-3 col-lg-3"})
book_data = []


# Looping through the book_name to get the title of the book
#h3 is the upper tag where the name is under, and a is the tag where the title is. 'title' is the attribute of the tag
for book in book_name:
    title = book.find('h3').find('a').get('title')
    price = book.find('p', attrs = {"class" : "price_color"}).text #'p' is at the same row as the price tag is
    rating = book.find('p').get('class')[1] #rating is the second class of the p tag
    book_data.append({'Title': title, 'Price': price, 'Rating': rating})#append the data to the book_data list
    
print(book_data)

#Working with the csv file. 'w'= write ,ode. 'newline' is used to avoid blank lines between rows
#encoding is used to avoid encoding errors
#DictWriter is used to write the data in dictionary format
#fieldnames are the column names
with open ('Books.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames = ['Title', 'Price', 'Rating'])
    writer.writeheader()
    for book in book_data: #looping while writing the data into the csv file
        writer.writerow(book)