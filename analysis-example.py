import json
import os
from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt

rootdir = "C:\Annies-Documents\Projects\Redeemer\\2018\\04"

for subdir, dirs, files in os.walk(rootdir):
	for file in files:
		print(file)
		os.path.join(subdir, file)
		'''		path_to_json = '2018/04/06/'''
		'''json_files = [pos_json for pos_json in os.listdir(path_to_json)]

		# You must change the date for the file you want to analyse!!!!
		for file in json_files:
		'''
		json_data = pd.read_json('{}'.format(os.path.join(subdir, file)), orient='columns')
		json_data = pd.read_json(json_data.to_json(), orient='index')

		#Plot the overall figure
		fig = plt.figure()

		#Adds first subplot
		ax1 = fig.add_subplot(2,1,1)
		ax1.title.set_text('Bid-Ask Spread {} (2 sec intervals)'.format(file))

		#Determines which pieces of the data are graphed together and asigns label
		ax1.plot(json_data['ask_price'], label='ask price')
		ax1.plot(json_data['bid_price'], label='bid price')
		ax1.plot(json_data['last_trade_price'], label='last trade price')
		ax1.legend(loc=1, ncol=3, shadow=True)

		#Adds second subplot
		ax2 = fig.add_subplot(2,1,2)
		ax2.title.set_text('Bid-Ask Size Spread')
		ax2.plot(json_data['ask_size'], label='ask size')
		ax2.plot(json_data['bid_size'], label='bid size')
		ax2.legend(loc=1, ncol=3, shadow=True)

		#Opens window with graph when program is run
		plt.tight_layout()
		plt.show()

		#Prints quote info to command line
		print(json_data)