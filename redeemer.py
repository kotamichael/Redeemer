"""

:::::::..  .,:::::::::::::-.   .,:::::: .,::::::  .        :   .,::::::  :::::::..   
;;;;``;;;; ;;;;""`" ;;,   `';,,;;;;""`" ;;;;""`"  ;;,.    ;;;  ;;;;""`"  ;;;;``;;;;  
 [[[,/[[['  [[cccc  `[[     [[  [[cccc   [[cccc   [[[[, ,[[[[,  [[cccc    [[[,/[[['  
 $$$$$$c    $$""`"   $$,    $$  $$""`"   $$""`"   $$$$$$$$"$$$  $$""`"    $$$$$$c    
 888b "88bo,888oo,__ 888_,o8P'  888oo,__ 888oo,__ 888 Y88" 888o8888ooo,__ 8888b 88bo,
 MMMM   "W" ""`"YUMMMMMMMP"`    ""`"YUMMM`"'"YUMMMMMM  M'  "MMM"'""YUMMMMMMMM   "WW"  


Next task is to make this a scheduled program that only runs from
opening to closing during trading days. That way you could have a
Conda prompt dedicated to running this perpetually.


"""
from Robinhood import Robinhood
import schedule
import time
import json
import os

#Setup connection
my_trader = Robinhood();

#LOGIN Place your credentials here:
my_trader.login(username="dsm080993@gmail.com", password="iy'LaCAQpfdX")

#List of stock symbols. Substitute for those which you desire.
fieldsToGlean = 'MSFT','GOOG','AAPL'

#Gleaning graphic
gleanSymbol = """
				  _______ __                  __                      
				|   _   |  .-----.---.-.-----|__.-----.-----.         
				|.  |___|  |  -__|  _  |     |  |     |  _  |__ __ __ 
				|.  |   |__|_____|___._|__|__|__|__|__|___  |__|__|__|
				|:  1   |                             |_____|         
				|::.. . |                                             
				`-------'

		But Ruth said, “Do not urge me to leave you or to return from following
		you. For where you go I will go, and where you lodge I will lodge.
		Your people shall be my people, and your God my God. Where you die I will
		die, and there will I be buried. May the LORD do so to me and more also
		if anything but death parts me from you.” (Ruth 1:16-17)\n"""

#Method to get the stock quote information from the Robinhood API
def glean(stock):
	quote_info = my_trader.quote_data(stock)

	#######  W R I T E   I N F O   T O   J S O N   F I L E ######
	fname = '{}.json'.format(stock)
	data = []
	if not os.path.isfile(fname):

		global gleanSymbol
		print("{}".format(gleanSymbol))
		gleanSymbol = "Gleaning..."
		print("{}".format(stock))
		data.append(quote_info)
		with open(fname, mode='a') as f:
			f.write("{{\n  \"{}\": ".format(quote_info["updated_at"]))
			f.write(json.dumps(quote_info, indent=4, sort_keys=True,
				separators=(',', ': '), ensure_ascii=False))

		with open(fname, mode='ab+') as b:
			b.seek(-1, 1)
			b.truncate()
			b.write('  }\n}'.encode('utf8'))
	else:
		print("Gleaning {}...".format(stock))
		with open(fname, mode='ab+') as s:
			s.seek(-2, 1)
			s.truncate()
			s.write(','.encode('utf8'))

		with open(fname, mode='a') as f:
			f.write("\n  \"{}\": ".format(quote_info["updated_at"]))
			f.write(json.dumps(quote_info, indent=4, sort_keys=True,
				separators=(',', ': '), ensure_ascii=False))

		with open(fname, mode='ab+') as b:
			b.seek(-1, 1)
			b.truncate()
			b.write('  }\n}'.encode('utf8'))

	print("Success!\n");

def ruthGlean():
	for eachStock in fieldsToGlean:
		glean(eachStock)

'''
Schedule gleaning: default 1 second, but you can substitute .minutes 
etc. This is only to demonstrate speed and efficiency. For more meaningful
data, maybe try more like 10 seconds.
'''
schedule.every(3).seconds.do(ruthGlean)
while True:
	schedule.run_pending()