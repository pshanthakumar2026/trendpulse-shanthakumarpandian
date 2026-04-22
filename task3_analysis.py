# Task 3: Data Analysis
# Perform basic trend analysis

import pandas as pd

def analyze_data():
    df = pd.read_csv("cleaned_data.csv")

    # Drop date column for numeric analysis
    numeric_df = df.select_dtypes(include=['number'])

    # Calculate average trend scores
    mean_values = numeric_df.mean()

    # Find top trending topic
    top_topic = mean_values.idxmax()
    top_value = mean_values.max()

    print("\n📊 Trend Analysis Results")
    print("----------------------------")
    print("Average Trend Scores:\n")
    print(mean_values)

    print("\n🔥 Top Trending Topic:", top_topic)
    print("Score:", round(top_value, 2))

    # Save analysis
    with open("analysis_results.txt", "w") as f:
        f.write("Trend Analysis Results\n\n")
        f.write(str(mean_values))
        f.write(f"\n\nTop Trending Topic: {top_topic} ({top_value})")

    print("\n✅ Analysis saved to analysis_results.txt")

if __name__ == "__main__":
    analyze_data()
