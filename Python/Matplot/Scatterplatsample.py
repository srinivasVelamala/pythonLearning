import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 12, 8, 15, 7]

# Create a scatter plot
plt.scatter(x, y, color='red', marker='*', s=100, label='Data Points')
plt.legend()
plt.title("Sample Scatter Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()