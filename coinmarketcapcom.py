# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 19:50:42 2020

@author: salam_000
"""


import requests
from bs4 import BeautifulSoup

r = requests.get('file:///C:/inetpub/wwwroot/coinmarketcap/coinmarketcap.html')
soup = BeautifulSoup(r.text, 'lxml')

data = []
table = soup.find('table', id='currencies-all')
for row in table.find_all('tr'):
    try:
        symbol = row.find('td', class_='text-left col-symbol').text
        price = row.find('a', class_='price').text
        time_1h = row.find('td', {'data-timespan': '1h'}).text
        time_24h = row.find('td', {'data-timespan': '24h'}).text
        time_7d = row.find('td', {'data-timespan': '7d'}).text
    except AttributeError:
        continue

    data.append((symbol, price, time_1h, time_24h, time_7d))

for item in data:
    print(item)