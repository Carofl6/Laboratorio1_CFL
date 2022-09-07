#%% Importo librerías 

import pandas as pd
import numpy as np
import yfinance as yf
import os

inversion = 1000000 #Inversion inicial
comision = .00125 #porcentaje de comision  
filenames = os.listdir(r"C:\Users\Natalia Moreno\Documents\MYST\NAFTRAC_MENSUAL") #Archivo a utilizar 

#%%Funcion data_clean que regresa un DataFrame del 31 de enero con la informacion de excel limpia(data)
#    y una lista de los tickers para ser descargados(tickers)

def data_clean():
    data = pd.read_csv(r"C:\Users\Natalia Moreno\Documents\MYST\NAFTRAC_MENSUAL\NAFTRAC_20200131.csv", skiprows=2)
    data.drop(data.tail(2).index, inplace=True)
    data.drop([10, 16], inplace=True)
    data = data.replace('GFREGIOO', "RA").replace('MEXCHEM*', "ORBIA").replace("LIVEPOLC.1", "LIVEPOLC-1")
    ticker_list = data["Ticker"].tolist()
    tickers = [i.replace('*', '') + ".MX" for i in ticker_list]
    return data, tickers

dat, ticker = data_clean()
