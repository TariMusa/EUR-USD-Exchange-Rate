import pandas as pd
import requests  # Use requests to make API calls

# Define the base URL for the World Bank API
base_url = "http://api.worldbank.org/v2"

# Specify the parameters (dataset example: GDP per capita)
indicator = "NY.GDP.PCAP.CD"  # GDP per capita (current US$)
country = "all"  # Get data for all countries
date = "2010:2022"  # Date range (2010 to 2022)
format_type = "json"  # Requesting data in JSON format

# Construct the API URL
url = f"{base_url}/country/{country}/indicator/{indicator}?date={date}&format={format_type}&per_page=10000"

# Make a request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Data fetched successfully!")

    # Parse the JSON response
    json_data = response.json()

    # Check the structure of the JSON response
    if len(json_data) > 1:
        data = pd.DataFrame(json_data[1])  # Extract the data part
        print(data.head())  # Preview the data

        # Save the data as a CSV file
        data.to_csv("world_bank_gdp_per_capita.csv", index=False)
        print("Data saved as 'world_bank_gdp_per_capita.csv'.")
    else:
        print("No data found in the response.")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
