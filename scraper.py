# SUPER SIMPLE SCRAPER STARTER
import pandas as pd
from datetime import datetime

def scrape():
    print(" Data Collector Started!")
    
    # Sample Data (will be add real scraping later)
    data = {
        "date": ["2025-07-28"],
        "provider": ["Google"],
        "location": ["Tokyo, Japan"],
        "size_sqft": [150000],
        "power_mw": [45.0],
        "link": ["https://example.com"],
        "last_update": [datetime.now().strftime("%Y-%m-%d %H:%M")]
    }
    
    pd.DataFrame(data).to_csv("output.csv")
    print(" CSV file created!")

if __name__ == "__main__":
    scrape()
