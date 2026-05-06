import pandas as pd
import matplotlib.pyplot as plt

file_path='Visualization/visualization/data.csv'
df = pd.read_csv(file_path)

# 2. EXPLORING DATA TYPES (Shape, Columns, Types)
print('------------------')
print("--- DATA TYPES ---")
print(f"Shape: {df.shape}") 
print(f"\nColumns: {df.columns}")
print("\nData Types:")
print(df.dtypes)

# 3. CLEAN DATA
# Checking for missing values and duplicates
missing_count = df.isnull().sum().sum()
duplicate_count = df.duplicated().sum()

# Cleaning
df = df.fillna(0) 
df = df.drop_duplicates()
print('-----------------------------')
print('-------CLEANING DETAILS------')
print(f"Missing values: {missing_count}")
print(f"Duplicates removed: {duplicate_count}")

# --- CHART 1: PIE CHART (Weather Condition) ---
# 1. Count the occurrences of each weather condition
counts = df['Condition'].value_counts()

# 2. Create the Pie Chart
plt.pie(counts, labels=counts.index, autopct='%1.1f%%')
plt.title('Weather Condition Distribution')
plt.axis('equal') # Makes the pie a perfect circle
plt.show()

# --- CHART 2: BAR GRAPH ( Average Temperature per Place) ---

# 1. Calculate Average Temperature per Place
avg_temp = df.groupby('Place')['Avg_Temp_C'].mean()

# 2. Create the Bar Graph
plt.bar(avg_temp.index, avg_temp.values, color='tomato', edgecolor='black')
# 3. Add Labels and Titles
plt.title('Average Temperature by Place')
plt.xlabel('Place')
plt.ylabel('Average Temperature (°C)')
plt.show()



