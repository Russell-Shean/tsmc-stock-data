import datetime

from FinMind.data import DataLoader
import time

from dotenv import load_dotenv
import os

import pandas as pd

load_dotenv()


# Load credentials from environment variables
API_KEY = os.environ["FINMIND_API_TOKEN"]




# Initialize loader
api = DataLoader()

# Login
api.login_by_token(api_token=API_KEY)

# Define stock ID for TSMC
stock_id = "2330"

# Define time range (last 10 years)
end_date = datetime.date.today()

# This data only starts from 2018-06-05 
start_date = datetime.date(2018, 7, 7)


start_date=start_date.strftime("%Y-%m-%d")
end_date=end_date.strftime("%Y-%m-%d")

# Create a range of dates for loop through
# because some of the endpoints only return single days at a time
date_range = pd.date_range(start=start_date, end=end_date, freq="D")

# convert to strings
dates = [d.strftime("%Y-%m-%d") for d in date_range]



# create a blank dataframe to add to
# Start with an empty DataFrame
taiwan_futures_institutional_investors = pd.DataFrame({
    "futures_id": pd.Series(dtype="string"),
    "date":pd.Series(dtype="datetime64[ns]"),  # dates like 2016-01-04
    "institutional_investors": pd.Series(dtype="string"),
    "long_deal_volume": pd.Series(dtype="float64"),
    "long_deal_amount": pd.Series(dtype="float64"),
    "short_deal_volume": pd.Series(dtype="float64"),
    "short_deal_amount": pd.Series(dtype="float64"),
    "long_open_interest_balance_volume": pd.Series(dtype="float64"),
    "long_open_interest_balance_amount": pd.Series(dtype="float64"),                                                                 
    "short_open_interest_balance_volume": pd.Series(dtype="float64"),
    "short_open_interest_balance_amount": pd.Series(dtype="float64")
})



for day in dates:

    # Rate limit the requests to avoid going over the limit (this will take 6 hours)
    time.sleep(2)


    try:
        
        one_day = api.taiwan_futures_institutional_investors(
                  start_date=day,
                  end_date=end_date)
        
        print(day)
        #print(one_day)
        
        if one_day.empty:
            print(f'Skipping {day}')
            
            
        else: 
           
            # add the day's results to the overall dataframe
            taiwan_futures_institutional_investors = pd.concat([taiwan_futures_institutional_investors, one_day], ignore_index=True)

    except:
        taiwan_futures_institutional_investors.to_csv('data/tsmc/taiwan_futures_institutional_investors.csv', index=False)
        break


taiwan_futures_institutional_investors.to_csv('data/tsmc/taiwan_futures_institutional_investors.csv', index=False)



