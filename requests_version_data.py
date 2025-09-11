import requests
import csv
import pandas as pd


def get_data_requests(base_url, endpoint, output_file, filter_column = None, filter_value=None):
    
    
    # Define the base URL and endpoint
    url = f"{base_url}{endpoint}"
    

    
    
    try:
        # Send GET request
        response = requests.get(url)
        
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            print(f"Received {len(data)} records.\n")
            
            
            if data:
                # Convert to pandas DataFrame
                df = pd.DataFrame(data)
                
                # Filter rows where "Name" contains "台積電"
                if filter_value:
                    df = df[df[filter_column].str.contains(filter_value, na=False)]
                
                
                # Save  data to CSV
                #filtered_
                df.to_csv(output_file, index=False, encoding='utf-8-sig')
                print(f"Data saved to '{output_file}' ({len(df)} rows).")
            
            else:
                print("No data to save.")
        
        else: 
            print(f"Failed to fetch data. Status code: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")



# Monthly Closing price
get_data_requests(base_url = "https://openapi.twse.com.tw/v1",
                   endpoint = "/exchangeReport/FMSRFK_ALL", 
                   filter_column="Name",
                   filter_value="台積電",
                   output_file="data/tsmc/closing_price_monthly.csv")

# Yearly closing price
get_data_requests(base_url = "https://openapi.twse.com.tw/v1", 
                  endpoint = "/exchangeReport/FMNPTK_ALL",
                  filter_column="Name",
                  filter_value="台積電",
                  output_file="data/tsmc/closing_price_annual.csv")

# Day trade
get_data_requests(base_url = "https://openapi.twse.com.tw/v1",
                   endpoint = "/exchangeReport/TWTB4U", 
                   output_file="data/tsmc/day_trade.csv")


# Quartly gross margin
get_data_requests(base_url = "https://openapi.twse.com.tw/v1", 
                  endpoint = "/opendata/t187ap17_L",
                  filter_column="公司名稱tw",
                  filter_value="台積電",
                  output_file="data/tsmc/gross_margin_quarterly.csv")
