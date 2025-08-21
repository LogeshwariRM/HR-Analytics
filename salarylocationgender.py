import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency, ttest_ind

# Load the data
file_path = 'HR analytics.csv'
df = pd.read_csv(file_path)
df['Salary'] = df['Salary'].replace('[\$,]','',regex=True).astype(float)


plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Loc', y='Salary', hue='Gender')
plt.title('Salary Distribution by Location and Gender')
plt.xticks(rotation=45)
plt.show()