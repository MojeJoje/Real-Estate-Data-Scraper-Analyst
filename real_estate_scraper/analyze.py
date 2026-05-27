import pandas as pd


def analyze(file_path="sample_data/sample_listings.csv"):
    df = pd.read_csv(file_path)
    pivot = df.pivot_table(index="area", values="price", aggfunc="mean")
    print("Average price by area:")
    print(pivot)
    output_path = "sample_data/average_price_by_area.csv"
    pivot.to_csv(output_path)
    print(f"Saved pivot table to {output_path}")


if __name__ == "__main__":
    analyze()
