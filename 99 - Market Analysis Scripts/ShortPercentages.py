import yfinance as yf
import pandas as pd
from tabulate import tabulate
import time

def get_short_percentage(tickers):
    """
    Fetches the short percentage of float for a list of stock tickers.
    
    :param tickers: List of stock tickers
    :return: DataFrame containing stock ticker and short percentage of float
    """
    stock_data = []

    for ticker in tickers:
        stock = yf.Ticker(ticker)
        try:
            short_percent = stock.info['shortPercentOfFloat']
            stock_data.append({
                'Ticker': ticker,
                'Short % of Float': short_percent * 100  # Convert to percentage
            })
        except KeyError:
            stock_data.append({
                'Ticker': ticker,
                'Short % of Float': 'N/A'
            })
    
    return pd.DataFrame(stock_data)

# Example usage

tickers_input = input("Enter the list of stocks tickers separated by commas ('q' to quit): ")
tickers = []
while tickers_input != "q":
    if not tickers_input:
        tickers += ['AAPL', 'NVDA', 'MSFT'] if not tickers else []  # Add default tickers here
    else:
        tickers += [ticker.strip() for ticker in tickers_input.split(',')]

    short_data = get_short_percentage(tickers)

    # Display the table
    print(tabulate(short_data, headers='keys', tablefmt='grid'))
    time.sleep(5)
    tickers_input = input("Add more tickers of 'q' to quit: ")


    
