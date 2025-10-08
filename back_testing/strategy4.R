library(ggplot2)


tsmc_daily_closing |> mutate(alltime_max = cummax(close),
                             alltime_min = cummin(close)) |> View()



tsmc_daily_closing |> 
  ggplot2::ggplot(aes(x=date, y=close, group = 1)) +
  geom_line(col= "blue") +
 # geom_point(alpha = 0.3) 
  labs(title = "Daily Closing Price of TSMC - 2016 to Today",
       x = "Date",
       Y = "Daily Closing Price")
