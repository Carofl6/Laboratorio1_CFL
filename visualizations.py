
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: visualizations.py : python script with data visualization functions                         -- #
# -- author: CAROFL6                                                                      -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: https://github.com/Carofl6/Laboratorio1_CFL                                                                    -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

# Import libraries
import plotly.express as px

## -------------------------------------- Visualization functions -------------------------------------- ##

def pie_chart(df):
    """
    Interactive pie charts.
    
    """
    
    # Stock Weightings
    fig1 = px.pie(df, values = "Peso (%)", names = "Ticker", title = "NAFTRAC Stock Weightings (%)")
    
    # Sector Weightings
    df = df.groupby("Sector").sum()
    if df["Peso (%)"].sum() != 1:
        df.loc["Efectivo", :] = [1 - df["Peso (%)"].sum(), 0]
    
    df.reset_index(inplace = True)
    fig2 = px.pie(df, values = "Peso (%)", names = "Sector", title = "NAFTRAC Sector Weightings (%)")
    
    return fig1, fig2

def time_series(df, title):
    """
    Interactive time series plots.
    
    """
    
    fig = px.line(x = df.index, y = df.Capital, title = title, 
                  labels={"x": "Date", "y" : "Mexican Pesos MXN"})
    
    return fig



