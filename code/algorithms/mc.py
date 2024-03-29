# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 11:05:44 2020

@author: salam_000
"""

import pandas_datareader.data as web
import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

start = dt.datetime(2017, 1, 3)
end = dt.datetime(2017, 11, 20)

prices = web.DataReader('AAPL', 'famafrench', start, end)['Close']
returns = prices.pct_change()

last_price = prices[-1]

# Number of simulations
num_simulations = 1000
num_days = 525

simulation_df = pd.DataFrame()

for x in range(num_simulations):
    count = 0
    daily_vol = returns.std()
    
    price_series = []
    
    price = last_price * (1 + np.random.normal(0, daily_vol))
    price_series.append(price)
    
    for y in range(num_days):
        if count == 251:
            break
        price = price_series[count] * (1 + np.random.normal(0, daily_vol))
        count += 1
        
    simulation_df[x] = price_series

fig = plt.figure()
fig.suptitle('Monte Carlo Simulation: APPL')
plt.plot(simulation_df)
plt.axhline(y = last_price, color = 'r', linestyle = '-')
plt.xlabel('Day')
plt.ylabel('Price')
plt.show()    