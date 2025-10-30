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
stock_id = "2354"
stock_name = "Foxconn"


def download_data_individual_stock(stock_id, stock_name):

    # create a new folder for the stock if it doesn't already exist
    os.makedirs(f'data/{stock_name}', exist_ok=True)
    
    # Define time range (last 10 years)
    end_date = datetime.date.today()
    start_date = datetime.date(2016, 1, 1)
    
    start_date=start_date.strftime("%Y-%m-%d")
    end_date=end_date.strftime("%Y-%m-%d")
    
    # Download daily closing price data ----------------------------------------------------------------------------------------------
    stock_daily_close  = api.taiwan_stock_daily(
                  stock_id=stock_id,
                   start_date=start_date,
                   end_date=end_date)
    
    stock_daily_close.to_csv(f'data/{stock_name}/{stock_name}_daily_closing_price.csv', index=False)
    
    # Download weekly closing price data ----------------------------------------------------------------------------------------------
    stock_weekly_close = api.taiwan_stock_weekly(
    stock_id=stock_id,
    start_date='2020-04-02',
    end_date='2020-04-12')

    stock_weekly_close.to_csv(f'data/{stock_name}/{stock_name}_weekly_closing_price.csv', index=False)
    
    # Download monthly closing price data ----------------------------------------------------------------------------------------------
    stock_monthly_close  = api.taiwan_stock_monthly(
                  stock_id=stock_id,
                   start_date=start_date,
                  end_date=end_date)
    
    stock_monthly_close.to_csv(f'data/{stock_name}/{stock_name}_monthly_closing_price.csv', index=False)
    
    # Monthly revenue -----------------------------------------------------------------------------------------------------------------------
    stock_monthly_revenue = api.taiwan_stock_month_revenue(
        stock_id=stock_id,
        start_date=start_date,
        end_date=end_date)
    
    stock_monthly_revenue.to_csv(f'data/{stock_name}/{stock_name}_monthly_revenue.csv', index=False)
    
    # Institutional Buy and Sell ------------------------------------------------------------------------------------------------------------
    institutional_buy_and_sell = api.taiwan_stock_institutional_investors(
        stock_id=stock_id,
        start_date=start_date,
        end_date=end_date)
    
    institutional_buy_and_sell.to_csv(f'data/{stock_name}/{stock_name}_institutional_buy_and_sell.csv', index=False)
    
    taiwan_stock_shareholding = api.taiwan_stock_shareholding(
    stock_id=stock_id,
    start_date=start_date,
    end_date=end_date
    )
    
    taiwan_stock_shareholding.to_csv(f'data/{stock_name}/{stock_name}_taiwan_stock_shareholding.csv', index=False)
    
    # 台灣個股十年線資料表 	TaiwanStock10Year ---------------------------------------------
    TaiwanStock10Year = api.taiwan_stock_10year(
    stock_id=stock_id,
    start_date=start_date,
    end_date=end_date)
    
    TaiwanStock10Year.to_csv(f'data/{stock_name}/{stock_name}_taiwan_stock_10year.csv', index=False)
    
    time.sleep(1) 
    # 個股融資融劵表 	TaiwanStockMarginPurchaseShortSale ---------------------------------
    taiwan_stock_margin_purchase_short_sale = api.taiwan_stock_margin_purchase_short_sale(
    stock_id=stock_id,
    start_date=start_date,
    end_date=end_date)
    
    taiwan_stock_margin_purchase_short_sale.to_csv(f'data/{stock_name}/{stock_name}_taiwan_stock_margin_purchase_short_sale.csv', index=False)
    
    time.sleep(1) 
    
    # 台灣市場整體法人買賣表 	TaiwanStockTotalInstitutionalInvestors --------------------------------------------
    taiwan_stock_institutional_investors = api.taiwan_stock_institutional_investors(
    stock_id=stock_id,
   start_date=start_date,
    end_date=end_date)
    
    taiwan_stock_institutional_investors.to_csv(f'data/{stock_name}/{stock_name}_taiwan_stock_institutional_investors.csv', index=False)
    
    ##當日沖銷交易標的及成交量值 TaiwanStockDayTrading
    taiwan_stock_day_trading = api.taiwan_stock_day_trading(
    stock_id=stock_id,
    start_date=start_date,
    end_date=end_date)
    
    taiwan_stock_day_trading.to_csv(f'data/{stock_name}/{stock_name}_taiwan_stock_day_trading.csv', index=False)
    
    # 綜合損益表 TaiwanStockFinancialStatements
    taiwan_stock_financial_statement = api.taiwan_stock_financial_statement(
    stock_id=stock_id,
    start_date=start_date,
    end_date=end_date)
    
    taiwan_stock_financial_statement.to_csv(f'data/{stock_name}/{stock_name}_stock_financial_statement.csv', index=False)
    
    # 月營收表 TaiwanStockMonthRevenue
    taiwan_stock_month_revenue = api.taiwan_stock_month_revenue(
    stock_id=stock_id,
    start_date=start_date,
    end_date=end_date)
    
    taiwan_stock_month_revenue.to_csv(f'data/{stock_name}/{stock_name}_stock_month_revenue.csv', index=False)
    
    ## 法人買賣表 TaiwanStockInstitutionalInvestorsBuySell
    taiwan_stock_institutional_investors = api.taiwan_stock_institutional_investors(
    stock_id=stock_id,
    start_date=start_date,
    end_date=end_date)
    
    taiwan_stock_institutional_investors.to_csv(f'data/{stock_name}/{stock_name}_taiwan_stock_institutional_investors.csv', index=False)
    
    
    ## 個股PER、PBR資料表 TaiwanStockPER
    taiwan_stock_per_pbr = api.taiwan_stock_per_pbr(
    stock_id=stock_id,
    start_date=start_date,
    end_date=end_date)
    
    taiwan_stock_per_pbr.to_csv(f'data/{stock_name}/{stock_name}_taiwan_stock_per_pbr.csv', index=False)


download_data_individual_stock(stock_id=stock_id, stock_name=stock_name)