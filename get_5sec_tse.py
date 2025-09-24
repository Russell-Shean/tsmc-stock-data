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

start_date = datetime.date(2016, 1, 1)


start_date=start_date.strftime("%Y-%m-%d")
end_date=end_date.strftime("%Y-%m-%d")

# Create a range of dates for loop through
# because some of the endpoints only return single days at a time
date_range = pd.date_range(start=start_date, end=end_date, freq="D")

# convert to strings
dates = [d.strftime("%Y-%m-%d") for d in date_range]

## 加權指數 TaiwanVariousIndicators5Seconds

# create a blank dataframe to add to
# Start with an empty DataFrame
tsmc_tse = pd.DataFrame({
    "date": pd.Series(dtype="datetime64[ns]"),  # dates like 2016-01-04
    "time": pd.Series(dtype="string"),          # times like "13:30:00"
    "TAIEX": pd.Series(dtype="float64")         # numeric index values
})



for day in dates:

    # Rate limit the requests to avoid going over the limit (this will take 6 hours)
    time.sleep(2)


    try:
        
        tse = api.tse(
                  date=day)
        
        if tse.empty:
            print(f'Skipping {day}')
            
            
        else: 
            # make sure that date is recognized as date time
            tse['date'] = pd.to_datetime(tse['date'])
            
            # create separate date and time columns
            tse['time'] = tse['date'].dt.time
            tse['date'] = tse['date'].dt.date
            
            # filter tse to only include the tse value at market close
            market_close_tse = tse[tse['time'] == datetime.time(13, 30, 0)]
            
            # rearange columns
            market_close_tse = market_close_tse[["date", "time", "TAIEX"]]
            
            # add the day's results to the overall dataframe
            tsmc_tse = pd.concat([tsmc_tse, market_close_tse], ignore_index=True)

    except:
        tsmc_tse.to_csv('data/tsmc/tsmc_tse.csv', index=False)
        break



##當日沖銷交易標的及成交量值 TaiwanStockDayTrading
'''

taiwan_stock_day_trading = api.taiwan_stock_day_trading(
    stock_id='2330',
    start_date=start_date,
    end_date=end_date
)



print(taiwan_stock_day_trading)

taiwan_stock_day_trading.to_csv('data/tsmc/taiwan_stock_day_trading.csv', index=False)

'''