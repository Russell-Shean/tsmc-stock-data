## 台股月 K 資料表 TaiwanStockMonthPrice

# filter for TAIEX
# and Semiconductor


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

##  期貨三大法人買賣 TaiwanFuturesInstitutionalInvestors
taiwan_futures_institutional_investors = api.taiwan_futures_institutional_investors(
     #stock_id=stock_id,
    start_date="2018-06-05",
    end_date=end_date

)

print(taiwan_futures_institutional_investors)

taiwan_futures_institutional_investors.to_csv('data/tsmc/taiwan_futures_institutional_investors.csv', index=False)


