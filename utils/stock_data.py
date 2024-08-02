import yfinance as yf


# Example function to get stock prices
def get_stock_data(ticker):

    response = yf.Ticker(ticker).history(period="1d", interval="1m")

    if not response.empty:
        latest = response.iloc[-1]
        return {
            "open": latest["Open"],
            "high": latest["High"],
            "low": latest["Low"],
            "close": latest["Close"],
            "volume": latest["Volume"],
            "timestamp": latest.name,
        }

