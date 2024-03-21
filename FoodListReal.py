import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime

#strftime = format string
#%A = full weekend day name %d = the day of the month %B = full month name
todays_date = datetime.now().strftime("%A %d %B") 

#get request from the website
page_to_scrape = requests.get("https://jonsjacob.gastrogate.com/lunch/")

#Reference to BeautifulSoup class where we parse the page_to_scrape content (parse = taking doc and extracting meaningful data from it)
#Now we have assigned the parsed content to soup
soup = BeautifulSoup(page_to_scrape.content, 'html.parser')

#Fine the date in the page, basically extracting datetime from the page
#h3 = header 3
date_element = soup.find('th', class_="menu_header").find('h3')
date = date_element.text if date_element else 'No Date Found'

#find all the name of the food from table body
food_name_elements = soup.find_all('td', class_="td_title")
price_elements = soup.find_all('div', class_="price-alt")

# create a csv file with the date and food name and price with the string format 
csv_filename = f"FoodList_{datetime.now().strftime('%Y%m%d')}.csv" 

#open the file in write mode, newline='' is used to prevent blank lines between rows
#encoding='utf-8' is used to encode the file in utf-8 format called file
with open(csv_filename, "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file) #create a writer object, meaning we allowed to write in the csv file
    writer.writerow(["Date", "Food Name", "Price"]) #write the first row in the csv file, this will show as a row header

#in zip is used to combine two lists together
    for food_element, price_element in zip(food_name_elements, price_elements):
        food_name = food_element.get_text(strip=True) # get the text from the food_element and strip any whitespace
       # get the text from the price_element and if price_element is not found, set price to 'No Price'
        price = price_element.find('strong').text if price_element else 'No Price' 
        
        #print the date, food name and price
        print(date + " - " + food_name + " - " + price)
        #write it in the csv file
        writer.writerow([date, food_name, price])
