# Notes:
# Pandas is an API
# Pandas is actually set of software components , much of  which is not even written in Python.

import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot
import matplotlib.pyplot as plt
import datetime
from pycoingecko import CoinGeckoAPI
from mplfinance.original_flavor import candlestick2_ohlc

dir = {'a':[11,22,33], 'b':[44,55,66]}
df = pd.DataFrame(dir)
print(df)
print(f"head:{df.head()}")
print(f"mean: {df.mean()}")

cg = CoinGeckoAPI()
#get data from CoinGeckoAPI
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)
print(f"bitcoin_data from api : {bitcoin_data}")
print(f"Type of bitcoin_data : {type(bitcoin_data)}")
bitcoin_price_data = bitcoin_data['prices']
print(f"first 5 elemest of price data:{bitcoin_price_data[0:5]}")
#convert data into dataframe
data = pd.DataFrame(bitcoin_price_data, columns=['TimeStamp', 'Price'])
print(f"data in data frame: {data}")
#adding one more column with satndard time
data['Date'] = pd.to_datetime(data['TimeStamp'], unit='ms')
print(f"data in data frame after converting timestamp in std format: {data}")

#grouping of data fro grapha ploting
candlestick_data = data.groupby(data.Date.dt.date, as_index=False).agg({"Price": ['min', 'max', 'first', 'last']})
print(f"data for plotting graph: {candlestick_data}")

#ploating graph
fig = go.Figure(data=[go.Candlestick(x=data['Date'],
                open=candlestick_data['Price']['first'],
                high=candlestick_data['Price']['max'],
                low=candlestick_data['Price']['min'],
                close=candlestick_data['Price']['last'])
                ])

fig.update_layout(xaxis_rangeslider_visible=False)

fig.show()

# pip install pycoingecko
# python
# >>> from pycoingecko import CoinGeckoAPI
# >>> cg = CoinGeckoAPI()
# >>> bitCoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)
# >>> bitCoin_data
# >>> bitCoin_data_prices = bitCoin_data['prices']
# >>> data = pd.DataFrame(bitCoin_data_prices, columns=['TimeStamp', 'Price'])
# >>> data['Date'] = pd.to_datetime(data['TimeStamp'], unit = 'ms')
# >>> candlestrick_data= data.groupby(data.Date.dt.date).agg({'Price': ['min', 'max','first','last']})

#from ibm_watson import SpeechToTextV1



