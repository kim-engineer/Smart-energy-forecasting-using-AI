# scripts/data_explore.py
# Day 2 – Data Exploration Script

import pandas as pd
import matplotlib.pyplot as plt

# Loading dataset (make sure data/energy_data.csv exists)
df = pd.read_csv("data/energy_data.csv", parse_dates=["date"])

# Displaying first 5 rows in console
print("Sample of dataset:")
print(df.head())

# Plotting daily energy consumption
plt.figure(figsize=(10,4))
plt.plot(df['date'], df['consumption_kwh'], marker='o', linewidth=1)
plt.title("Daily Energy Consumption (kWh)")
plt.xlabel("Date")
plt.ylabel("Consumption (kWh)")
plt.tight_layout()

# Saving the plot
plt.savefig("dashboard/consumption_plot.png")
print("Plot saved as dashboard/consumption_plot.png")
