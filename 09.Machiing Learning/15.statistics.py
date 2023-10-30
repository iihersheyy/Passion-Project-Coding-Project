import statistics

data = [1, 2, 3, 4, 5]

# Calculate the mean using the statistics module
mean = statistics.mean(data)
print("Mean : %s" % str(mean))

# Calculate the median
median = statistics.median(data)
print("Median : %s" % str(median))

# Calculate the standard deviation
std_dev = statistics.stdev(data)
print("SD : %s" % str(std_dev))

# Calculate the variance
variance = statistics.variance(data)
print("Variance : %s" % str(variance))
