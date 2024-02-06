import yfinance as yf
import matplotlib.pyplot as plt
import time


def fetch_historical_data(symbol, start_date, end_date, interval):
    """
    Fetch historical price data for a given symbol from start_date to end_date.
    """
    data = yf.download(symbol, start=start_date, end=end_date, interval=interval)
    return data


def plot_price_data(data):
    """
    Plot the closing price data.
    """
    plt.figure(figsize=(14, 7))
    plt.plot(data['Close'], label='Close Price')
    plt.title('Historical Close Price')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.show()

# Main usage
symbol = 'BTC-USD'
start_date = '2019-01-01'
end_date = time.strftime("%Y-%m-%d")
interval = '1d'  # Valid intervals: [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]

# Fetch historical data
data = fetch_historical_data(symbol, start_date, end_date, interval)

# Plot price data
plot_price_data(data)
