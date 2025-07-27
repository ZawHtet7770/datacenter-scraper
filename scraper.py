import pandas as pd
from datetime import datetime

# Expanded Region Mapping
REGION_MAP = {
    # APAC
    "tokyo": "APAC", "singapore": "APAC", "mumbai": "APAC", "seoul": "APAC",
    # EMEA
    "dubai": "EMEA", "frankfurt": "EMEA", "london": "EMEA", "oslo": "EMEA",
    # North America
    "mexico": "North America", "virginia": "North America", "ohio": "North America"
}

def get_region(location):
    """Safely extract region from any location string"""
    if not isinstance(location, str):
        return "Unknown"
    loc_lower = location.lower()
    for key in REGION_MAP:
        if key in loc_lower:
            return REGION_MAP[key]
    return "Unknown"  # Default value

def scrape():
    print("🌐 Region-Aware Scraper Started!")
    
    # Sample Data (Replace with real scraping)
    data = {
        "date": ["2025-07-30", "2025-07-30", "2025-07-30"],
        "provider": ["Google", "Amazon", "Microsoft"],
        "location": ["Tokyo, Japan", "Dubai, UAE", "Unknown City"],
        "size_sqft": [150000, 200000, 0],  # 0 for unknown
        "power_mw": [45.0, 50.0, 0],
        "link": ["https://example.com/1", "https://example.com/2", ""]
    }
    
    # Create DataFrame WITH REGION COLUMN (ensured)
    df = pd.DataFrame(data)
    df["region"] = df["location"].apply(get_region)  # Always added
    df["last_update"] = datetime.now().strftime("%Y-%m-%d %H:%M") 
    
    # Save to CSV
    df.to_csv("output1.csv", index=False)
    print("✅ CSV saved with regions!")
    return df

if __name__ == "__main__":
    scrape()

