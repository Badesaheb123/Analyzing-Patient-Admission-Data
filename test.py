# print("hello world")

# print("Badesaheb Maruf")


import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

csv_path = "Project_analyzing_admission_data/records.csv"
# Load the CSV file
try:
    df = pd.read_csv(csv_path)
    print(df.head())
except FileNotFoundError:
    print(f'Error: file not found csv {csv_path}')

import os
print('Current Working Directory:', os.getcwd())
print('Files in Directory:', os.listdir("Project_analyzing_admission_data"))
# Count the occurrences of each department using Counter
department_counts = Counter(df['Department'])
print(department_counts)

# Convert the Counter object to a DataFrame for plotting
try:

    department_counts_df = pd.DataFrame.from_dict(department_counts, orient='index').reset_index()
    print(department_counts_df)
except Exception as e:
    print(e)
department_counts_df.columns = ['Department', 'Number of Patients']

# Ensure the 'Number of Patients' column is numeric
department_counts_df['Number of Patients'] = pd.to_numeric(department_counts_df['Number of Patients'])

# Plotting the bar graph
plt.figure(figsize=(10, 6))
plt.bar(department_counts_df['Department'], department_counts_df['Number of Patients'], color='lightblue')
plt.xlabel('Departments')
plt.ylabel('Number of Patients')
plt.title('Number of Patients in Each Department')
plt.xticks(rotation=45)
plt.show()