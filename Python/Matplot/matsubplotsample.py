import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y1 = [10, 12, 15, 18, 22]
y2 = [5, 7, 9, 11, 13]

# Create subplots: 1 row, 2 columns
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# First subplot
ax1.plot(x, y1, color='green', marker='o')
ax1.set_title("Plot 1")
ax1.set_xlabel("X Axis")
ax1.set_ylabel("Y1 Axis")

# Second subplot
ax2.plot(x, y2, color='blue', marker='s')
ax2.set_title("Plot 2")
ax2.set_xlabel("X Axis")
ax2.set_ylabel("Y2 Axis")

plt.tight_layout()
plt.show()