# tsmc-stock-data
A collection of scripts for aggregating TSMC data

# Data in this Repository 
| Dataset | Description | Link | Spreadsheet Link | Code |
| :------- | :------: | :------: | :------: | -------: |
| 1. [GDP_CHG.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/GDP_CHG.csv) | US GDP - Change, Billions of Dollars  | https://fred.stlouisfed.org/series/GDP  | [Spreadsheet Row](https://docs.google.com/spreadsheets/d/14ejejpMYTp3udQ0Er5-YgOjPwka907MtyHEntYqLVvs/edit?pli=1&gid=0#gid=0&range=46:46) | N/A  |
| 2. [GDP_PC1.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/GDP_PC1.csv) | US GDP - Percent Change from 1 year ago  | https://fred.stlouisfed.org/series/GDP  | [Spreadsheet Row](https://docs.google.com/spreadsheets/d/14ejejpMYTp3udQ0Er5-YgOjPwka907MtyHEntYqLVvs/edit?pli=1&gid=0#gid=0&range=46:46) | N/A  |
| 3. [GDP_PCH.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/GDP_PCH.csv) | US GDP - Percent Change | https://fred.stlouisfed.org/series/GDP  | [Spreadsheet Row](https://docs.google.com/spreadsheets/d/14ejejpMYTp3udQ0Er5-YgOjPwka907MtyHEntYqLVvs/edit?pli=1&gid=0#gid=0&range=46:46) | N/A  |
| 4. [GDP.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/GDP.csv) | US GDP - Billions of Dollars | https://fred.stlouisfed.org/series/GDP  | [Spreadsheet Row](https://docs.google.com/spreadsheets/d/14ejejpMYTp3udQ0Er5-YgOjPwka907MtyHEntYqLVvs/edit?pli=1&gid=0#gid=0&range=46:46) | N/A  |
| 5. [ISM-pmi-pm.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/ISM-pmi-pm.csv) | US ISM/PMI  | https://db.nomics.world/ISM/pmi | [Spreadsheet Row](https://docs.google.com/spreadsheets/d/14ejejpMYTp3udQ0Er5-YgOjPwka907MtyHEntYqLVvs/edit?pli=1&gid=0#gid=0&range=44:44)  | N/A  |
| 6. [meetings_announcements.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/meetings_announcements.csv) | 法說會發佈日期	Earnings conference call (investor call) release date  | https://investor.tsmc.com/english/financial-calendar  | [Spreadsheet Row](https://docs.google.com/spreadsheets/d/14ejejpMYTp3udQ0Er5-YgOjPwka907MtyHEntYqLVvs/edit?pli=1&gid=0#gid=0&range=9:9)  | [code link](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/get_earnings_reports.R) |
| 7. [monthly_revenue.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/monthly_revenue.csv) | -  | -  | -  | -  |
| 8. [NAIM_Data-since-Inception_2025-09-03.xlsx](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/NAIM_Data-since-Inception_2025-09-03.xlsx) | -  | -  | -  | -  |
| 9. [nasdaq_daily_closing_price.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/nasdaq_daily_closing_price.csv) | -  | -  | -  | -  |
| 10. [nfci_data.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/nfci_data.csv) | -  | -  | -  | -  |
| 11. [PAYEMS_PC1.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/PAYEMS_PC1.csv) | -  | -  | -  | -  |
| 12. [PAYEMS_PCH.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/PAYEMS_PCH.csv) | -  | -  | -  | -  |
| 13. [PAYEMS.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/PAYEMS.csv) | -  | -  | -  | -  |
| 14. [PCE_PC1.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/PCE_PC1.csv) | -  | -  | -  | -  |
| 15. [PCE_PCH.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/PCE_PCH.csv) | -  | -  | -  | -  |
| 16. [PCE.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/PCE.csv) | -  | -  | -  | -  |
| 17. [SandP_daily_closing_price.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/SandP_daily_closing_price.csv) | -  | -  | -  | -  |
| 18. [sox_daily_closing_price.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/sox_daily_closing_price.csv) | -  | -  | -  | -  |
| 19. [taiwan_futures_daily.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_futures_daily.csv) | -  | -  | -  | -  |
| 20. [taiwan_futures_institutional_investors.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_futures_institutional_investors.csv) | -  | -  | -  | -  |
| 21. [taiwan_futures_open_interest_large_traders.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_futures_open_interest_large_traders.csv) | -  | -  | -  | -  |
| 22. [taiwan_stock_10year.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_10year.csv) | -  | -  | -  | -  |
| 23. [taiwan_stock_daily_closing_price.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_daily_closing_price.csv) | -  | -  | -  | -  |
| 24. [taiwan_stock_daily.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_daily.csv) | -  | -  | -  | -  |
| 25. [taiwan_stock_day_trading.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_day_trading.csv) | -  | -  | -  | -  |
| 26. [taiwan_stock_institutional_investors_total.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_institutional_investors_total.csv) | -  | -  | -  | -  |
| 27. [taiwan_stock_institutional_investors.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_institutional_investors.csv) | -  | -  | -  | -  |
| 28. [taiwan_stock_margin_purchase_short_sale.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_margin_purchase_short_sale.csv) | -  | -  | -  | -  |
| 29. [taiwan_stock_monthly_closing_price.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_monthly_closing_price.csv) | -  | -  | -  | -  |
| 30. [taiwan_stock_monthly_semiconductors.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_monthly_semiconductors.csv) | -  | -  | -  | -  |
| 31. [taiwan_stock_monthly_TAIEX.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_monthly_TAIEX.csv) | -  | -  | -  | -  | 
| 32. [taiwan_stock_monthly.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_monthly.csv) | -  | -  | -  | -  |
| 33. [taiwan_stock_shareholding.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_shareholding.csv) | -  | -  | -  | -  |
| 34. [taiwan_stock_weekly_closing_price.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_weekly_closing_price.csv) | -  | -  | -  | -  |
| 35. [taiwan_stock_weekly.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_weekly.csv) | -  | -  | -  | -  |
| 36. [taiwan_total_exchange_margin_maintenance.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_total_exchange_margin_maintenance.csv) | -  | -  | -  | -  |
| 37. [tsmc_daily_closing_price.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/tsmc_daily_closing_price.csv) | -  | -  | -  | -  |
| 38. [tsmc_event_announcements.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/tsmc_event_announcements.csv) | -  | -  | -  | -  |
| 39. [tsmc_institutional_buy_and_sell.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/tsmc_institutional_buy_and_sell.csv) | -  | -  | -  | -  |
| 40. [tsmc_monthly_closing_price.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/tsmc_monthly_closing_price.csv) | -  | -  | -  | -  |
| 41. [tsmc_monthly_revenue.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/tsmc_monthly_revenue.csv) | -  | -  | -  | -  |
| 42. [tsmc_stock_financial_statement.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/tsmc_stock_financial_statement.csv) | -  | -  | -  | -  |
| 43. [tsmc_stock_month_revenue.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/tsmc_stock_month_revenue.csv) | -  | -  | -  | -  |
| 44. [tsmc_taiwan_stock_institutional_investors.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/tsmc_taiwan_stock_institutional_investors.csv) | -  | -  | -  | -  |
| 45. [tsmc_taiwan_stock_per_pbr.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/tsmc_taiwan_stock_per_pbr.csv) | -  | -  | -  | -  |
| 46. [tsmc_tse.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/tsmc_tse.csv) | -  | -  | -  | -  |
| 47. [tsmc_weekly_closing_price.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/tsmc_weekly_closing_price.csv) | -  | -  | -  | -  |
| 48. [vix_daily_closing_price.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/vix_daily_closing_price.csv) | -  | -  | -  | -  |