import pandas as pd

def save_listings_to_csv(listings, file_path):
    df = pd.DataFrame(listings)
    df.to_csv(file_path, index=False)
