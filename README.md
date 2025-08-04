# UHG-Live-KPI-Tracker
Live KPI dashboard for UnitedHealth Group using Python, Excel VBA, and Power BI. Automated daily data refresh with Task Scheduler and manual override via macro-enabled Excel interface. Visualizes key stock and performance metrics in a fully dynamic dashboard.


This project tracks live financial KPIs for UnitedHealth Group (UNH) using a fully automated pipeline:

- Python: pulls real-time stock & performance data
- Excel (.xlsm): serves as a dynamic data store with manual VBA refresh
- Windows Task Scheduler: automates daily refresh
- Power BI Dashboard: visualizes live KPIs

# Tools Used
- Python (yfinance, pandas)
- Excel (macro-enabled for VBA refresh button)
- Power BI Desktop
- Windows Task Scheduler

# Tracked Metrics
- Stock Price
- Market Cap
- PE Ratio / EPS
- Revenue (TTM)
- Sector / Industry
- Employees

# Dashboard Preview
<img width="898" height="419" alt="Screenshot 2025-08-04 155542" src="https://github.com/user-attachments/assets/bc784cc3-7640-49ea-8edb-68408a7f2ce0" />



# How to Run
1. Clone this repo
2. Run `live_kpi_tracker.py` manually or schedule with Windows Task Scheduler
3. Open `uhg_kpi_tracker.xlsm` and click the **"Refresh Data"** button if needed
4. Open Power BI dashboard and hit refresh
