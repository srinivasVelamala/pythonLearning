import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 12, 15, 18, 22]

# Correctly double the values for the second line
x1 = [i * 2 for i in x]
y1 = [j * 2 for j in y]

# Create a simple line plot with colored lines
plt.plot(x, y, marker='o', color='green', label='Original')
plt.plot(x, y1, marker='o', color='blue', label='Doubled')
plt.title("Sample Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()
plt.grid(True)
plt.show()