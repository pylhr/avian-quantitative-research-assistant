import requests


# Example function to get stock prices
def get_stock_data(ticker):
    # Placeholder implementation
    # Replace with actual API call to a service like Alpha Vantage or Yahoo Finance
    response = requests.get(
        f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=5min&apikey=BAR9T6XZNMM4WJMB"
    )
    data = response.json()
    # Extracting the latest time series data
    latest_timestamp = list(data["Time Series (5min)"].keys())[0]
    stock_info = data["Time Series (5min)"][latest_timestamp]

    return {
        "open": stock_info["1. open"],
        "high": stock_info["2. high"],
        "low": stock_info["3. low"],
        "close": stock_info["4. close"],
        "volume": stock_info["5. volume"],
        "timestamp": latest_timestamp,
    }
