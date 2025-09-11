
import pandas as pd



def download_nfci_direct_csv():
    url = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=NFCI"
    df = pd.read_csv(url)

    print(df.head())
    df.to_csv("data/tsmc/nfci_data.csv", index=False)


download_nfci_direct_csv()