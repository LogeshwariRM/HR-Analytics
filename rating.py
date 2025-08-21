import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency, ttest_ind

# Load the data
file_path = 'HR analytics.xlsx'
df = pd.read_excel(file_path)

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Rating', hue='Gender')
plt.title('Ratings Distribution by Gender')
plt.xticks(rotation=45)
plt.show()
