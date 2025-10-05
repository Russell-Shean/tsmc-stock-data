# calculate gross margin
# Load required libraries
library(tidyr)
library(dplyr)



tsmc_stock_financial_statement <- read.csv('data/tsmc/tsmc_stock_financial_statement.csv')


tsmc_fs_wide <- tsmc_stock_financial_statement |>
  dplyr::select(date, stock_id, type, value) |>
  tidyr::pivot_wider(names_from = type, values_from = value) |> 
  
  # Create gross margin columns
  mutate(
    across(
      .cols = where(is.numeric) & !c("stock_id", "EPS", "Revenue"),
      .fns = ~ .x / Revenue,
      .names = "{.col}_gross_margin"
    )
  )


# Save the new calculate data to file
tsmc_fs_wide |> write.csv('data/tsmc/tsmc_stock_financial_statement_gross_margin.csv')