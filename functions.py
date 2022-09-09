
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: functions.py : python script with general functions                                         -- #
# -- author: CAROFL6                                                                     -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: https://github.com/Carofl6/Laboratorio1_CFL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

# Import libraries
import visualizations
import pandas as pd
import yfinance as yf
import numpy as np

## ------------------------------------------ General functions ------------------------------------------ ##

def passive_investment_strategy(df, naftrac_date, capital, comission, title):
    """
    Passive Investment Strategy general functions.
    
    """
    
    # Data download from yfinance
    start_date = pd.to_datetime(str(naftrac_date))
    stock_prices = pd.DataFrame()

    for stock in list(df["Ticker"]):
        stock_prices[stock] = yf.download(stock, start_date, progress = False, show_errors = False)["Adj Close"]
    
    stock_prices.reset_index(inplace = True)
    stock_prices = stock_prices.groupby([stock_prices["Date"].dt.year, stock_prices["Date"].dt.month], as_index=False).last()
    stock_prices.set_index("Date", inplace = True)
    
    # Passive strategy backtest
    position_values = [np.floor((capital * weights_i) / (price_i * (1 + comission / 100))) for price_i, weights_i in zip(list(stock_prices.iloc[0, :]), list(df["Peso (%)"]))]
    cash = capital - np.dot(position_values, stock_prices.iloc[0, :] * (1 + comission / 100))
    
    df_passive = pd.DataFrame(index = stock_prices.index)
    df_passive["Capital"] = np.dot(stock_prices, position_values) + cash
    df_passive["Return"] = df_passive["Capital"].pct_change() 
    df_passive["Cummulative Return"] = (df_passive["Return"] + 1).cumprod() - 1
    
    fig = visualizations.time_series(df_passive, title)
    
    # Performance
    df_metrics = pd.DataFrame(index = ["rend_m", "rend_c", "sharpe"], columns = ["descripción", "inv_pasiva"])
    df_metrics.loc["rend_m", "descripción"] = "Rendimiento promedio mensual"
    df_metrics.loc["rend_m", "inv_pasiva"] = df_passive["Return"].dropna().mean()
    df_metrics.loc["rend_c", "descripción"] = "Rendimiento mensual acumulado"
    df_metrics.loc["rend_c", "inv_pasiva"] = df_passive["Cummulative Return"][-1]
    df_metrics.loc["sharpe", "descripción"] = "Sharpe ratio"
    df_metrics.loc["sharpe", "inv_pasiva"] = df_passive["Return"].dropna().mean() / df_passive["Return"].dropna().std()
    
    return df_passive, fig, df_metrics

