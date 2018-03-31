import json
from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_json('2018/03/29/MSFT.json', orient='columns')
data = pd.read_json(data.to_json(), orient='index')
data = data.loc[:,['ask_price']]
data.index.name = 'dateTime'

data.plot()
plt.title('Intraday Ask Price for MSFT(1 sec)')
plt.show()
print(data)