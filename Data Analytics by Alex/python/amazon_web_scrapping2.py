# Import required libraries
from bs4 import BeautifulSoup
import requests
import datetime
import time
import csv

# Amazon product URL
url = "https://www.amazon.com/Data-Analyst-Definition-Scientist-Expert/dp/B0CVTSG4BB"

# Proper headers (User-Agent)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
}

# Request the webpage
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")

# Extract product title and price (Check actual class names in DevTools)
title_tag = soup.find("span", {"id": "productTitle"})  # Corrected ID
price_tag = soup.find("span", {"class": "a-offscreen"})  # Corrected class

if title_tag and price_tag:
    title = title_tag.get_text().strip()
    price = price_tag.get_text().strip()[1:]  # Removing currency symbol
else:
    print("Failed to retrieve product data. Check the element selectors.")
    title, price = "N/A", "N/A"

# Get today's date
today = datetime.date.today()

# Write data to CSV file
header_csv = ["Product", "Price", "Date"]
data = [title, price, today]

# Create and write to the CSV file (if it doesn't exist)
with open('AmazonWebscraperDataSet.csv', 'w', newline='', encoding="UTF-8") as f:
    writer = csv.writer(f)
    writer.writerow(header_csv)
    writer.writerow(data)

# Function to update price daily
def price_update():
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    title_tag = soup.find("span", {"id": "productTitle"})
    price_tag = soup.find("span", {"class": "a-offscreen"})

    if title_tag and price_tag:
        title = title_tag.get_text().strip()
        price = price_tag.get_text().strip()[1:]
    else:
        print("Failed to retrieve product data.")
        title, price = "N/A", "N/A"

    today = datetime.date.today()
    data = [title, price, today]

    with open('AmazonWebscraperDataSet.csv', 'a', newline='', encoding="UTF-8") as f:
        writer = csv.writer(f)
        writer.writerow(data)

# Run daily price updates (Every 24 hours)
while True:
    price_update()
    time.sleep(86400)  # Sleep for 24 hours
