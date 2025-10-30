import datetime

from FinMind.data import DataLoader
import time

from dotenv import load_dotenv
import os

load_dotenv()


# Load credentials from environment variables
API_KEY = os.environ["FINMIND_API_TOKEN"]




# Initialize loader
api = DataLoader()

# Login
api.login_by_token(api_token=API_KEY)

# Define stock ID for TSMC
stock_id = "2330"


# overall stock market

# 台灣大盤融資維持率	TaiwanTotalExchangeMarginMaintenance
taiwan_total_exchange_margin_maintenance = api.taiwan_total_exchange_margin_maintenance(
   start_date=start_date,
    end_date=end_date
)

taiwan_total_exchange_margin_maintenance.to_csv('data/tsmc/taiwan_total_exchange_margin_maintenance.csv', index=False)

# 期貨大額交易人未沖銷部位 	TaiwanFuturesOpenInterestLargeTraders -------------------------------------
taiwan_futures_open_interest_large_traders = api.taiwan_futures_open_interest_large_traders(
    futures_id='TX',
    start_date=start_date,
    end_date=end_date
)

taiwan_futures_open_interest_large_traders.to_csv('data/tsmc/taiwan_futures_open_interest_large_traders.csv', index=False)

time.sleep(1) 



# 台灣市場整體法人買賣表 	TaiwanStockTotalInstitutionalInvestors
taiwan_stock_institutional_investors_total = api.taiwan_stock_institutional_investors_total(
     #stock_id=stock_id,
    start_date=start_date,
    end_date=end_date

)

taiwan_stock_institutional_investors_total.to_csv('data/tsmc/taiwan_stock_institutional_investors_total.csv', index=False)



# 台灣股價資料表	TaiwanStockPrice
taiwan_stock_daily = api.taiwan_stock_daily(
     #stock_id=stock_id,
    start_date=start_date,
    end_date=end_date

)

taiwan_stock_daily.to_csv('data/tsmc/taiwan_stock_daily_closing_price.csv', index=False)



# 台股週 K 資料表 	TaiwanStockWeekPrice
taiwan_stock_weekly = api.taiwan_stock_weekly(
     #stock_id=stock_id,
    start_date=start_date,
    end_date=end_date

)

taiwan_stock_weekly.to_csv('data/tsmc/taiwan_stock_weekly_closing_price.csv', index=False)




# 台股月 K 資料表 	TaiwanStockMonthPrice
taiwan_stock_monthly = api.taiwan_stock_monthly(
     #stock_id=stock_id,
    start_date=start_date,
    end_date=end_date

)

taiwan_stock_monthly.to_csv('data/tsmc/taiwan_stock_monthly_closing_price.csv', index=False)



## 期貨日成交資訊 TaiwanFuturesDaily
taiwan_futures_daily = api.taiwan_futures_daily(
    futures_id='CDF',
    start_date=start_date,
    end_date=end_date
)




taiwan_futures_daily.to_csv('data/tsmc/taiwan_futures_daily.csv', index=False)


# 外資持股表 	Taiwan Stock Shareholding -----------------------------------------


## 加權指數 TaiwanVariousIndicators5Seconds

# See separate file...


## 台股月 K 資料表 TaiwanStockMonthPrice

# filter for TAIEX
taiwan_stock_monthly_TAIEX = api.taiwan_stock_monthly(
    stock_id="TAIEX",
    start_date=start_date,
    end_date=end_date
)

taiwan_stock_monthly_TAIEX.to_csv('data/tsmc/taiwan_stock_monthly_TAIEX.csv', index=False)



# and Semiconductor

taiwan_stock_monthly_semiconductors = api.taiwan_stock_monthly(
    stock_id="Semiconductor",
    start_date=start_date,
    end_date=end_date
)

taiwan_stock_monthly_semiconductors.to_csv('data/tsmc/taiwan_stock_monthly_semiconductors.csv', index=False)



# Strategy 4 data



#tsmc = dl.taiwan_stock_daily(stock_id="2330", start_date=start_date )
tsmc_stock_weight_total_index = api.taiwan_stock_market_value_weight(
    stock_id=stock_id,
    start_date="2024-10-30",
    end_date=end_date
)


# Download daily closing price data ----------------------------------------------------------------------------------------------
stock_daily_close  = api.taiwan_stock_daily(
                  stock_id=stock_id,
                   start_date=start_date,
                   end_date=end_date
)

tsmc_stock_weight_total_index.to_csv('data/{stock_name}/{stock_name}_index_weight.csv', index=False)


# Step 2: Pull TAIEX data
df = api.taiwan_stock_total_return_index(
    index_id="TAIEX",
    start_date=start_date,
    end_date=end_date
)

df.to_csv('data/tsmc/taiex_overal_daily_closing_price.csv' , 
           index=False)

