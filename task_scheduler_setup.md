# Task Scheduler Setup – Daily Python Refresh

This guide explains how to set up a **daily automatic refresh** for the `live_kpi_tracker.py` script using **Windows Task Scheduler**.

---

# Goal

Automatically run the Python script each morning to refresh UnitedHealth Group KPI data and export the latest metrics to Excel.

---

# Requirements

- Python 3.13+ installed
- All required packages installed (`yfinance`, `pandas`, `openpyxl`, etc.)
- `live_kpi_tracker.py` saved locally (e.g., Desktop)
- Windows 10 or 11 (with Task Scheduler)

---

# Step-by-Step Instructions

## 1. Find Your Python Executable

- Run this in PowerShell or Command Prompt:

where python

- Example Result:

C:\Users\name\AppData\Local\Programs\Python\Python313\python.exe

---

## 2. Open Task Scheduler

Press Window key + S, type Task Scheduler, and open it

---

## 3. Create a Basic Task

- Click Create Basic Task
- Name: UHG KPI Daily Refresh
- Description: Runs live_kpi_tracker.py daily to refresh Excel KPI data

---

## 4. Set Trigger

- Choose: Daily

---

## 5. Set Action

- Choose: Start a program
- Program/script:

C:\Users\name\AppData\Local\Programs\Python\Python313\python.exe

- Add arguments (optional):

C:\Users\name\OneDrive\Desktop\Live KPI Tracker\live_kpi_tracker.py

---

## 6. Finish and Test

- Click Finish
- Right-click the new task and then run to test it



