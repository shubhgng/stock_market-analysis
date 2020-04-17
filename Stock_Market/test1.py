import datetime as dt 
import matplotlib.pyplot as plt 
import pandas as pd 
#from matplotlib.finance import candlestick_ohlc
#import mplfinance as mpf
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas_datareader.data as web 
from matplotlib import style 

style.use('ggplot')

start = dt.datetime(2000, 1, 1)
end = dt.datetime(2019, 12 , 31)

df = web.DataReader('TSLA', 'yahoo', start, end)
df.to_csv('tsla.csv')
df.head()

df = pd.read_csv('tsla.csv', parse_dates = True, index_col = 0)
#df['100ma'] = df['Adj Close'].rolling(window = 100, min_periods = 0).mean()
#df.head()
#df.tail()
df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

df_ohlc.reset_index(inplace = True)
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)


ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan = 5, colspan = 1)
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan = 1, colspan = 1, sharex = ax1)
ax1.xaxis_date()

candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)

plt.show()