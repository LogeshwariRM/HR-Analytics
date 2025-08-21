import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency, ttest_ind

# Load the data
file_path = 'HR analytics.csv'
df = pd.read_csv(file_path)
df['Salary'] = df['Salary'].replace('[\$,]','',regex=True).astype(float)

# Statistical Analysis
# Chi-Square test for categorical variables
def chi_square_test(df, col1, col2):
    contingency_table = pd.crosstab(df[col1], df[col2])
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    return chi2, p

# T-test for numerical variables
def t_test(df, group_col, value_col):
    group1 = df[df[group_col] == df[group_col].unique()[0]][value_col]
    group2 = df[df[group_col] == df[group_col].unique()[1]][value_col]
    t_stat, p_val = ttest_ind(group1, group2, equal_var=False)
    return t_stat, p_val

# Gender & Location
chi2_gender_location, p_gender_location = chi_square_test(df, 'Gender', 'Loc')

# Gender & Department
chi2_gender_department, p_gender_department = chi_square_test(df, 'Gender', 'Department')

# Gender & Rating
chi2_gender_rating, p_gender_rating = chi_square_test(df, 'Gender', 'Rating')

# Gender & Salary
t_stat_gender_salary, p_val_gender_salary = t_test(df, 'Gender', 'Salary')

# Location & Salary
f_stat_location_salary, p_val_location_salary = t_test(df, 'Loc', 'Salary')

# Department & Salary
f_stat_department_salary, p_val_department_salary = t_test(df, 'Department', 'Salary')

# Printing the results of statistical tests
print("\nStatistical Analysis Results:")
print(f"Chi-Square Test between Gender & Location: chi2 = {chi2_gender_location}, p-value = {p_gender_location}")
print(f"Chi-Square Test between Gender & Department: chi2 = {chi2_gender_department}, p-value = {p_gender_department}")
print(f"Chi-Square Test between Gender & Rating: chi2 = {chi2_gender_rating}, p-value = {p_gender_rating}")
print(f"T-Test between Gender & Salary: t-statistic = {t_stat_gender_salary}, p-value = {p_val_gender_salary}")
print(f"T-Test between Location & Salary: t-statistic = {f_stat_location_salary}, p-value = {p_val_location_salary}")
print(f"T-Test between Department & Salary: t-statistic = {f_stat_department_salary}, p-value = {p_val_department_salary}")

