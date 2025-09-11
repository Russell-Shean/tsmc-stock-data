import yfinance as yf
import pandas as pd

import datetime

# Define time range (last 10 years)
start_date = datetime.date(2016, 1, 1)


# Define a function ------------------------------------------------------------------------------------------d----
def get_yfinance_data(start_date, interval, ticker, file_name):
    
    

    df = yf.download(ticker, start=start_date, interval=interval)
    
    print(df)
    
    df.columns = df.columns.droplevel(1)
    
    df['Ticker'] = ticker
    
    # Step 3: Reset index to bring 'Date' into a column (optional)
    df = df.reset_index()
    
    df.to_csv(file_name, index=False)



# NASDAQ DATA ------------------------------------------------------------------------------------------------------
get_yfinance_data(start_date=start_date,
                  interval="1D",
                  ticker="^IXIC",
                  file_name="data/tsmc/nasdaq_daily_closing_price.csv") 
 
 

# Philadelphia Semiconductor Index (SOX) ----------------------------------------------------------------------------
get_yfinance_data(start_date=start_date,
                  interval="1D",
                  ticker="^SOX",
                  file_name="data/tsmc/sox_daily_closing_price.csv") 
 




# S and P Index ----------------------------------------------------------------------------
get_yfinance_data(start_date=start_date,
                  interval="1D",
                  ticker="^GSPC",
                  file_name="data/tsmc/SandP_daily_closing_price.csv") 
 

# S and P volitility Index ----------------------------------------------------------------------------
get_yfinance_data(start_date=start_date,
                  interval="1D",
                  ticker="^VIX",
                  file_name="data/tsmc/vix_daily_closing_price.csv") 