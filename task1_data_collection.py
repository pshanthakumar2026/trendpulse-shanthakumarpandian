# Task 1: Data Collection
# Fetch trending data using Google Trends (pytrends)

from pytrends.request import TrendReq
import pandas as pd

def fetch_trends():
    pytrends = TrendReq(hl='en-US', tz=330)

    # Keywords (you can change based on interest)
    keywords = ["Artificial Intelligence", "Cricket", "Stock Market", "Renewable Energy"]

    pytrends.build_payload(keywords, timeframe='now 1-d')

    data = pytrends.interest_over_time()

    if data.empty:
        print("No data fetched!")
        return

    # Save raw data
    data.to_csv("trends_data.csv")

    print("✅ Data collection complete. Saved as trends_data.csv")

if __name__ == "__main__":
    fetch_trends()
