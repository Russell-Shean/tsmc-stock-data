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


##  期貨三大法人買賣 TaiwanFuturesInstitutionalInvestors
taiwan_futures_institutional_investors = api.taiwan_futures_institutional_investors(
     #stock_id=stock_id,
    start_date=start_date,
    end_date=end_date

)

taiwan_futures_institutional_investors.to_csv('data/tsmc/taiwan_futures_institutional_investors.csv', index=False)
