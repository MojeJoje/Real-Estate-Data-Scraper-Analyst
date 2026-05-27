import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

def export_to_gsheets(csv_path, sheet_name):
    # Set up Google Sheets API
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)
    
    # Read data
    df = pd.read_csv(csv_path)
    sheet = client.create(sheet_name).sheet1
    sheet.update([df.columns.values.tolist()] + df.values.tolist())
    print(f"Exported {csv_path} to Google Sheets: {sheet_name}")

if __name__ == "__main__":
    export_to_gsheets("../sample_data/sample_listings.csv", "Real Estate Listings")
