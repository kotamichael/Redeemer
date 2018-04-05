redeemer = """\n\n\n\n

     :::::::..  .,:::::::::::::-.   .,:::::: .,::::::  .        :   .,::::::  :::::::..   
     ;;;;``;;;; ;;;;""`" ;;,   `';,,;;;;""`" ;;;;""`"  ;;,.    ;;;  ;;;;""`"  ;;;;``;;;;  
      [[[,/[[['  [[cccc  `[[     [[  [[cccc   [[cccc   [[[[, ,[[[[,  [[cccc    [[[,/[[['  
      $$$$$$c    $$""`"   $$,    $$  $$""`"   $$""`"   $$$$$$$$"$$$  $$""`"    $$$$$$c    
      888b "88bo,888oo,__ 888_,o8P'  888oo,__ 888oo,__ 888 Y88" 888o8888ooo,__ 8888b 88bo,
      MMMM   "W" ""`"YUMMMMMMMP"`    ""`"YUMMM`"'"YUMMMMMM  M'  "MMM"'""YUMMMMMMMM   "WW"  
         
"""

'''
Next task is to make this a scheduled program that only runs from
opening to closing during trading days. That way you could have a
Conda prompt dedicated to running this perpetually.
'''

from Robinhood import Robinhood
import schedule
import time
from time import strftime
from datetime import datetime
import json
import os

#Setup connection
my_trader = Robinhood();

#LOGIN Place your credentials here:
my_trader.login(username="dsm080993@gmail.com", password="iy'LaCAQpfdX")

#List of stock symbols. Substitute for those which you desire.
fieldsToGlean = 'MSFT','GOOG','AAPL','FB','TSLA','EBAY','BAC'

#Gleaning graphic
gleanSymbol = """
				  _______ __                  __                      
				|   _   |  .-----.---.-.-----|__.-----.-----.         
				|.  |___|  |  -__|  _  |     |  |     |  _  |__ __ __ 
				|.  |   |__|_____|___._|__|__|__|__|__|___  |__|__|__|
				|:  1   |                             |_____|         
				|::.. . |                                             
				`-------'"""

verse = '''
	Ruth said, “Do not urge me to leave you or to return from following
	you. For where you go I will go, and where you lodge I will lodge.
	Your people shall be my people, and your God my God. Where you die I will
	die, and there will I be buried. May the LORD do so to me and more also
	if anything but death parts me from you.” (Ruth 1:16-17)\n\n'''

print("{}".format(redeemer))
print("{}".format(verse))

#Method to get the stock quote information from the Robinhood API
def glean(stock):
	print(datetime.now().strftime('%H:%M:%S'))
	quote_info = my_trader.quote_data(stock)

	#######  W R I T E   I N F O   T O   J S O N   F I L E ######

	data = []

	#Beautifies the maneuver which places the Update time as the index
	timeStamp = (quote_info["updated_at"])

	#Sets time-based variables for use in the directory structure
	time = timeStamp[11:][:-1]
	year = timeStamp[:4]
	month = timeStamp[:7][5:]
	day = timeStamp[8:][:2]
	timeIndex = ("\n  \"{}\": ".format(time))
	path = "{}/{}/{}/".format(year, month, day)
	filename = '{}.json'.format(stock)
	fname = "{}{}".format(path, filename)

	#Checks for preexisting members of the path and generates any missing part.
	if not os.path.exists(path):
	    os.makedirs(path)

	#Checks for preexisting files with this symbol's data. If not it makes one.
	if not os.path.isfile(fname):

		#Keeps us up to date with where Ruth is in the process.
		global gleanSymbol
		print(gleanSymbol)
		gleanSymbol = "Gleaning...{}".format(stock)

		#Inserts the json data into the empty list in order to put it in the file.
		with open(fname, mode='a') as f:
			f.write("{{{}".format(timeIndex))
			json.dump(quote_info, f)

		#Adds closing curly brace to maintain JSON structure
		with open(fname, mode='ab+') as b:
			b.seek(-1, 1)
			b.truncate()
			b.write('}\n}'.encode('utf8'))
	
	#If the file DID already exist this updates it with the new data
	else:
		#Updates user with which stock is being handled
		print("Gleaning {}...".format(stock))

		#Inserts the comma between entries before adding new entry
		with open(fname, mode='ab+') as s:
			s.seek(-2, 1)
			s.truncate()
			s.write(','.encode('utf8'))

		#Adds time index followed by new entry
		with open(fname, mode='a') as f:
			f.write(timeIndex)
			json.dump(quote_info, f)

		#Adds closing curly-brace to maintain proper JSON formatting as data builds
		with open(fname, mode='ab+') as b:
			b.seek(-1, 1)
			b.truncate()
			b.write('}\n}'.encode('utf8'))

	print("Success!\n");

#Iterates through list of stocks at top of file running them through the glean() function.
def ruthGlean():
	for eachStock in fieldsToGlean:
		glean(eachStock)

'''
Schedule gleaning: default 1 second, but you can substitute .minutes 
etc. This is only to demonstrate speed and efficiency. For more meaningful
data, maybe try more like 10 seconds.
'''
def opening_bell():
	schedule.every(1).minutes.do(ruthGlean).tag('gather')

def closing_bell():
	schedule.clear('gather')
	print("Done!")

'''
Set start and end times of gathering data. No need to end program unless chaning
the default times. Set the startup ahead one interval of running, because Ruth will
wait one run interval before starting. E.g. if she's set to run once every minute, set
the start time one minute ahead of that desired; for 20 seconds, set her 20 seconds ahead.
'''
schedule.every().day.at("9:29").do(opening_bell)
schedule.every().day.at("16:30").do(closing_bell)

while True:
	schedule.run_pending()