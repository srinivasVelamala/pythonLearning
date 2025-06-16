import pandas as pd
# Create a DataFrame
data = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
# Print the DataFrame
print(data)
# Accessing elements
print(data['a'])  # Accessing by label

