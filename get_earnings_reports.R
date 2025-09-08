library(rvest)

page_html <- read_html("/home/russ/Documents/simon_projects/tsmc-stock-data/data/tsmc/earnings_announcements.html")


content_block <- page_html |>
                 html_nodes("#block-tsmc-investor-theme-content")


event_starts <- current_events <- content_block |>
                  html_nodes(".item-list") |> 
                  html_nodes(".atc_date_start")|>
                  html_text()


event_name <- current_events <- content_block |>
  html_nodes(".item-list") |> 
  html_nodes(".atc_title") |>
  html_text()


upcoming_events <- data.frame(date = event_starts,
                              event = event_name)



past_event_dates <- page_html |> 
                    html_nodes("div.view-content:nth-child(2)") |> 
                    html_nodes(".datetime") |> 
                    html_text()


past_event_titles <- page_html |> 
  html_nodes("div.view-content:nth-child(2)") |> 
  html_nodes(".views-field-field-event-title") |> 
  html_text()


                       







