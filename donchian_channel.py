import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc
import matplotlib.ticker as ticker
from matplotlib.dates import DateFormatter, MinuteLocator


df = pd.read_csv('test.csv', parse_dates=['Date'])
df['Date'] = pd.to_datetime(df['Date'], unit='s').dt.date
array_date = np.array(df['Date'])
array_close = np.array(df['Close Price'])
array_open = np.array(df['Open Price'])
array_high = np.array(df['High Price'])
array_low = np.array(df['Low Price'])
array_volume = np.array(df['No. of Trades'])
print("High Array size", array_high.size)
print("Low Array size", array_low.size)
print("Open Array size", array_open.size)
print("Close Array size", array_close.size)


# Function to caculate the high band
def DchannelUpper(i):
    x = float(0.0)
    if(i < 20):
        for j in range(i, -1, -1):
            x = max(array_high[j], x)
    else:
        for j in range(i-1, i-20, -1):
            x = max(array_high[j], x)
    return x

# Function to caculate the low band


def DchannelLower(i):
    x = float("inf")
    if(i < 20):
        for j in range(i, -1, -1):
            x = min(array_low[j], x)
    else:
        for j in range(i-1, i-20, -1):
            x = min(array_low[j], x)
    return x


# calculating the high band, n = 20

array_upper = []
for i in range(0, array_high.size):
    array_upper.append(DchannelUpper(i))

print("The high band is:")
print(array_upper)


# calculating the low band, n = 20

array_lower = []
for i in range(0, array_low.size):
    array_lower.append(DchannelLower(i))

print("The low band is:")
print(array_lower)


# calculating the mid band, n = 20

array_middle = []
for i in range(0, len(array_lower)):
    array_middle.append((array_upper[i]+array_lower[i])/2)

print("The mid band is:")
print(array_middle)


# Plotting the graph
fig = plt.figure(figsize=(25,15), dpi=50, facecolor='w', edgecolor='k')
ax1 = fig.add_subplot(111)
ax2 = fig.add_subplot(111)
ax1.xaxis_date()
for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(45)
bars = df
bars=bars.reset_index()
bars = bars.ix[:,['Date','Open Price','High Price','Low Price','Close Price']]
bars['Date'] = bars['Date'].map(mdates.date2num)
candlestick_ohlc(ax1,bars.values,width=.5, colorup='green', colordown='red',alpha=0.75)

print(df.index)
df = df.reset_index()
df['Highest high'] = array_upper
df['Lowest low'] = array_lower
df['Middle band'] = array_middle
bands = df.ix[:,['Highest high','Lowest low','Middle band']]
MA = [bands['Highest high'].as_matrix(), bands['Lowest low'].as_matrix(), bands['Middle band'].as_matrix()]
colors = ['blue','blue','yellow']
for color, band in zip(colors,MA):
    ax2.plot(bars['Date'], band,color = color)
plt.title('Donchian Channel', fontsize=20)
plt.ylabel('Stock Values', fontsize=20)
plt.xlabel('Dates', fontsize=15)
plt.xticks(array_date,)
plt.show()


        
        
        
        
    
    
    
    
    

    
