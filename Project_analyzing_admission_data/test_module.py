import unittest
import pandas as pd
from collections import Counter

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
df = pd.read_csv('records.csv')
data = pd.DataFrame(df)


# df = pd.DataFrame(new_data)

class TestAdmissionDatabase(unittest.TestCase):

    def test_most_common_diagonsis(self):
        most_common_diagonsis = df['Diagnosis'].mode()[0]
        self.assertNotEqual(most_common_diagonsis, 'Flu')

    def test_average_length_of_stay(self):
        df_common_diagonsis = df[df['Diagnosis']=='Flu']
        average_length_of_stay = df_common_diagonsis['Length of Stay'].mean()
        self.assertEqual(average_length_of_stay,8.0)

    def test_total_treatment_cost(self):
        df_common_diagonsis = df[df['Diagnosis']=='Flu']
        total_treatment_cost = df_common_diagonsis['Treatment Cost'].sum()
        self.assertEqual(total_treatment_cost,24000)
    
    def test_department_distribution(self):
        department_distribution = df['Department'].value_counts()
        self.assertNotEqual(department_distribution['General'],3)
    
    def test_total_days_per_department(self):
        total_days_per_department = df.groupby('Department')['Length of Stay'].sum()
        self.assertNotEqual(total_days_per_department['General'],32)
    
    def test_department_counts(self):
        department_counts = Counter(df['Department'])
        self.assertNotEqual(department_counts['General'], 3)

if __name__ == '__main__':
    unittest.main()

