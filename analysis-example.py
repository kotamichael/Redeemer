import json
from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt

# You must change the date for the file you want to analyse!!!!
MSFT = pd.read_json('2018/04/02/MSFT.json', orient='columns')
MSFT = pd.read_json(MSFT.to_json(), orient='index')

fig = plt.figure()

ax1 = fig.add_subplot(2,1,1)
ax1.title.set_text('Bid-Ask Spread MSFT (2 sec intervals)')
ax1.plot(MSFT['ask_price'], label='ask price')
ax1.plot(MSFT['bid_price'], label='bid price')
ax1.legend(loc=1, ncol=3, shadow=True)

ax2 = fig.add_subplot(2,1,2)
ax2.title.set_text('Bid-Ask Size Spread')
ax2.plot(MSFT['ask_size'], label='ask size')
ax2.plot(MSFT['bid_size'], label='bid size')
ax2.legend(loc=1, ncol=3, shadow=True)

plt.show()
plt.tight_layout()
print(MSFT)
