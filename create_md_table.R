data_files <- list.files("data/tsmc") 

  
"https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/GDP.csv"


paste0("| ",
       1:length(data_files), 
       ". [", 
       data_files,
       "](https://github.com/Russell-Shean/tsmc-stock-data/blob/main/data/tsmc/", 
       data_files,
       ") | -  | -  | -  |\n") |> cat()


# chafs