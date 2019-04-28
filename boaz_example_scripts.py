from Robinhood import Robinhood
from boaz import my_trader

#Get stock information
    #Note: Sometimes more than one instrument may be returned for a given stock symbol
stock_instrument = my_trader.instruments("MSFT")[0]

#Get a stock's quote
###### HERE's an example of a comment for use in the tutorial today I love you eric
my_trader.print_quote("AAPL")

#Prompt user for a symbol
my_trader.print_quote();

#Print multiple symbols
my_trader.print_quotes(stocks=["GOOG", "FB", "MSFT"])

#View all data for a given stock ie. Ask price and size, bid price and size, previous close, adjusted previous close, etc.
quote_info = my_trader.quote_data("BAC")
print(quote_info);

'''
<------------------------ D A N G E R O U S     C O M M A N D S ---------------->
					
					Think twice before uncommenting this section and 
								   watch what you type!!!


#Place a buy order (uses market bid price)
buy_order = my_trader.place_buy_order(stock_instrument, 1)

#Place a sell order
sell_order = my_trader.place_sell_order(stock_instrument, 1)
'''