import json
from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_json('MSFT.json', orient='columns')
data = pd.read_json(data.to_json(), orient='index')
data = data.loc[:,['ask_price']]
data.index.name = 'dateTime'

data.plot()
plt.title('Made up Intraday Ask Price for MSFT over 11 mins (1 min)')
plt.show()
print(data)