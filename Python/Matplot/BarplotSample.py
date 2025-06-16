import matplotlib.pyplot as plt

# Sample data
categories = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 78]

# Create a bar plot
plt.bar(categories, values, color='skyblue')
plt.title("Sample Bar Plot")
plt.xlabel("Category")
plt.ylabel("Value")
plt.show()