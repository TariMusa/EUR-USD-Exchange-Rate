import requests
import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO
import re

# Load the webpage content
url = "https://en.wikipedia.org/wiki/World_Happiness_Report"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find all tables with the class 'wikitable'
tables = soup.find_all("table", {"class": "wikitable"})

# Iterate over each table and save them individually
for i, table in enumerate(tables):
    try:
        # Use StringIO to parse the table HTML
        table_html = str(table)
        df = pd.read_html(StringIO(table_html))[0]

        # Try to find the corresponding header for the year
        header = table.find_previous("h2")
        header_text = header.get_text(strip=True) if header else ""

        # Extract the year using regex (looks for a 4-digit number)
        match = re.search(r"\b(19|20)\d{2}\b", header_text)
        year = match.group(0) if match else f"Unknown_{i + 1}"

        # Save the dataframe as a CSV file named by the year
        filename = f"world_happiness_{year}.csv"
        df.to_csv(filename, index=False)
        print(f"Saved: {filename}")

    except Exception as e:
        print(f"Error processing table {i + 1}: {e}")
