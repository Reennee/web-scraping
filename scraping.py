import requests
from bs4 import BeautifulSoup
import csv

# URL to scrape
url = 'https://www.scrapethissite.com/pages/forms/'

# Send HTTP request to the URL
response = requests.get(url)

# Create BeautifulSoup object
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table
table = soup.find('table', class_='table')

# Get all rows from the table
rows = table.find_all('tr')

# Prepare CSV file
with open('scraped_table_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Write headers from the first row
    header = [th.text.strip() for th in rows[0].find_all('th')]
    writer.writerow(header)
    
    # Write the remaining rows
    for row in rows[1:]:
        data = [td.text.strip() for td in row.find_all('td')]
        writer.writerow(data)

print("Tabular data saved in scraped_table_data.csv")
