library(lubridate)


# Load total stock market price data
taiex_daily <- read.csv('data/tsmc/taiex_overal_daily_closing_price.csv')#|>
 # mutate(date = as.Date(date)) |>
  
  # add a month column
  mutate(month = month(date),
         year = year(date),
         month_year = paste0(month, "_", year)) |> 
  group_by(month_year) |>
  summarise(index_avg_price = mean(price))

# Load weights data
tsmc_weights <- read.csv("data/tsmc/tsmc_index_weight.csv") #|>
                mutate(date = as.Date(date)) |>
  
  # add a month column
mutate(month = month(date),
       year = year(date),
       month_year = paste0(month, "_", year)) 
  


# attach weights onto tenth of month stuff
strategy3 <- 
  tenth_of_month |> 
  left_join(tsmc_weights,
            by = c("month_year" = "month_year")) |>
  
  
  # calculate monthly return
  # fill in missing weights
  group_by(month_year) |>
  summarise(avg_monthly_price = mean(avg_monthly_price),
            date = min(date.x, na.rm = TRUE),
            avg_weight = mean(weight_per)) |>
  
  left_join(taiex_daily, 
            by = c("month_year" = "month_year"))  |>
  
  arrange(date) |>
  fill(avg_weight, .direction = "down") |>
  
  # Then fill up?
  fill(avg_weight, .direction = "up") |>
  
  # convert weight to percent
  
  
  # calculate other things 
  mutate(
    
    return_tsmc = (avg_monthly_price / lag(avg_monthly_price)) - 1,
    weight_lag = lag(avg_weight) / 100,  # convert to decimal and lag it
    contribution_tsmc = weight_lag * return_tsmc,  # in decimal (e.g., 0.012)
    
    # Optional: set a hypothetical index return for demo (e.g., 4% = 0.04)
    return_index = (index_avg_price / lag(index_avg_price)) - 1,
    
    # Share of index return explained by TSMC
    share_of_index_return = (contribution_tsmc / return_index) * 100
  )


# filter out data that is unreliable
strategy3_filtered <- strategy3 |>
                      filter(date > "2024-10-01")

# save data
write.csv(strategy3, "data/back_testing/strategy3.csv", row.names = FALSE)
