# calculate gross margin
# Load required libraries
library(tidyr)
library(dplyr)



tsmc_stock_financial_statement <- read.csv('data/tsmc/tsmc_stock_financial_statement.csv')


tsmc_fs_wide <- tsmc_stock_financial_statement %>%
  select(date, stock_id, type, value) |>
  tidyr::pivot_wider(names_from = type, values_from = value) #|> 
   #mutate(gross_margin = )
