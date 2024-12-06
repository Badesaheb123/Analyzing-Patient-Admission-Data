import pandas as pd

df = pd.read_csv('records.csv')
# df = pd.DataFrame(data)

# df['Admission Date'] = pd.to_datetime(df['Admission Date'])
# df['Discharge Date'] = pd.to_datetime(df['Discharge Date'])
# df['Length of Stay'] = (df['Discharge Date'] - df['Admission Date']).dt.days
# df.dropna(inplace=True)

# new_data = {
#     'Patient ID': [4, 5,8,9,10],
#     'Admission Date': ['2024-01-05', '2024-02-10','2024-03-05', '2024-04-10','2024-09-10'],
#     'Discharge Date': ['2024-01-15', '2024-02-20','2024-03-13', '2024-04-16','2024-09-19'],
#     'Age': [30, 45,55,23,78],
#     'Gender': ['F', 'M','F','M','M'],
#     'Diagnosis': ['Asthma', 'Diabetes', 'Flu', 'Cold', 'Fever'],
#     'Department': ['Pulmonology', 'Endocrinology', 'General', 'General', 'General'],
#     'Length of Stay': [10, 10, 8, 9, 15],
#     'Treatment Cost': [2000, 4000, 8000, 10000,1000]
# }

# list1 = ['Pulmonology', 'Endocrinology', 'General']
# value_counts = {'Department':values.count(values) for values in new_data.values()}
# print(value_counts)

from collections import Counter
# Count the occurrences of each department using Counter

# department_counts = Counter(new_data['Department'])
# print(department_counts)

department_counts = Counter(df['Department'])
# print(department_counts)

# data = pd.DataFrame(new_data)

# df_updated = pd.concat([df,data])

# columns_to_remove = ['length_Of_stay']
# df_updated = df.drop(columns=columns_to_remove)

# df_updated.to_csv('records.csv', index=False)


# print("New data has been added 'records.csv'.")
# print(df)


# print(df.describe())
# print(df['Age'].value_counts())
# print(df['Gender'].value_counts())
# print(df['Diagnosis'].value_counts())
# print(df.groupby('Department')['Length of Stay'].mean())
# print(df.groupby('Department')['Treatment Cost'].sum())



import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10,6))
sns.histplot(df['Age'], bins=20, kde=True)
plt.title('Age Distribution')
plt.show()

df['Gender'].value_counts().plot.pie(autopct = "%1.1f%%", startangle =90 )
plt.title('Gender Distibutuions')
plt.show()

df['Diagnosis'].value_counts().head(10).plot.bar()
plt.title('Top 10 Diagonsis')
plt.show()


sns.boxplot(x='Department', y='Length of Stay', data=df)
plt.title('Length of stay by department')
plt.show()

df.groupby('Department')['Treatment Cost'].sum().plot.bar()
plt.title('Total treatment Cost by Department')
plt.show()

df.groupby('Department')['Length of Stay'].mean().plot.bar()
plt.title('Identify Departments')
plt.show()

#Identify the most common dioagonsis
most_common_diagonsis = df['Diagnosis'].mode()[0]

#filter data frame for the most common diagonsis
df_common_daiagonsis = df[df['Diagnosis'] == most_common_diagonsis]

#analyaze the impact on hospital resources 
average_length_of_stay = df_common_daiagonsis['Length of Stay'].mean()
total_treatment_cost = df_common_daiagonsis['Treatment Cost'].sum()
department_distribution = df_common_daiagonsis['Department'].value_counts()


#plotting the results
fig, axs = plt.subplots(1,3, figsize=(18,6))

#plot average length of stay
axs[0].bar(['Length of Stay'], [average_length_of_stay])
axs[0].set_ylabel('Days')
axs[0].set_title('Average Lengtyh of Stay')

#Plot Treatment of Cost
axs[1].bar(['Treatment Cost'], [total_treatment_cost])
axs[1].set_ylabel('Cost($)')
axs[1].set_title('Total Treatment Cost')


#Plot Departmemt Distribution
department_distribution.plot(kind='bar', color='salmon', ax=axs[2])
axs[2].set_ylabel('department_counts')
axs[2].set_title('Department Distribution')

#Set the main title for this figure
fig.suptitle(f'Imact the most common Diagonsis:{most_common_diagonsis}', fontsize=16)
plt.tight_layout(rect=[0,0.03,1,0.95])
plt.show()


# Highlight the most common diagnoses and their impact on hospital resources.
# df.groupby('Department')['Diagnosis'].sum().plot.bar()
# plt.title('Each department common diagonsis')
# plt.show()

# Convert the Counter object to a DataFrame for plotting
try:

    department_counts_df = pd.DataFrame.from_dict(department_counts, orient='index').reset_index()
    # print(department_counts_df)
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


#Suggest areas for cost reduction based on treatment cost analysis.
sns.boxplot(x='Diagnosis', y='Length of Stay', data=df)
plt.title('Cost Reduction based on treatment analysis')
plt.show()

