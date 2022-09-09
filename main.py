
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: main.py : python script with the main functionality                                         -- #
# -- author: CAROFL6                                                                       -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: https://github.com/Carofl6/Laboratorio1_CFL                                                                    -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

import data, visualizations, functions

## ------------------------------------------ Main functionality ------------------------------------------ ##

def lab_passive(naftrac_date = 20200131, capital = 1000000, comission = 0.125):
    """
    Lab. 1. Passive Investment Strategy.
   
    """
    
    df, naftrac_date = data.file_reading(naftrac_date = naftrac_date)
    df = data.data_wrangling(df)
    fig1, fig2 = visualizations.pie_chart(df)
    
    df_passive, fig3, df_metrics = functions.passive_investment_strategy(df, naftrac_date, capital, comission, 
                                                         "Passive Investment Strategy: NAFTRAC")    
    
    return df_passive, df_metrics, fig1, fig2, fig3
