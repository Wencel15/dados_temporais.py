#Obtendo um mes de dados de uma ação

import yfinance as yf
import numpy as np
ticker = 'TSLA'
tkr = yf.Ticker(ticker)
df = tkr.history(period='1mo')

#Vamos utilizar somente as colunas CLose e Volume

df = df[['Close', 'Volume']].rename(columns={'Close': 'Price'})

print(df)

#Calcular a mudança percentual diaria com shift(1) e log()

df['PriceRise'] = np.log(df['Price'] / df['Price'].shift(1))

#Utilizamos a mesma tecnica para criar uma coluna VolumeRise

df['VolumeRise'] = np.log(df['Volume'] / df['Volume'].shift(1))

print(df)

#Vamos filtrar os dias que as ações excede o threshold em 5%

print(df[abs(df['PriceRise']) > .05])

#Agora calculamos a mudança média do volume ao longo de toda a série

print(df['VolumeRise'].mean().round(4))
