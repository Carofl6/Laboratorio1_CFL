
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: data.py : python script for data collection                                                 -- #
# -- author: CAROFL6                                                                      -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

# Import libraries
import pandas as pd

## ------------------------------------- Data collection functions ------------------------------------- ##

def file_reading(path = "files/NAFTRAC_", skiprows = 2, naftrac_date = 20200131):
    """
    NAFTRAC files reading.
    
    """
    
    filepath = path + str(naftrac_date) + ".csv" 
    df = pd.read_csv(filepath, skiprows = skiprows)
    
    return df.dropna(), naftrac_date

def data_wrangling(df):
    """
    Data wrangling.
    
    """
    
    df["Peso (%)"] = df["Peso (%)"] / 100
    [df.drop(labels = i, axis = 0, inplace = True) for i in range(len(df)) if df["Ticker"][i] in ["KOFL", "KOFUBL", "MXN", "BSMXB", "NMKA"]];
    df.reset_index(drop = True, inplace = True)
    df["Ticker"] = [stock.replace(".", "-").replace("*", "") + ".MX" for stock in list(df["Ticker"])]
   
    return df
    
    
    
    
    
    