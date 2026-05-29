import numpy as np

# Mean, median, std
data = np.array([10, 20, 30, 40, 50])

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Std:", np.std(data))

# Random values
rand = np.random.randint(1, 100, 5)
print(rand)

# Sorting
print(np.sort(rand))

# Min / Max
print(np.min(rand))
print(np.max(rand))