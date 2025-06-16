import matplotlib.pyplot as plt

# Sample data
data = [12, 15, 13, 17, 19, 21, 18, 17, 16, 14, 13, 15, 19, 20, 22]

# Create a histogram
plt.hist(data, bins=9, color='purple', edgecolor='black')
plt.title("Sample Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()