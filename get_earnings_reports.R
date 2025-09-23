library(rvest)
library(stringr)
library(lubridate)

# Get data from here: https://investor.tsmc.com/english/financial-calendar

page_html <- read_html("data/tsmc/earnings_announcements2.html")


content_block <- page_html |>
                 html_nodes("#block-tsmc-investor-theme-content")


current_event_dates <- content_block |>
                  html_nodes(".item-list") |> 
                  html_nodes(".atc_date_start")|>
                  html_text() |>
                  as.Date()


current_event_titles <- content_block |>
  html_nodes(".item-list") |> 
  html_nodes(".atc_title") |>
  html_text() |>
  str_remove_all("\r\n") |> 
  str_squish()



event_dates <- page_html |> 
                    # html_nodes("div.view-content:nth-child(2)") |> 
                    html_nodes(".datetime") |> 
                    html_text() |>
                    str_extract(".*(?=\\()") |> 
                    str_squish()  |>
                    mdy()


past_event_titles <- page_html |> 
 # html_nodes("div.view-content:nth-child(2)") |> 
  html_nodes(".views-field-field-event-title") |> 
  html_text()



df <- data.frame(event_date = event_dates,
                 event_title = c(current_event_titles, past_event_titles))



write.csv(df,
          "data/tsmc/tsmc_event_announcements.csv",
          row.names = FALSE)
                       







