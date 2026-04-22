# Task 2: Data Processing
# Clean and prepare the collected data

import pandas as pd

def process_data():
    df = pd.read_csv("trends_data.csv")

    # Remove unwanted column if exists
    if 'isPartial' in df.columns:
        df = df.drop(columns=['isPartial'])

    # Handle missing values
    df = df.fillna(0)

    # Reset index (convert datetime index to column)
    df = df.reset_index()

    # Rename columns for clarity
    df.columns = [col.replace(" ", "_") for col in df.columns]

    # Save cleaned data
    df.to_csv("cleaned_data.csv", index=False)

    print("✅ Data processing complete. Saved as cleaned_data.csv")

if __name__ == "__main__":
    process_data()
