import matplotlib.pyplot as plt

# Sample data with 4 data points (each as a separate group)
data = [
    [12, 15, 13, 17],
    [19, 21, 18, 17],
    [16, 14, 13, 15],
    [19, 20, 22, 18]
]

# Create a box plot
plt.boxplot(data)
plt.title("Sample Box Plot with 4 Data Groups")
plt.ylabel("Value")
plt.xlabel("Group")
plt.show()