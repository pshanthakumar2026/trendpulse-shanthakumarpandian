# Task 4: Data Visualization
# Plot trends using matplotlib

import pandas as pd
import matplotlib.pyplot as plt

def visualize_data():
    df = pd.read_csv("cleaned_data.csv")

    # Set datetime as index if available
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
        df = df.set_index('date')

    # Plot all trends
    plt.figure(figsize=(12, 6))

    for column in df.columns:
        plt.plot(df.index, df[column], label=column)

    plt.title("📈 Google Trends Analysis")
    plt.xlabel("Time")
    plt.ylabel("Interest Level")
    plt.legend()
    plt.grid()

    # Save plot
    plt.savefig("trend_visualization.png")

    plt.show()

    print("✅ Visualization saved as trend_visualization.png")

if __name__ == "__main__":
    visualize_data()
