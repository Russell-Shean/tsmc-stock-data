import datetime
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from FinMind.data import DataLoader

# Initialize loader
api = DataLoader()

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

# Download daily closing price data ----------------------------------------------------------------------------------------------
#tsm_daily_close  = api.taiwan_stock_monthly(
  #                stock_id=stock_id,
  #                 start_date=start_date,
 #                  end_date=end_date
#)


#tsm_daily_close.to_csv('data/tsmc/monthly_closing_price.csv', index=False)


# Monthly revenue -----------------------------------------------------------------------------------------------------------------------
tsm_monthly_revenue = api.taiwan_stock_month_revenue(
        stock_id=stock_id,
        start_date=start_date,
        end_date=end_date
    )

tsm_monthly_revenue.to_csv('data/tsmc/monthly_revenue.csv', index=False)





# Institutional Buy and Sell ------------------------------------------------------------------------------------------------------------
institutional_buy_and_sell = api.taiwan_stock_institutional_investors(
        stock_id=stock_id,
        start_date=start_date,
        end_date=end_date
)


institutional_buy_and_sell.to_csv('data/tsmc/institutional_buy_and_sell.csv', index=False)


# 台股八大行庫賣賣表	TaiwanstockGovernmentBankBuySell

#taiwan_stock_government_bank_buy_sell = api.taiwan_stock_government_bank_buy_sell(
    #stock_id=stock_id,
#        start_date=start_date,
       # end_date=end_date
#)

#taiwan_stock_government_bank_buy_sell.to_csv('data/tsmc/taiwan_stock_government_bank_buy_sell.csv', index=False)

# 台灣大盤融資維持率	TaiwanTotalExchangeMarginMaintenance
#taiwan_total_exchange_margin_maintenance = api.taiwan_total_exchange_margin_maintenance(
#    start_date=start_date,
 #   end_date=end_date
#)

#taiwan_total_exchange_margin_maintenance.to_csv('data/tsmc/taiwan_total_exchange_margin_maintenance.csv', index=False)


# 期貨大額交易人未沖銷部位 	TaiwanFuturesOpenInterestLargeTraders -------------------------------------
#taiwan_futures_open_interest_large_traders = api.taiwan_futures_open_interest_large_traders(
    #futures_id='TJF',
    #start_date=start_date,
    #end_date=end_date,
#)

#taiwan_futures_open_interest_large_traders.to_csv('data/tsmc/taiwan_futures_open_interest_large_traders.csv', index=False)