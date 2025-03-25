from bs4 import BeautifulSoup
import requests

url = 'https://www.scrapethissite.com/pages/forms/'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')

soup.find('div')  # Finds the first occerence of that element
soup.find_all('div') # Finds all the occerences of this html element

#Use attributes / class to specify the element that we want

print(soup.find('div', class_ = 'col-md-12'))
print(soup.find('p', class_ = 'lead').text.strip())