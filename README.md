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
| 6. [meetings_announcements.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/meetings_announcements.csv) | 法說會發佈日期	Earnings conference call (investor call) release date  | https://investor.tsmc.com/english/financial-calendar  |  |
| 7. [NAIM_Data.xlsx](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/NAIM_Data-since-Inception_2025-09-03.xlsx) | NAAIM 經理人持倉指數	NAAIM Exposure Index (National Association of Active Investment Managers’ exposure index) | https://naaim.org/programs/naaim-exposure-index/ | [Spreadsheet Row](https://docs.google.com/spreadsheets/d/14ejejpMYTp3udQ0Er5-Y| N/A |
| 8. [nasdaq_daily_closing_price.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/nasdaq_daily_closing_price.csv) | 納斯達克指數	Nasdaq Index | https://ranaroussi.github.io/yfinance/ | [Spreadsheet Row](https://docs.google.com/spreadsheets/d/14ejejpMYTp3udQ0Er5-YgOjPwka907MtyHEntYqLVvs/edit?pli=1&gid=0#gid=0&range=33:33)  | [code link](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/get_yfinance_Data.py) |
| 9. [nfci_data.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/nfci_data.csv) |  NAAIM 經理人持倉指數	NAAIM Exposure Index (National Association of Active Investment Managers’ exposure index) | fred.stlouisfed.org/docs/api/fred/  | [Spreadsheet Row](https://docs.google.com/spreadsheets/d/14ejejpMYTp3udQ0Er5-YgOjPwka907MtyHEntYqLVvs/edit?pli=1&gid=0#gid=0&range=43:43)  | [code link](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/get_fed_api_data.py) |

| 10. [PAYEMS_PC1.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/PAYEMS_PC1.csv) | -  | -  | -  | -  |
| 11. [PAYEMS_PCH.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/PAYEMS_PCH.csv) | -  | -  | -  | -  |
| 12. [PAYEMS.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/PAYEMS.csv) | -  | -  | -  | -  |
| 13. [PCE_PC1.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/PCE_PC1.csv) | -  | -  | -  | -  |
| 14. [PCE_PCH.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/PCE_PCH.csv) | -  | -  | -  | -  |
| 15. [PCE.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/PCE.csv) | -  | -  | -  | -  |
| 16. [SandP_daily_closing_price.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/SandP_daily_closing_price.csv) | -  | -  | -  | -  |
| 17. [sox_daily_closing_price.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/sox_daily_closing_price.csv) | -  | -  | -  | -  |
| 18. [taiwan_futures_daily.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_futures_daily.csv) | -  | -  | -  | -  |
| 19. [taiwan_futures_institutional_investors.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_futures_institutional_investors.csv) | -  | -  | -  | -  |
| 20. [taiwan_futures_open_interest_large_traders.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_futures_open_interest_large_traders.csv) | -  | -  | -  | -  |
| 21. [taiwan_stock_10year.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_10year.csv) | -  | -  | -  | -  |
| 22. [taiwan_stock_daily_closing_price.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_daily_closing_price.csv) | -  | -  | -  | -  |
| 23. [taiwan_stock_daily.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_daily.csv) | -  | -  | -  | -  |
| 24. [taiwan_stock_day_trading.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_day_trading.csv) | -  | -  | -  | -  |
| 25. [taiwan_stock_institutional_investors_total.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_institutional_investors_total.csv) | -  | -  | -  | -  |
| 26. [taiwan_stock_institutional_investors.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_institutional_investors.csv) | -  | -  | -  | -  |
| 27. [taiwan_stock_margin_purchase_short_sale.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_margin_purchase_short_sale.csv) | -  | -  | -  | -  |
| 28. [taiwan_stock_monthly_closing_price.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_monthly_closing_price.csv) | -  | -  | -  | -  |
| 29. [taiwan_stock_monthly_semiconductors.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_monthly_semiconductors.csv) | -  | -  | -  | -  |
| 30. [taiwan_stock_monthly_TAIEX.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_monthly_TAIEX.csv) | -  | -  | -  | -  | 
| 31. [taiwan_stock_monthly.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_monthly.csv) | -  | -  | -  | -  |
| 32. [taiwan_stock_shareholding.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_shareholding.csv) | -  | -  | -  | -  |
| 33. [taiwan_stock_weekly_closing_price.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_weekly_closing_price.csv) | -  | -  | -  | -  |
| 34. [taiwan_stock_weekly.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_stock_weekly.csv) | -  | -  | -  | -  |
| 35. [taiwan_total_exchange_margin_maintenance.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/taiwan_total_exchange_margin_maintenance.csv) | -  | -  | -  | -  |
| 36. [tsmc_daily_closing_price.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/tsmc_daily_closing_price.csv) | -  | -  | -  | -  |
| 37. [tsmc_event_announcements.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/tsmc_event_announcements.csv) | -  | -  | -  | -  |
| 38. [tsmc_institutional_buy_and_sell.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/tsmc_institutional_buy_and_sell.csv) | -  | -  | -  | -  |
| 39. [tsmc_monthly_closing_price.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/tsmc_monthly_closing_price.csv) | -  | -  | -  | -  |
| 40. [tsmc_monthly_revenue.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/tsmc_monthly_revenue.csv) | -  | -  | -  | -  |
| 41. [tsmc_stock_financial_statement.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/tsmc_stock_financial_statement.csv) | -  | -  | -  | -  |
| 42. [tsmc_stock_month_revenue.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/tsmc_stock_month_revenue.csv) | -  | -  | -  | -  |
| 43. [tsmc_taiwan_stock_institutional_investors.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/tsmc_taiwan_stock_institutional_investors.csv) | -  | -  | -  | -  |
| 44. [tsmc_taiwan_stock_per_pbr.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/tsmc_taiwan_stock_per_pbr.csv) | -  | -  | -  | -  |
| 45. [tsmc_tse.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/tsmc_tse.csv) | -  | -  | -  | -  |
| 46. [tsmc_weekly_closing_price.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/tsmc_weekly_closing_price.csv) | -  | -  | -  | -  |
| 47. [vix_daily_closing_price.csv](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/vix_daily_closing_price.csv) | -  | -  | -  | -  |