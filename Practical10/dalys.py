# IBI1 Practical 10: Working with Global Health Data
# Student name: [Your Name]
# Date: [Date]

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ---------------------- 1. Set working directory ----------------------
# Change this path to YOUR local folder where the csv is stored
os.chdir("/home/rob/Work/IBI1/Practical10")

# Check current working directory (same as pwd in Unix)
print("Current working directory:", os.getcwd())

# List files in folder (same as ls in Unix)
print("Files in directory:", os.listdir())

# ---------------------- 2. Import CSV dataset into DataFrame ----------------------
# Read DALYs dataset using pandas
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# ---------------------- 3. Explore the dataframe ----------------------
# Show first 5 rows
print("\n=== First 5 rows of dataset ===")
print(dalys_data.head(5))

# Show data structure and variable types
print("\n=== Dataframe information ===")
dalys_data.info()

# Show summary statistics (count, mean, std, min, max, etc.)
print("\n=== Summary statistics ===")
print(dalys_data.describe())

# ---------------------- 4. Show first 10 rows: Year and DALYs (3rd & 4th columns) ----------------------
# Select first 10 rows, column index 2 (Year) and 3 (DALYs)
first_10_afghanistan = dalys_data.iloc[0:10, [2, 3]]
print("\n=== First 10 rows (Year and DALYs) ===")
print(first_10_afghanistan)

# Find year with maximum DALYs in Afghanistan's first 10 years
max_year_afg = first_10_afghanistan.loc[first_10_afghanistan["DALYs"].idxmax(), "Year"]
# COMMENT FOR PORTFOLIO: Year with maximum DALYs in Afghanistan first 10 years
print("Year with maximum DALYs in Afghanistan (first 10 years):", max_year_afg)

# ---------------------- 5. Extract all years for Zimbabwe using Boolean indexing ----------------------
# Filter all rows where Entity is Zimbabwe
zimbabwe_data = dalys_data.loc[dalys_data["Entity"] == "Zimbabwe"]
print("\n=== Zimbabwe DALYs data by year ===")
print(zimbabwe_data[["Year", "DALYs"]])

# Get first and last year of Zimbabwe data
zimbabwe_first_year = zimbabwe_data["Year"].min()
zimbabwe_last_year = zimbabwe_data["Year"].max()

# COMMENT FOR PORTFOLIO: First and last year for Zimbabwe DALYs data
print("First year of Zimbabwe data:", zimbabwe_first_year)
print("Last year of Zimbabwe data:", zimbabwe_last_year)

# ---------------------- 6. Find countries with max and min DALYs in 2019 ----------------------
# Filter data for the year 2019 only
data_2019 = dalys_data.loc[dalys_data["Year"] == 2019, ["Entity", "DALYs"]]

# Find country with maximum DALYs in 2019
country_max_dalys = data_2019.loc[data_2019["DALYs"].idxmax()]

# Find country with minimum DALYs in 2019
country_min_dalys = data_2019.loc[data_2019["DALYs"].idxmin()]

# COMMENT FOR PORTFOLIO: Countries with maximum and minimum DALYs in 2019
print("\nCountry with maximum DALYs in 2019:", country_max_dalys["Entity"])
print("Country with minimum DALYs in 2019:", country_min_dalys["Entity"])

# ---------------------- 7. Plot DALYs over time for one country (min or max) ----------------------
# Select the country with minimum DALYs in 2019 for plotting
target_country = country_min_dalys["Entity"]
country_time_data = dalys_data.loc[dalys_data["Entity"] == target_country]

# Create time series plot
plt.figure(figsize=(10, 5))
plt.plot(country_time_data["Year"], country_time_data["DALYs"], "bo-", linewidth=2, markersize=5)
plt.title(f"{target_country} DALYs Over Time (1990–2019)")
plt.xlabel("Year")
plt.ylabel("DALYs (Disability‑Adjusted Life Years)")
plt.xticks(country_time_data["Year"], rotation=-90)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# ---------------------- 8. Answer my own question (for question.txt) ----------------------
# LINE NUMBER FOR QUESTION.TXT: Line 78
# Question: What is the distribution of DALYs across all countries in 2019?
print("\n=== Own question: 2019 global DALYs distribution ===")

# Plot boxplot of 2019 DALYs
plt.figure(figsize=(8, 6))
plt.boxplot(data_2019["DALYs"].dropna())
plt.title("Distribution of DALYs Across All Countries in 2019")
plt.ylabel("DALYs")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# Calculate range between maximum and minimum DALYs in 2019
dalys_range_2019 = data_2019["DALYs"].max() - data_2019["DALYs"].min()
print("Range of DALYs in 2019:", dalys_range_2019)

# Interpretation: The distribution is highly skewed. Most countries have low DALYs, while a few have very high burden.