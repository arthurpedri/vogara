import yfinance as yf

data = yf.Ticker("ITUB4.SA")

print(data.info)
