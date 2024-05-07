import requests
import pandas


# specify license plate
selected_brand = input("Insert brand:\n").upper()

# define the endpoint
endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={selected_brand}"

# execute the response
response = requests.get(endpoint)

# get the data
data = response.json()

# convert to datat frame
data_df = pandas.DataFrame(data)

#
data_df.to_csv(f"data_{selected_brand}.csv", index=False)

pass