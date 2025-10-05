library(ggplot2)

tsmc_daily <- read.csv('data/tsmc/tsmc_daily_closing_price.csv')


tsmc_daily |> ggplot() + geom_point(aes(x = date, y= close))


Taiex_daily <- read.csv('data/tsmc/tsmc_daily_closing_price.csv')