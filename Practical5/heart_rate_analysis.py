# 1. Number of patients and mean heart rate
heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]
num_patients = len(heart_rates)
mean_hr = sum(heart_rates) / num_patients
print(f"There are {num_patients} patients in the dataset, and the mean heart rate is {mean_hr:.2f} bpm.")

# 2. Categorize heart rates
low_count = 0      # < 60
normal_count = 0   # 60 - 120
high_count = 0     # > 120

for hr in heart_rates:
    if hr < 60:
        low_count += 1
    elif 60 <= hr <= 120:
        normal_count += 1
    else: # hr > 120
        high_count += 1

print(f"Category Counts -> Low: {low_count}, Normal: {normal_count}, High: {high_count}")

# Identify the largest category
categories = {"Low": low_count, "Normal": normal_count, "High": high_count}
largest_category = max(categories, key=categories.get)

print(f"The category with the largest number of patients is: {largest_category}")

# 3. Create a Pie Chart
import matplotlib.pyplot as plt

labels = ['Low (<60)', 'Normal (60-120)', 'High (>120)']
sizes = [low_count, normal_count, high_count]
colors = ['lightgreen', 'skyblue', 'salmon']

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title("Distribution of Heart Rate Categories", fontsize=14)
plt.axis('equal') # Equal aspect ratio ensures the pie is drawn as a circle
plt.show()