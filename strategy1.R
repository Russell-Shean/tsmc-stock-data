# load data
library(lubridate)
library(dplyr)
library(tidyr)


tsmc_daily_closing <- read.csv("data/tsmc/tsmc_daily_closing_price.csv")

tsmc_daily_closing <- tsmc_daily_closing |>
  mutate(date = as.Date(date)) |>
  arrange(date) |>

  

  mutate(
         
         
         # offset the values by one so that the rolling avg
         # doesn't include the tenth
         closing_price_offset = lead(close, 1)) |>
  
  mutate(
    avg_closing_next5 = zoo::rollapply(closing_price_offset,
                                       width = 5, 
                                       align = "left", 
                                       FUN = mean,
                                       fill = NA)
  )


# After we've calculated averages for trading days
# we can fill in missing values

# Add missing dates into the dateframe
# we are going to assume that on the days the market aren't open
# i.e. sunday, the stock price will be the same as the price on the day
# the market was open last (ie. friday)

# This adds in missing dates
tsmc_daily_closing <- tsmc_daily_closing |>
                         tidyr::complete(date = seq(min(date), 
                                                    max(date),
                                                    by = "1 day")) |>
  
  arrange(date) |>
  
  # This uses previous values
  fill(everything(), .direction = "down")  |>
  
  # add day of week
  mutate(day_of_week = wday(date,
                            label = TRUE),
         
         # add row number
         row_number = row_number())

# find the tenth of each month
tenth_of_month <- tsmc_daily_closing |> 
                  filter(day(date) == 10) |>
                  arrange(date) |> 
                  mutate(one_month_later = NA,
                         two_months_later = NA,
                         three_months_later = NA)


# find fifthenth of each month
fifteenth_of_month <- tsmc_daily_closing |> 
  filter(day(date) == 15)|>
  arrange(date)


for(i in 1:nrow(tenth_of_month)){
  
  ith_date <- tenth_of_month[i,"date"]
  
  # find the next three fiftenths of the month
  next_3_dates <- fifteenth_of_month |>
                  filter(date > ith_date) |>
                  arrange(date) |>
                  slice_head(n=3)
  
  tenth_of_month[i,"one_month_later"] <- next_3_dates[1,"close"]
  tenth_of_month[i,"two_months_later"] <- next_3_dates[2,"close"]
  tenth_of_month[i,"three_months_later"] <- next_3_dates[3,"close"]
  
}
