# import libraries

from bs4 import BeautifulSoup
import requests
import datetime
import time
 
import smtplib

# Connect to website

url = "https://www.amazon.com/Data-Analyst-Definition-Scientist-Expert/dp/B0CVTSG4BB/ref=sr_1_3_sspa?dib=eyJ2IjoiMSJ9.gohP5rh17WZ97AwXis9fHz92zA63y9onNDE5DghtUSaHw8_I91jB8brqFTh2G8fRYVkVA2jh_Kd_Eb2SJ5U-5bRtDF0BR_-h5h1gpj4dSBn6gClzE_h89qJ1Vk-tpcZkU8Z6gChFGL-Md5XrlfDdweK7Cfwf6d6hQ-H8DEqtGZz9NlmsYDEbpVqpHJ-98W3qI9e0y8VjFRnCFYDUKP9aKvdt0c4Q89GnkdMIIrMg5PW-wDKF7sKINDDAhTBo7tTZDL2ohHk6kDEoQ3ZOyTfgT0dXQUwa8WLwMmouvGxreVM.8wpyRKfbLNjZLIhecv0qnTd2yTjGtGHBezKKLE9D7Zs&dib_tag=se&keywords=data+analytics+t+shirt&qid=1742286798&sr=8-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
header = ('"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"')

page = requests.get(url)

soup1 = BeautifulSoup(page.content, "html.parser")
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id ="producttitle").get_text()

price = soup2.find(id= 'priceblovk_ourprice').get_text()

price = price.strip()[1:]
title = title.strip()

today = datetime.date.today()

import csv

header_csv = ["Product", "Price", "Date"]
data = [title, price, today]

with open('AmazonWebscraperDataSet','w', newline='',encoding="UTF-8") as f:
     write = csv.writer(f)
     write.writerow(header_csv)
     write.writerow(data)
     write.writerow(today)
     
     
with open('AmazonWebscraperDataSet','a+', newline='',encoding="UTF-8") as f:
     write = csv.writer(f)
     write.writerow(data)

     
def price_update():
    url = "https://www.amazon.com/Data-Analyst-Definition-Scientist-Expert/dp/B0CVTSG4BB/ref=sr_1_3_sspa?dib=eyJ2IjoiMSJ9.gohP5rh17WZ97AwXis9fHz92zA63y9onNDE5DghtUSaHw8_I91jB8brqFTh2G8fRYVkVA2jh_Kd_Eb2SJ5U-5bRtDF0BR_-h5h1gpj4dSBn6gClzE_h89qJ1Vk-tpcZkU8Z6gChFGL-Md5XrlfDdweK7Cfwf6d6hQ-H8DEqtGZz9NlmsYDEbpVqpHJ-98W3qI9e0y8VjFRnCFYDUKP9aKvdt0c4Q89GnkdMIIrMg5PW-wDKF7sKINDDAhTBo7tTZDL2ohHk6kDEoQ3ZOyTfgT0dXQUwa8WLwMmouvGxreVM.8wpyRKfbLNjZLIhecv0qnTd2yTjGtGHBezKKLE9D7Zs&dib_tag=se&keywords=data+analytics+t+shirt&qid=1742286798&sr=8-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
    header = ('"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"')

    page = requests.get(url, headers=header)

    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id ="producttitle").get_text()

    price = soup2.find(id= 'priceblovk_ourprice').get_text()

    price = price.strip()[1:]
    title = title.strip()

    import datetime
    
    today = datetime.date.today()
    import csv
    
    header_csv = ["Product", "Price", "Date"]
    data = [title, price, today]
        
    with open('AmazonWebscraperDataSet','a+', newline='',encoding="UTF-8") as f:
        write = csv.writer(f)
        write.writerow(data)

while(True):
    price_update()
    time.sleep(86400)