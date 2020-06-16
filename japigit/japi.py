import urllib.request
import urllib.parse
import json




def getStockData(stockSymbol):
    stockURL = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=' + stockSymbol + '&apikey=O29RFVN3YFGI86J5';
    #https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=sony&apikey=demo
    #stockURL = 'https://www.nasdaq.com/symbol/aapl';
    #print('Stock URL is: ' + stockURL);
    connection=urllib.request.urlopen(stockURL);
    responseString = connection.read().decode();
    obj = json.loads(responseString);
    price = obj['Global Quote']['05. price'];
    #print(obj);
    return("The current price of " + str(stockSymbol) + " is: $" + str(price));



stockSymbol = "";

while stockSymbol != 'quit':
    stockSymbol=input("Enter a stock symbol: ");
    stockSymbol=stockSymbol.lower();
    if stockSymbol == 'quit':
        exit;
    else:
        #print("Your stock symbol is: " + stockSymbol);
        print(getStockData(stockSymbol));
print("Program has been terminated by the user.");
print("Stock Quotes retrieved successfully!.");
