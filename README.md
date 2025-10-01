# tsmc-stock-data
A collection of scripts for aggregating TSMC data

# Data in this Repository 
| Dataset | Description | Link | Code |
| :------- | :------: | :------: | -------: |
| 1. [closing_price_monthly.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/closing_price_monthly.csv) | 股價收盤價 (日) Closing stock price  | https://finmind.github.io/tutor/TaiwanMarket/Technical/#taiwanstockprice  | ``` tsm_daily_close  = api.taiwan_stock_daily(
                  stock_id=stock_id,
                   start_date=start_date,
                   end_date=end_date
)


tsm_daily_close.to_csv('data/tsmc/daily_closing_price.csv', index=False) ``` |          
| 3. [daily_closing_price.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/daily_closing_price.csv) | -  | -  | -  |
| 4. [day_trade.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/day_trade.csv) | -  | -  | -  |
| 5. [earnings_announcements.html](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/earnings_announcements.html) | -  | -  | -  |
| 6. [earnings_announcements2.html](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/earnings_announcements2.html) | -  | -  | -  |
| 7. [GDP_CHG.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/GDP_CHG.csv) | -  | -  | -  |
| 8. [GDP_PC1.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/GDP_PC1.csv) | -  | -  | -  |
| 9. [GDP_PCH.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/GDP_PCH.csv) | -  | -  | -  |
| 10. [GDP.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/GDP.csv) | -  | -  | -  |
| 11. [gross_margin_quarterly.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/gross_margin_quarterly.csv) | -  | -  | -  |
| 12. [institutional_buy_and_sell.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/institutional_buy_and_sell.csv) | -  | -  | -  |
| 13. [ISM-pmi-pm.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/ISM-pmi-pm.csv) | -  | -  | -  |
| 14. [meetings_announcements.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/meetings_announcements.csv) | -  | -  | -  |
| 15. [monthly_closing_price.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/monthly_closing_price.csv) | -  | -  | -  |
| 16. [monthly_revenue_announcement.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/monthly_revenue_announcement.csv) | -  | -  | -  |
| 17. [monthly_revenue.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/monthly_revenue.csv) | -  | -  | -  |
| 18. [NAIM_Data-since-Inception_2025-09-03.xlsx](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/NAIM_Data-since-Inception_2025-09-03.xlsx) | -  | -  | -  |
| 19. [nasdaq_daily_closing_price.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/nasdaq_daily_closing_price.csv) | -  | -  | -  |
| 20. [nfci_data.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/nfci_data.csv) | -  | -  | -  |
| 21. [PAYEMS_PC1.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/PAYEMS_PC1.csv) | -  | -  | -  |
| 22. [PAYEMS_PCH.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/PAYEMS_PCH.csv) | -  | -  | -  |
| 23. [PAYEMS.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/PAYEMS.csv) | -  | -  | -  |
| 24. [PCE_PC1.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/PCE_PC1.csv) | -  | -  | -  |
| 25. [PCE_PCH.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/PCE_PCH.csv) | -  | -  | -  |
| 26. [PCE.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/PCE.csv) | -  | -  | -  |
| 27. [PE_YR_PB.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/PE_YR_PB.csv) | -  | -  | -  |
| 28. [SandP_daily_closing_price.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/SandP_daily_closing_price.csv) | -  | -  | -  |
| 29. [sox_daily_closing_price.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/sox_daily_closing_price.csv) | -  | -  | -  |
| 30. [taiwan_futures_daily.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_futures_daily.csv) | -  | -  | -  |
| 31. [taiwan_futures_institutional_investors.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_futures_institutional_investors.csv) | -  | -  | -  |
| 32. [taiwan_futures_open_interest_large_traders.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_futures_open_interest_large_traders.csv) | -  | -  | -  |
| 33. [taiwan_stock_10year.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_10year.csv) | -  | -  | -  |
| 34. [taiwan_stock_daily.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_daily.csv) | -  | -  | -  |
| 35. [taiwan_stock_day_trading.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_day_trading.csv) | -  | -  | -  |
| 36. [taiwan_stock_institutional_investors_total.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_institutional_investors_total.csv) | -  | -  | -  |
| 37. [taiwan_stock_institutional_investors.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_institutional_investors.csv) | -  | -  | -  |
| 38. [taiwan_stock_margin_purchase_short_sale.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_margin_purchase_short_sale.csv) | -  | -  | -  |
| 39. [taiwan_stock_monthly_semiconductors.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_monthly_semiconductors.csv) | -  | -  | -  |
| 40. [taiwan_stock_monthly_TAIEX.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_monthly_TAIEX.csv) | -  | -  | -  |
| 41. [taiwan_stock_monthly.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_monthly.csv) | -  | -  | -  |
| 42. [taiwan_stock_shareholding.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_shareholding.csv) | -  | -  | -  |
| 43. [taiwan_stock_weekly.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_weekly.csv) | -  | -  | -  |
| 44. [taiwan_total_exchange_margin_maintenance.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_total_exchange_margin_maintenance.csv) | -  | -  | -  |
| 45. [tsmc_event_announcements.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/tsmc_event_announcements.csv) | -  | -  | -  |
| 46. [tsmc_institutional_buy_and_sell.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/tsmc_institutional_buy_and_sell.csv) | -  | -  | -  |
| 47. [tsmc_stock_financial_statement.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/tsmc_stock_financial_statement.csv) | -  | -  | -  |
| 48. [tsmc_stock_month_revenue.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/tsmc_stock_month_revenue.csv) | -  | -  | -  |
| 49. [tsmc_taiwan_stock_institutional_investors.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/tsmc_taiwan_stock_institutional_investors.csv) | -  | -  | -  |
| 50. [tsmc_taiwan_stock_per_pbr.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/tsmc_taiwan_stock_per_pbr.csv) | -  | -  | -  |
| 51. [tsmc_tse.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/tsmc_tse.csv) | -  | -  | -  |
| 52. [vix_daily_closing_price.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/vix_daily_closing_price.csv) | -  | -  | -  |
