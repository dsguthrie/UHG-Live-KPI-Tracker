import yfinance as yf
import pandas as pd
from datetime import datetime

# Define ticker
ticker = yf.Ticker("UNH")

# Get info dictionary
info = ticker.info

# Create a DataFrame with key financial KPIs
data = {
    "Date": [datetime.today().strftime('%Y-%m-%d')],
    "Stock Price": [info.get("currentPrice")],
    "Market Cap (B)": [info.get("marketCap") / 1e9 if info.get("marketCap") else None],
    "PE Ratio": [info.get("trailingPE")],
    "EPS (TTM)": [info.get("trailingEps")],
    "Forward PE": [info.get("forwardPE")],
    "Revenue (TTM, B)": [info.get("totalRevenue") / 1e9 if info.get("totalRevenue") else None],
    "Employees": [info.get("fullTimeEmployees")],
    "Sector": [info.get("sector")],
    "Industry": [info.get("industry")]
}

df = pd.DataFrame(data)

# Define Excel path
output_path = r"C:\Users\drake\OneDrive\Desktop\Live KPI Tracker\uhg_kpi_tracker.xlsx"

# Save to Excel
df.to_excel(output_path, index=False)

print(f" UHG KPIs saved to Excel at:\n{output_path}")
from datetime import datetime

with open("log.txt", "a") as log:
    log.write(f" KPI refresh ran successfully on {datetime.now()}\n")
