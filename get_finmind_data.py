import datetime
#import matplotlib
#matplotlib.use("Agg")
#import matplotlib.pyplot as plt
from FinMind.data import DataLoader
import time



# Initialize loader
api = DataLoader()

# Define stock ID for TSMC
stock_id = "2330"

# Define time range (last 10 years)
end_date = datetime.date.today()


start_date = end_date - datetime.timedelta(days=365*10)


start_date=start_date.strftime("%Y-%m-%d")
end_date=end_date.strftime("%Y-%m-%d")

# Download daily closing price data ----------------------------------------------------------------------------------------------
tsm_daily_close  = api.taiwan_stock_daily(
                  stock_id=stock_id,
                   start_date=start_date,
                   end_date=end_date
)


tsm_daily_close.to_csv('data/tsmc/daily_closing_price.csv', index=False)


# Monthly revenue -----------------------------------------------------------------------------------------------------------------------
#tsm_monthly_revenue = api.taiwan_stock_month_revenue(
 #       stock_id=stock_id,
  #      start_date=start_date,
   #     end_date=end_date
    # )

# tsm_monthly_revenue.to_csv('data/tsmc/monthly_revenue.csv', index=False)





time.sleep(1) 
# Institutional Buy and Sell ------------------------------------------------------------------------------------------------------------
institutional_buy_and_sell = api.taiwan_stock_institutional_investors(
        stock_id=stock_id,
        start_date=start_date,
        end_date=end_date
)


institutional_buy_and_sell.to_csv('data/tsmc/tsmc_institutional_buy_and_sell.csv', index=False)



time.sleep(1) 
# 外資持股表 	Taiwan Stock Shareholding -----------------------------------------

taiwan_stock_shareholding = api.taiwan_stock_shareholding(
    stock_id=stock_id,
    start_date=start_date,
    end_date=end_date
)

taiwan_stock_shareholding.to_csv('data/tsmc/taiwan_stock_shareholding.csv', index=False)



# 台灣個股十年線資料表 	TaiwanStock10Year ---------------------------------------------

#TaiwanStock10Year = api.taiwan_stock_10year(
 #   stock_id=stock_id,
  #  start_date=start_date,
   # end_date=end_date
 #)

#TaiwanStock10Year.to_csv('data/tsmc/taiwan_stock_10year.csv', index=False)



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
#taiwan_stock_institutional_investors = api.taiwan_stock_institutional_investors(
    #stock_id=stock_id,
 #   start_date=start_date,
  #  end_date=end_date
#)

#taiwan_stock_institutional_investors.to_csv('data/tsmc/taiwan_stock_institutional_investors.csv', index=False)


# 台灣股價資料表	TaiwanStockPrice
#taiwan_stock_daily = api.taiwan_stock_daily(
     #stock_id=stock_id,
  #  start_date=start_date,
  #  end_date=end_date

#)

#taiwan_stock_daily.to_csv('data/tsmc/taiwan_stock_daily.csv', index=False)


# 台股週 K 資料表 	TaiwanStockWeekPrice

taiwan_stock_weekly = api.taiwan_stock_monthly(
    stock_id=stock_id,
    start_date=start_date,
    end_date=end_date


)