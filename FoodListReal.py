import requests
from bs4 import BeautifulSoup
import os
import csv


base_url = "https://jonsjacob.gastrogate.com/lunch/1/" 
file_name = 'scraped_menu.csv'
request = requests.get(base_url)
soup = BeautifulSoup(request.content, 'html.parser')

# Boolean operator if file exists or is empty (same directory as .py script) 
#file_exists is True if file exists and is not empty
#os = operating system
file_exists = os.path.isfile(file_name) and os.path.getsize(file_name) > 0

# a means append, newline='' is to avoid empty lines between rows
with open(file_name, 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Write the header only if the file did not exist or was empty
    if not file_exists:
        column_names = ['Date', 'Dish', 'Price']
        writer.writerow(column_names)


    # Find every dish for each date
    headers = soup.find_all('thead', attrs={'class': 'lunch-day-header'})

# Loop through each date and strip the text from thehtml tag
    for header in headers:
        dates_tag = header.find('h3')
        dates_text = dates_tag.text.strip()
   
        # Find next dish information within the same date
        #find next sibling is a method that returns the tag that is right after the tag that is passed as an argument
        tbody = header.find_next_sibling('tbody', attrs={'class': 'lunch-day-content'})
        #find_all returns a list of all the tags that match the criteria
        rows = tbody.find_all('tr', attrs={'class': 'lunch-menu-item'})

        for row in rows:

            # Loop through each dish and strip data
            dishes_tag = row.find('td', attrs={'class': 'td_title'})
            dishes_text = dishes_tag.text.strip()

            price_tag = row.find('strong', attrs={'class': 'price-tag'})
            price_text = price_tag.text.strip()

            #write the data to the csv file
            writer.writerow([dates_text, dishes_text, price_text])
            
            
