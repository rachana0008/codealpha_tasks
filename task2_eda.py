import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("quotes.csv")

# 1. Explore data structure
print("First 5 rows:\n", data.head())
print("\nData Info:")
print(data.info())

# 2. Basic analysis
print("\nTotal Quotes:", len(data))
print("\nUnique Authors:", data['Author'].nunique())

# 3. Most common authors
top_authors = data['Author'].value_counts().head(5)
print("\nTop 5 Authors:\n", top_authors)

# 4. Visualization
top_authors.plot(kind='bar')
plt.title("Top 5 Authors")
plt.xlabel("Author")
plt.ylabel("Number of Quotes")
plt.show()