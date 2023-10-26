#Analisaremos series temporais referente a ações dos ultimos dias

import yfinance as yf
import pandas as pd
ticker = 'TSLA'
tkr = yf.Ticker(ticker)
df = tkr.history(period='5d')

print(df)

#Iremos focar na coluna "close"

print(df['Close'])

# Calculando mudanças percentuais usando o metodo shift()

print(pd.concat([df['Close'], df['Close'].shift(2)], axis=1, keys= ['Close', '2DaysShift']))

#Para calcular a mudança percentual

print((df['Close'] - df['Close'].shift(2))/ df['Close'].shift(2))

# Utilizaremos o logaritimo natural log() para calcular a diferença e armazenar em nova coluna
import numpy as np
df['2daysRise'] = np.log(df['Close'] / df['Close'].shift(2))
print(df[['Close', '2daysRise']])

#Calculos de janela rolante
#Utilizaremos o metodo rolling() para analisar a janela rolante

df['2daysAvg'] = df['Close'].shift(1).rolling(2).mean()
print(df[['Close', '2daysAvg']])

#Calculando a mudança percentual de uma média móvel utilizando log()

df['2daysAvgRise'] = np.log(df['Close'] / df['2daysAvg'])
print(df[['Close', '2daysRise', '2daysAvgRise']])


