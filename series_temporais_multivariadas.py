#Vamos obter cinco dias de dados de ação para multiplos ticker:

import pandas as pd
import yfinance as yf

stocks = pd.DataFrame()
tickers = ['MSFT', 'TSLA', 'GM', 'AAPL', 'ORCL', 'AMZN']
for ticker in tickers:
    tkr = yf.Ticker(ticker)
    hist = tkr.history(period='5d')
    hist= pd.DataFrame(hist[['Close',]].rename(columns={'Close': ticker}))
    if stocks.empty:
        stocks = hist
    else:
        stocks = stocks.join(hist)

print(stocks)

#Vamos processar séries temporais multivariadas
#Vamos eliminar os ticker que cairam mais de 3% com o metodo shif() para comparar

stocks_to_keep = []
for i in  stocks.columns:
    if stocks[stocks[i]/stocks[i].shift(1)< .97].empty:
        stocks_to_keep.append(i)

print(stocks_to_keep)

#Mostrando apenas as linhas da lista stocks_to_keep

print(stocks[stocks_to_keep])
