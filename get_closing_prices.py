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


start_date = end_date - datetime.timedelta(days=365*10)


start_date=start_date.strftime("%Y-%m-%d")
end_date=end_date.strftime("%Y-%m-%d")

# Download daily closing price data
tsm_daily_close  = api.taiwan_stock_daily(
                  stock_id=stock_id,
                   start_date=start_date,
                   end_date=end_date
)


tsm_daily_close.to_csv('data/tsmc/closing_price.csv', index=False)


# Monthly revenue
tsm_monthly_revenue = api.taiwan_stock_month_revenue(
        stock_id=stock_id,
          start_date=start_date,
            end_date=end_date
    )

tsm_monthly_revenue.to_csv('data/tsmc/monthly_revenue.csv', index=False)


