#Automating data from a crypto api
# How to use a public api

import pandas as pd
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os
from time import time
from time import sleep


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'20',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '72868dba-0ed7-4511-84d4-689c688d65a7',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  #print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
  

import pandas as pd

pd.set_option('display.max_columns', None)
new_data = pd.json_normalize(data['data'])


def api_runner():
    global new_data

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
    'start':'1',
    'limit':'20',
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '72868dba-0ed7-4511-84d4-689c688d65a7',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        #print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
    

    import pandas as pd

    pd.set_option('display.max_columns', None)
    new_data2 = pd.json_normalize(data['data'])

    new_data2['timestamp'] = pd.to_datetime('now')
    new_data = new_data._append(new_data2)
    
    if not os.path.isfile("C:/Users/user/Documents/Programming/Data Analytics by Alex/python/API.csv"):
        new_data.to_csv(r"C:/Users/user/Documents/Programming/Data Analytics by Alex/python/API.csv", header = "column_names")
    else:
        new_data.to_csv(r"C:/Users/user/Documents/Programming/Data Analytics by Alex/python/API.csv",mode= "a", header = "column_names")
  
for i in range(333):
    api_runner()
    print("Api run complete") 
    sleep(60)
exit()


new_data2 =  pd.read_csv("C:/Users/user/Documents/Programming/Data Analytics by Alex/python/API.csv")
new_data3 = new_data2.groupby('name', sort= False)[["quote.USD.percent_change_1h","quote.USD.percent_change_24h","quote.USD.percent_change_7d","quote.USD.percent_change_30d","quote.USD.percent_change_60d","quote.USD.percent_change_90d"]].mean()

new_data4 = new_data3.stack()
new_data5 = new_data4.to_frame(name="values")


Index = pd.Index(range(29838))
new_data6= new_data5.reset_index()
new_data7 = new_data6.rename(columns={'level_1': 'percent_change'})

new_data7['percent_change'] = new_data7['percent_change'].replace(['quote.USD.percent_change_1h','quote.USD.percent_change_24h','quote.USD.percent_change_7d','quote.USD.percent_change_30d','quote.USD.percent_change_60d','quote.USD.percent_change_90d'],['1h','24h','7d','30d','60d','90d'])
print(new_data7)


