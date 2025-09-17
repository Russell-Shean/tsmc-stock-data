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

# Define time range (last 10 years)
end_date = datetime.date.today()

start_date = datetime.date(2016, 1, 1)


start_date=start_date.strftime("%Y-%m-%d")
end_date=end_date.strftime("%Y-%m-%d")

# Download daily closing price data ----------------------------------------------------------------------------------------------
tsm_daily_close  = api.taiwan_stock_daily(
                  stock_id=stock_id,
                   start_date=start_date,
                   end_date=end_date
)


tsm_daily_close.to_csv('data/tsmc/daily_closing_price.csv', index=False)

# Download weekly closing price data ----------------------------------------------------------------------------------------------

taiwan_stock_weekly = api.taiwan_stock_weekly(
    stock_id='2330',
    start_date='2020-04-02',
    end_date='2020-04-12'
)

taiwan_stock_weekly.to_csv('data/tsmc/taiwan_stock_weekly.csv', index=False)

# Download monthly closing price data ----------------------------------------------------------------------------------------------
tsm_monthly_close  = api.taiwan_stock_monthly(
                  stock_id=stock_id,
                   start_date=start_date,
                  end_date=end_date
)


tsm_monthly_close.to_csv('data/tsmc/monthly_closing_price.csv', index=False)


# Monthly revenue -----------------------------------------------------------------------------------------------------------------------
tsm_monthly_revenue = api.taiwan_stock_month_revenue(
        stock_id=stock_id,
        start_date=start_date,
        end_date=end_date
     )

tsm_monthly_revenue.to_csv('data/tsmc/monthly_revenue.csv', index=False)





time.sleep(1) 
# Institutional Buy and Sell ------------------------------------------------------------------------------------------------------------
institutional_buy_and_sell = api.taiwan_stock_institutional_investors(
        stock_id=stock_id,
        start_date=start_date,
        end_date=end_date
)


institutional_buy_and_sell.to_csv('data/tsmc/tsmc_institutional_buy_and_sell.csv', index=False)


# 台股八大行庫賣賣表	TaiwanstockGovernmentBankBuySell

#taiwan_stock_government_bank_buy_sell = api.taiwan_stock_government_bank_buy_sell(
    #stock_id=stock_id,
       # start_date=start_date #,
        #end_date=end_date
#)

#taiwan_stock_government_bank_buy_sell.to_csv('data/tsmc/taiwan_stock_government_bank_buy_sell.csv', index=False)

# 台灣大盤融資維持率	TaiwanTotalExchangeMarginMaintenance
taiwan_total_exchange_margin_maintenance = api.taiwan_total_exchange_margin_maintenance(
   start_date=start_date,
    end_date=end_date
)

taiwan_total_exchange_margin_maintenance.to_csv('data/tsmc/taiwan_total_exchange_margin_maintenance.csv', index=False)


# 期貨大額交易人未沖銷部位 	TaiwanFuturesOpenInterestLargeTraders -------------------------------------
taiwan_futures_open_interest_large_traders = api.taiwan_futures_open_interest_large_traders(
    futures_id='TJF',
    start_date=start_date,
    end_date=end_date,
)

taiwan_futures_open_interest_large_traders.to_csv('data/tsmc/taiwan_futures_open_interest_large_traders.csv', index=False)

time.sleep(1) 
# 外資持股表 	Taiwan Stock Shareholding -----------------------------------------

taiwan_stock_shareholding = api.taiwan_stock_shareholding(
    stock_id=stock_id,
    start_date=start_date,
    end_date=end_date
)

taiwan_stock_shareholding.to_csv('data/tsmc/taiwan_stock_shareholding.csv', index=False)



# 台灣個股十年線資料表 	TaiwanStock10Year ---------------------------------------------

TaiwanStock10Year = api.taiwan_stock_10year(
    stock_id=stock_id,
    start_date=start_date,
    end_date=end_date
 )

TaiwanStock10Year.to_csv('data/tsmc/taiwan_stock_10year.csv', index=False)



time.sleep(1) 
# 個股融資融劵表 	TaiwanStockMarginPurchaseShortSale ---------------------------------
taiwan_stock_margin_purchase_short_sale = api.taiwan_stock_margin_purchase_short_sale(
    stock_id=stock_id,
    start_date=start_date,
    end_date=end_date
)

taiwan_stock_margin_purchase_short_sale.to_csv('data/tsmc/taiwan_stock_margin_purchase_short_sale.csv', index=False)


time.sleep(1) 
# 台灣市場整體法人買賣表 	TaiwanStockTotalInstitutionalInvestors --------------------------------------------
taiwan_stock_institutional_investors = api.taiwan_stock_institutional_investors(
    stock_id=stock_id,
   start_date=start_date,
    end_date=end_date
)

taiwan_stock_institutional_investors.to_csv('data/tsmc/taiwan_stock_institutional_investors.csv', index=False)



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

taiwan_stock_daily.to_csv('data/tsmc/taiwan_stock_daily.csv', index=False)



# 台股週 K 資料表 	TaiwanStockWeekPrice
taiwan_stock_weekly = api.taiwan_stock_weekly(
     #stock_id=stock_id,
    start_date=start_date,
    end_date=end_date

)

taiwan_stock_weekly.to_csv('data/tsmc/taiwan_stock_weekly.csv', index=False)




# 台股月 K 資料表 	TaiwanStockMonthPrice
taiwan_stock_monthly = api.taiwan_stock_monthly(
     #stock_id=stock_id,
    start_date=start_date,
    end_date=end_date

)

taiwan_stock_monthly.to_csv('data/tsmc/taiwan_stock_monthly.csv', index=False)
