import requests
from bs4 import BeautifulSoup
import urllib.request
import os

# Example Amazon URL (replace with the correct search or product listing page)
url = 'https://www.amazon.com/s?k=laptops'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# Send the HTTP request
response = requests.get(url, headers=headers)

# Create BeautifulSoup object
soup = BeautifulSoup(response.content, 'html.parser')

# Create a folder to save images
if not os.path.exists('product_images'):
    os.makedirs('product_images')

# Find products and extract data (example for 5 products)
products = soup.find_all('div', {'data-component-type': 's-search-result'}, limit=5)

for i, product in enumerate(products):
    try:
        # Extract product name
        name = product.find('span', class_='a-size-medium').text.strip()
        
        # Extract image URL
        img_tag = product.find('img', class_='s-image')
        img_url = img_tag['src']

        # Save the image
        img_path = f'product_images/product_{i+1}.jpg'
        urllib.request.urlretrieve(img_url, img_path)

        # Output product name and image path
        print(f'Product {i+1}: {name}')
        print(f'Image saved at: {img_path}\n')
    
    except AttributeError:
        continue

print("Products scraped and images saved.")
