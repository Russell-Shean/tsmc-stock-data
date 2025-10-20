# strategy 2
library(lubridate)
library(dplyr)


only_thursdays <- tsmc_daily_closing |> 
  filter(wday(date) == 4 ) |>
  select(week_start,
         week_end,
         thursday_close = close)

only_fridays <- tsmc_daily_closing |> 
  filter(wday(date) == 5 ) |>
  select(week_start,
         week_end,
         friday_close = close)


strategy2 <- tsmc_daily_closing |> 
   group_by(week_start) |> 
   summarise(week_max = max(close),
             week_min = min(close),
             week_avg = mean(close)) |>
   left_join(only_thursdays) |>
  left_join(only_fridays) |>
  mutate(week_avg_return_rate = (thursday_close - week_avg) / thursday_close,
         thurs_fri_return_rate = (thursday_close - friday_close) / thursday_close ) #|>
  #mutate(positive_return = ifelse(return_rate > 0,
   #                               "Yes", 
   #                               "No"))


#strategy2 |> 
 # count(positive_return)


#strategy2 |> pull(return_rate) |> sum(na.rm = TRUE)

write.csv(strategy2,
          "data/back_testing/strategy2.csv",
          row.names = FALSE)
