# strategy 2
library(lubridate)
library(dplyr)


only_thursdays <- tsmc_daily_closing |> 
  filter(wday(date) == 4 ) |>
  select(week_start,
         week_end,
         thursday_close = close)


strategy2 <- tsmc_daily_closing |> 
   group_by(week_start) |> 
   summarise(week_max = max(close),
             week_min = min(close),
             week_avg = mean(close)) |>
   left_join(only_thursdays)


write.csv(strategy2,
          "data/back_testing/strategy2.csv",
          row.names = FALSE)
