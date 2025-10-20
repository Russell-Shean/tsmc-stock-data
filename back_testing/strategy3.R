# strategy 3

library(ggplot2)
library(dplyr)

# N = lookback window for rolling high
# d = minimum drawdown threshold

find_pullbacks_after_new_high <- function(df,
                                          price_col = "close", 
                                          N = 252, 
                                          d = 0.05) {
  
  # Ensure data is arranged by date
  df <- df %>%
    arrange(date)
  
  # Create rolling max (excluding current day)
  df <- df %>%
    mutate(
      rollmax_prev = lag(rollapplyr(.data[[price_col]], 
                                    width = N, 
                                    FUN = max, 
                                    fill = NA, 
                                    align = "right"))
    )
  
  # Initialize state variables
  in_leg <- FALSE
  peak <- NA
  trough <- NA
  peak_date <- NA
  trough_date <- NA
  events <- list()
  
  for (i in 1:nrow(df)) {
    row <- df[i, ]
    px <- row[[price_col]]
    date <- row$date
    rollmax_val <- row$rollmax_prev
    
    new_high <- !is.na(rollmax_val) && px > rollmax_val
    
    if (!in_leg) {
      if (new_high) {
        in_leg <- TRUE
        peak <- px
        peak_date <- date
        trough <- px
        trough_date <- date
      }
    } else {
      if (px >= peak) {
        peak <- px
        peak_date <- date
        trough <- px
        trough_date <- date
      } else {
        if (px < trough) {
          trough <- px
          trough_date <- date
        }
        drawdown <- (peak - px) / peak
        if (drawdown >= d) {
          retracement_pct <- round((peak - trough) / peak * 100, 2)
          events[[length(events) + 1]] <- tibble(
            peak_date = peak_date,
            peak_price = peak,
            trough_date = trough_date,
            trough_price = trough,
            retracement_pct = retracement_pct
          )
          in_leg <- FALSE
        }
      }
    }
  }
  
  # Combine list of tibbles into a single tibble
  if (length(events) > 0) {
    result <- bind_rows(events)
  } else {
    result <- tibble()
  }
  
  return(result)
}




# Run the pullback finder
pullbacks <- find_pullbacks_after_new_high(tsmc_daily_closing, 
                                           price_col = "close",
                                           N = 252, 
                                           d = 0.05)

# separate into to dfs for merging
peaks <- pullbacks |>
         select(peak_date,
                peak_price)


troughs <- pullbacks |>
            select(trough_date,
                   trough_price,
                   retracement_pct)


# Reattach pullbacks onto strategy 4
strategy4 <- tsmc_daily_closing |>
             left_join(peaks, by = c("date" = "peak_date")) |>
             left_join(troughs, by = c("date" = "trough_date"))

# save results
write.csv(pullbacks,
          "data/back_testing/strategy4_pullbacks.csv")

write.csv(pullbacks,
          "data/back_testing/strategy4_full_data.csv")


# create graph
  ggplot2::ggplot() +
  geom_line(data = strategy4,
            aes(x=date, 
                y=close, 
                group = 1), 
            col= "black") +
  geom_point(data = filter(strategy4,
                           !is.na(peak_price)),
             aes(x=date, 
                 y=close),
             col = "green") +
    geom_point(data = filter(strategy4,
                             !is.na(trough_price)),
               aes(x=date, 
                   y=close),
               col = "red") +
  # geom_point(alpha = 0.3) 
  labs(title = "Daily Closing Price of TSMC - 2016 to Today\nGreen dots are peaks\nRed dots are troughs",
       x = "Date",
       Y = "Daily Closing Price")



