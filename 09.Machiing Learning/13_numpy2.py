import numpy as np

# Create an array of data
data = np.array([1, 2, 3, 4, 5])

# Mean (average) of the data
mean = np.mean(data)
print("Mean :  %d" % mean)

# Median of the data
median = np.median(data)
print("Median :  %d" % median)

# Standard deviation of the data
std_dev = np.std(data)
print("SD :  %d" % std_dev)

# Variance of the data
variance = np.var(data)
print("Variance :  %d" % variance)
