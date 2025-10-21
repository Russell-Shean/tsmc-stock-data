# strategy 3

library(ggplot2)
library(dplyr)
library(purrr)
library(ggrepel)

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


#troughs <- pullbacks |>
 # select(trough_date,
    #     trough_price,
     #    retracement_pct)


# Reattach pullbacks onto strategy 4
strategy4 <- tsmc_daily_closing |>
  left_join(peaks, by = c("date" = "peak_date")) |>
#  left_join(troughs, by = c("date" = "trough_date"))
  arrange(date)
  
# create date pairs
highs_date_pairs <- data.frame(first_high = lag(peaks$peak_date),
                               second_high = peaks$peak_date) |>
   
  # Filter out first entry (which doesn't have a date before it)
  filter(!is.na(first_high))

# loop through the high pairs
# find the lowest value between the two pairs

all_local_mins <- data.frame()

for(i in 1:nrow(highs_date_pairs)){
  
  print(i)
  
  local_min <- strategy4 |>
    
    # filter to find the section between the two highs 
    filter(date >= highs_date_pairs[i, "first_high"] & 
           date <= highs_date_pairs[i, "second_high"]) |>
    
    # filter to find the lowest closing price between the two highs
    filter(close == min(close)) |>
    
    select(date,
           trough_price = close)
  
  print(local_min)
  
  
  
  # Collect the result
  all_local_mins <- bind_rows(all_local_mins, local_min)
 

}

# attach the local min back to the dataframe
strategy4 <- strategy4 |>
  left_join(all_local_mins)



# re-create a pullbacks dataframe
pullbacks <- strategy4 |>
             filter(!is.na(peak_price) |
                    !is.na(trough_price)) |>

             # select only what we need 
             select(date,
                    peak_price,
                    trough_price)


# stuff from chatgpt, too lazy to clean lol
# Step 1: Separate peaks and troughs
peaks <- pullbacks %>%
  filter(!is.na(peak_price)) %>%
  select(peak_date = date, peak_price)

troughs <- pullbacks %>%
  filter(!is.na(trough_price)) %>%
  select(trough_date = date, trough_price)

# Step 2: Pair each peak with the next available trough
# (Assumes every peak is followed by a trough)
n_pairs <- min(nrow(peaks), nrow(troughs))

pullbacks2 <- tibble(
  peak_date   = peaks$peak_date[1:n_pairs],
  peak_price  = peaks$peak_price[1:n_pairs],
  trough_date = troughs$trough_date[1:n_pairs],
  trough_price = troughs$trough_price[1:n_pairs]
) |>
  # calculate retracement percent
  mutate(retracement_pct = round((peak_price - trough_price) / peak_price * 100, 2)) 


# add retracement onto strategy4 df
retracements <- pullbacks2 |>
                select(date = trough_date,
                       retracement_pct)


strategy4 <- strategy4 |> 
             left_join(retracements)



# save results 
write.csv(pullbacks2,
          "data/back_testing/strategy4_pullbacks.csv")


write.csv(strategy4,
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
  
  # label retracement percentages
  geom_text_repel(
    data = filter(strategy4, !is.na(trough_price)),
    aes(x = date, y = close, label = paste0(retracement_pct, "%")),
    size = 3,         # adjust as needed
    color = "black",  # optional
    box.padding = 0.5,
    #point.padding = 75,
    segment.color = "red",
    segment.alpha = 0.5,
    segment.linetype = "dashed",
    nudge_y = 400,
    max.overlaps = Inf,
    min.segment.length = 0
  ) +
  

  # geom_point(alpha = 0.3) 
  labs(title = "Daily Closing Price of TSMC - 2016 to Today\nGreen dots are peaks\nRed dots are troughs",
       x = "Date",
       y = "Daily Closing Price")



