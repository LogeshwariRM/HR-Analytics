import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency, ttest_ind

# Load the data
file_path = 'HR analytics.csv'
df = pd.read_csv(file_path)

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Department', hue='Gender')
plt.title('Gender Distribution by Department')
plt.xticks(rotation=45)
plt.show()
