import pandas as pd
import random

random.seed(42)

areas = ["Downtown", "Midtown", "Uptown", "Suburb", "Riverfront"]
records = []
for i in range(60):
    area = random.choice(areas)
    sqft = random.randint(900, 3200)
    bedrooms = random.randint(1, 5)
    bathrooms = random.randint(1, 4)
    price = int((sqft * random.uniform(180, 260)) + (bedrooms * 12000) + (bathrooms * 8000))
    records.append({
        "address": f"{1000 + i} {random.choice(['Main', 'Oak', 'Pine', 'Elm', 'Cedar'])} St",
        "price": price,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "sqft": sqft,
        "listing_date": f"2026-0{(i % 9) + 1:01d}-{(i % 27) + 1:02d}",
        "agent_contact": f"agent{i}@example.com",
        "area": area,
    })

_df = pd.DataFrame(records)
_df.to_csv("sample_data/sample_listings.csv", index=False)
print(f"Generated {len(_df)} sample listings in sample_data/sample_listings.csv")
