import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = pd.read_csv("quotes.csv")

# Count quotes per author
author_counts = data['Author'].value_counts().head(10)

# 1. Bar Chart
plt.figure()
author_counts.plot(kind='bar')
plt.title("Top 10 Authors by Number of Quotes")
plt.xlabel("Author")
plt.ylabel("Number of Quotes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Seaborn Count Plot
plt.figure()
sns.countplot(y='Author', data=data, order=data['Author'].value_counts().index[:10])
plt.title("Top Authors (Seaborn Visualization)")
plt.tight_layout()
plt.show()