# Real Estate Listings Scraper

A Python project to extract property listings (address, price, bedrooms, bathrooms, sqft, listing date, agent contact) from property portals for a specific city or zip code range. Supports both JS-heavy and static portals. Includes data analysis and export to Google Sheets.

## Features
- Scrape listings from property portals (e.g., Zillow, local sites)
- Extract address, price, bedrooms, bathrooms, sqft, listing date, agent contact
- Use Playwright for JS-heavy portals, BeautifulSoup for static portals
- Analyze data with Pandas
- Export results to Google Sheets
- Sample pivot table: average price by area

## Getting Started
1. Install dependencies: `pip install -r requirements.txt`
2. Generate or refresh the sample dataset: `python generate_sample_data.py`
3. Configure the target portal and search parameters in `real_estate_scraper/config.py`
4. Run the scraper entry point: `python -m real_estate_scraper.main`
5. Analyze the data and generate the pivot table: `python -m real_estate_scraper.analyze`
6. Export to Google Sheets (optional, requires service account credentials): `python -m real_estate_scraper.export_to_gsheets`

## Project Structure
- `real_estate_scraper/` — Scraper and analysis code
- `sample_data/` — Example dataset (60 listings) and pivot table output
- `README.md` — Project documentation
- `.github/copilot-instructions.md` — Copilot workflow

## Requirements
- Python 3.8+
- Playwright
- BeautifulSoup4
- Pandas
- gspread (for Google Sheets export)

## Portfolio Tip
Show the final dataset with 50-100 listings and a pivot table of average price by area to demonstrate analysis capability.

---

*Replace portal-specific code and credentials as needed for your target site.*