import scipy.stats as stats

# Normal distribution
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Calculate the mode (most frequent value)
mode = stats.mode(data)
print("Mode :  %s" % str(mode))

# Calculate the skewness of the data
skewness = stats.skew(data)
print("Skewness :  %s" % str(skewness))

# Calculate the kurtosis of the data
kurtosis = stats.kurtosis(data)
print("Kurtosis :  %s" % str(kurtosis))
