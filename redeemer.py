#!/usr/bin/python

'''          <<<<<<<<<<<<<<<<<<   T O   D O   L I S T  >>>>>>>>>>>>>>>>>>>>>>>

 [1] Switch from using file storage to in-memory/Jupyter Notebook
 [2] Host notebook online
'''


redeemer = """\n\n\n\n

     :::::::..  .,:::::::::::::-.   .,:::::: .,::::::  .        :   .,::::::  :::::::..   
     ;;;;``;;;; ;;;;""`" ;;,   `';,,;;;;""`" ;;;;""`"  ;;,.    ;;;  ;;;;""`"  ;;;;``;;;;  
      $$$,/$$$'  $$cccc  `$$     $$  $$cccc   $$cccc   $$$$, ,$$$$,  $$cccc    $$$,/$$$'  
      $$$$$$c    $$""`"   $$,    $$  $$""`"   $$""`"   $$$$$$$$"$$$  $$""`"    $$$$$$c    
      $$$b "$$;.,$$$::,__ $$$_,c$$'  $$$cc,__ $$$cc,__ $$$ $$$" $$$c$$$$ccc,__ $$$$; $$;.,
      $$$$   "$" ""`"$$$$$$$$$$"`    ""`"$$$$$`"'"$$$$$$$$  $'  "$$$"'""$$$$$$$$$$   "$$"  
         
"""

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
my_trader.login(username="USERNAME", password="PASSWORD")

#List of stock symbols. Substitute for those which you desire.
fieldsToGlean = 'MSFT'

#Gleaning graphic
gleanSymbol = """
          _______ __                  __                      
        |   _   |  .-----.---.-.-----|__.-----.-----.         
        |.  |___|  |  -__|  _  |     |  |     |  _  |__ __ __ 
        |.  |   |__|_____|___._|__|__|__|__|__|___  |__|__|__|
        |:  1   |                             |_____|         
        |::.. . |                                             
        `-------'"""

verse = """
  Ruth said, "Do not urge me to leave you or to return from following
  you. For where you go I will go, and where you lodge I will lodge.
  Your people shall be my people, and your God my God. Where you die I will
  die, and there will I be buried. May the LORD do so to me and more also
  if anything but death parts me from you." (Ruth 1:16-17)\n\n"""

print("{}".format(redeemer))
print("{}".format(verse))

#Method to get the stock quote information from the Robinhood API
def fetch(stock):
  print(datetime.now().strftime('%H:%M:%S'))
  quote_info = my_trader.quote_data(stock)
  store(quote_info)

def store(quote_info):
  #Sets time-based variables for use in the directory structure
  timeStamp = (quote_info["updated_at"])
  year = timeStamp[:4]
  month = timeStamp[:7][5:]
  day = timeStamp[8:][:2]
  path = "{}/{}/{}/".format(year, month, day)
  filename = '{}.json'.format(quote_info["symbol"])
  full_name = "{}{}".format(path, filename)

  #Checks for preexisting members of the path and generates any missing part.
  if not os.path.exists(path):
      os.makedirs(path)

  #Checks for preexisting files with this symbol's data. If not it makes one.
  if not os.path.isfile(full_name):
    create_file(full_name, quote_info)

  #If the file DID already exist this updates it with the new data
  else:
    append_file(full_name, quote_info)

  print("Gleaning successful!\n");

def create_file(full_name, quote_info):
  #Keeps us up to date with where Ruth is in the process.
  global gleanSymbol
  print(gleanSymbol)
  gleanSymbol = "Gleaning...{}".format(quote_info["symbol"])

  timeIndex = ('\n  "{}": '.format(quote_info["updated_at"][11:][:-1]))

  #Inserts the json data into the empty list in order to put it in the file
  with open(full_name, mode='a') as f:
    f.write("{{{}".format(timeIndex))
    json.dump(quote_info, f)

  #Adds closing curly brace to maintain JSON structure
  with open(full_name, mode='ab+') as b:
    b.seek(-1, 1)
    b.truncate()
    b.write('}\n}'.encode('utf8'))

def append_file(full_name, quote_info):
  #Updates user with which stock is being handled
  print("Gleaning {}...".format(quote_info["symbol"]))

  timeStamp = (quote_info["updated_at"])
  timeIndex = ("\n  \"{}\": ".format(timeStamp[11:][:-1]))

  #Inserts the comma between entries before adding new entry
  with open(full_name, mode='ab+') as s:
    s.seek(-2, 1)
    s.truncate()
    s.write(','.encode('utf8'))

  #Adds time index followed by new entry
  with open(full_name, mode='a') as f:
    f.write(timeIndex)
    json.dump(quote_info, f)

  #Adds closing curly-brace to maintain proper JSON formatting as data builds
  with open(full_name, mode='ab+') as b:
    b.seek(-1, 1)
    b.truncate()
    b.write('}\n}'.encode('utf8'))

#Iterates through list of stocks at top of file running them through the glean() function.
def ruthGlean():
  for eachStock in fieldsToGlean:
    fetch('MSFT')

'''
Schedule gleaning: default 1 second, but you can substitute .minutes 
etc. This is only to demonstrate speed and efficiency. For more meaningful
data, maybe try something smaller, like 10 seconds.
'''
def opening_bell():
  schedule.every(15).seconds.do(ruthGlean).tag('gather')

def closing_bell():
  schedule.clear('gather')
  print("Ding, Ding! Closing bell!")

'''
Set start and end times of gathering data. No need to end program unless chaning
the default times. Set the startup ahead one interval of running, because Ruth will
wait one run interval before starting. E.g. if she's set to run once every minute, set
the start time one minute ahead of that desired; for 20 seconds, set her 20 seconds ahead.
'''

schedule.every().day.at("20:10").do(opening_bell)
schedule.every().day.at("21:34").do(closing_bell)

while True:
  schedule.run_pending()