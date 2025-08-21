import pandas as pd
csv_file ='HR analytics.csv'
df = pd.read_csv(csv_file)
df['Salary'] = df['Salary'].replace('[\$,]','',regex=True).astype(float)


# 1. How many Males/Females are there in the entire organization?
gender_counts = df['Gender'].value_counts()

# 2. How many Males/Females are there in each department or location?
gender_department_counts = df.groupby(['Department', 'Gender']).size().unstack()
gender_location_counts = df.groupby(['Loc', 'Gender']).size().unstack()

# 3. For which department is the average pay highest?
avg_pay_department = df.groupby('Department')['Salary'].mean()
highest_avg_pay_department = avg_pay_department.idxmax(), avg_pay_department.max()

# 4. For which location is the average pay highest?
avg_pay_location = df.groupby('Loc')['Salary'].mean()
highest_avg_pay_location = avg_pay_location.idxmax(), avg_pay_location.max()

# 5. What percentage of employees received good & very good rating? 
# What about poor & very poor rating? and average rating?
rating_counts = df['Rating'].value_counts(normalize=True) * 100

good_ratings_percentage = rating_counts[['Good', 'Very Good']].sum()
poor_ratings_percentage = rating_counts[['Poor', 'Very Poor']].sum()
average_ratings_percentage = rating_counts['Average']

# 6. Compute gender pay gap for each department. Interpret.
gender_pay_gap_department = df.groupby(['Department', 'Gender'])['Salary'].mean().unstack()
gender_pay_gap_department['Pay Gap'] = gender_pay_gap_department['Male'] - gender_pay_gap_department['Female']

# 7. Compute gender pay gap for each location. Interpret.
gender_pay_gap_location = df.groupby(['Loc', 'Gender'])['Salary'].mean().unstack()
gender_pay_gap_location['Pay Gap'] = gender_pay_gap_location['Male'] - gender_pay_gap_location['Female']

# Printing the results
print("1. Gender Counts in the entire organization:")
print(gender_counts)
print("\n2. Gender Counts in each department:")
print(gender_department_counts)
print("\n2. Gender Counts in each location:")
print(gender_location_counts)
print("\n3. Department with highest average pay:")
print(highest_avg_pay_department)
print("\n4. Location with highest average pay:")
print(highest_avg_pay_location)
print("\n5. Ratings percentages:")
print(f"Good & Very Good Ratings: {good_ratings_percentage:.2f}%")
print(f"Poor & Very Poor Ratings: {poor_ratings_percentage:.2f}%")
print(f"Average Ratings: {average_ratings_percentage:.2f}%")
print("\n6. Gender Pay Gap by Department:")
print(gender_pay_gap_department)
print("\n7. Gender Pay Gap by Location:")
print(gender_pay_gap_location)