# Data setup
countries = ["UK", "China", "Italy", "Brazil", "USA"]
pop_2020 = [66.7, 1426, 59.4, 208.6, 331.6]
pop_2024 = [69.2, 1410, 58.9, 212.0, 340.1]

# 1. Calculate percentage change
percent_changes = []
for i in range(len(countries)):
    change = ((pop_2024[i] - pop_2020[i]) / pop_2020[i]) * 100
    percent_changes.append(change)

# Print individual changes
print("Percentage Population Change for each country:")
for i in range(len(countries)):
    print(f"{countries[i]}: {percent_changes[i]:.2f}%")

# 2. Sort from largest increase to largest decrease
# zip countries and changes together to keep them linked during sorting
combined_data = list(zip(countries, percent_changes))

# Sort by the second element (change percentage) in descending order
sorted_data = sorted(combined_data, key=lambda x: x[1], reverse=True)

sorted_countries = [item[0] for item in sorted_data]
sorted_changes = [item[1] for item in sorted_data]

print("\nPopulation changes sorted (Largest Increase to Largest Decrease):")
for country, change in sorted_data:
    print(f"  {country}: {change:.2f}%")

# Identify largest increase and decrease
largest_increase_country = sorted_data[0][0]
largest_increase_val = sorted_data[0][1]

largest_decrease_country = sorted_data[-1][0]
largest_decrease_val = sorted_data[-1][1]

print(f"\n   Country with largest increase: {largest_increase_country} ({largest_increase_val:.2f}%)")
print(f"   Country with largest decrease: {largest_decrease_country} ({largest_decrease_val:.2f}%)")

# 3. Create a well-labelled bar chart
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
# Use distinct colors for positive (increase) and negative (decrease)
colors = ['green' if x > 0 else 'red' for x in sorted_changes]

plt.bar(sorted_countries, sorted_changes, color=colors, edgecolor='black')
plt.axhline(0, color='black', linewidth=1) # Add a line at y=0
plt.title("Population Change by Country (2020-2024)", fontsize=14)
plt.xlabel("Country", fontsize=12)
plt.ylabel("Percentage Change (%)", fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()