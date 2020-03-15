import random
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import statistics

# box plotting
original_results = [72.7000, 74.8100, 69.0400, 69.5000, 54.7900, 73.1500, 74., 9.5800, 74.2900, 72., 9.7400, 63.6500, 72.0200, 73.4300, 70.5900, 69.9400, 9.7400, 72.3100, 72.8400, 22.8600, 46.5500, 71.9500, 64.6500, 30.3900, 72.0500, 75.4700, 76.2100, 74.6500, 9.7400, 73.6900, 45.2000, 66.9600, 68.0800, 74.6200, 56.6600, 73.4900, 76.7700, 73.9900, 27.9900, 62.8900, 9.7400, 76.3700, 9.7400, 35.5100, 9.7400, 69.4800, 66.0200, 71.7000, 71.9800, 22.9100, 71.6200, 72.1700, 60.7000, 72.3500, 72.9200, 75.5800, 66.7300, 70.2900, 36.7000, 72.7600, 71.2600, 71.9500, 71.2200, 74.5500, 64.7000, 70.6800, 67.0600, 75.3300, 59.9300, 50.0700, 73.9000, 23.9100, 10.2800, 73.8000, 13.0100, 9.7400, 28.5900, 74.1600, 9.7400, 73.6500, 60.7200, 48.5400, 74.6600, 16.8500, 73.8900, 32.0400, 74.0900, 9.5800, 71.9800, 10.2800, 67.8200, 70.2900, 73.4300, 10.2800, 71.7900, 66.7300, 10.2800, 75.5700, 67.0200, 76.6500]
modified_results = [75.27999877929688, 76.31999969482422, 73.5, 73.27999877929688, 73.7699966430664, 75.79000091552734, 74.73999786376953, 74.4000015258789, 75.5999984741211, 75.0999984741211, 74.73999786376953, 74.4800033569336, 74.51000213623047, 74.75, 75.45999908447266, 73.80999755859375, 74.27999877929688, 73.61000061035156, 74.3499984741211, 73.13999938964844, 74.38999938964844, 74.55000305175781, 74.61000061035156, 74.9800033569336, 73.68000030517578, 76.02999877929688, 74.56999969482422, 74.86000061035156, 74.9800033569336, 73.66999816894531, 74.26000213623047, 76.77999877929688, 72.51000213623047, 72.7699966430664, 73.04000091552734, 73.91000366210938, 74.23999786376953, 75.76000213623047, 75.01000213623047, 75.18000030517578, 75.16999816894531, 75.58999633789062, 74.19000244140625, 73.0199966430664, 73.7300033569336, 75.12999725341797, 73.2300033569336, 73.41000366210938, 75.55000305175781, 74.30999755859375, 74.83000183105469, 73.52999877929688, 74.16000366210938, 74.25, 74.77999877929688, 74.5999984741211, 74.83000183105469, 75.0999984741211, 74.5999984741211, 75.08000183105469, 73.80999755859375, 49.06999969482422, 74.79000091552734, 75.52999877929688, 75.33999633789062, 75.43000030517578, 75.13999938964844, 74.29000091552734, 73.3499984741211, 74.83999633789062, 75.08000183105469, 75.33999633789062, 74.31999969482422, 75.2300033569336, 75.04000091552734, 73.73999786376953, 75.4800033569336, 75.88999938964844, 76.01000213623047, 73.94999694824219, 73.6500015258789, 75.98999786376953, 74.87999725341797, 75.37000274658203, 75.37000274658203, 75.0999984741211, 75.33000183105469, 73.69000244140625, 73.66999816894531, 73.9000015258789, 75.08000183105469, 76.16000366210938, 73.69000244140625, 75.06999969482422, 75.18000030517578, 72.37000274658203, 74.80999755859375, 73.88999938964844, 72.91000366210938, 76.80999755859375]
data = [original_results, modified_results]

print("Original condition:")
print("Mean accuracy:         {}".format(np.mean(original_results)))
print("Standard deviation:    {}".format(np.std(original_results)))
print("1st Quartile accuracy: {}".format(np.percentile(original_results, 25)))
print("Median accuracy:       {}".format(np.percentile(original_results, 50)))
print("3rd Quartile accuracy: {}".format(np.percentile(original_results, 75)))
print("Interquartile range:   {}".format(np.percentile(original_results, 75) - np.percentile(original_results, 25)))

print("\nModified condition:")
print("Mean accuracy:         {}".format(np.mean(modified_results)))
print("Standard deviation:    {}".format(np.std(modified_results)))
print("1st Quartile accuracy: {}".format(np.percentile(modified_results, 25)))
print("Median accuracy:       {}".format(np.percentile(modified_results, 50)))
print("3rd Quartile accuracy: {}".format(np.percentile(modified_results, 75)))
print("Interquartile range:   {}".format(np.percentile(modified_results, 75) - np.percentile(modified_results, 25)))

# x label
# y label
# title
# y limit
fig, ax = plt.subplots()
ax.boxplot(data)
ax.set_title("Result of both conditions after 100 trials")
plt.ylim(0, 100)
plt.xlabel("Conditions (1 is original, 2 is modified)")
plt.ylabel("Validation accuracy")

plt.show()



# ======================================================================================

# arr = [i for i in range(10)]
# # circular-shift right once
# temp = arr[len(arr)-1]
# for ind in range(len(arr)-1, 0, -1):
#   arr[ind] = arr[ind-1]
# arr[0] = temp
# print(arr)


# ======================================================================================

# vec = np.divide([1,2,3,4,5,-6,-7,-8,-9,-10], [0,0,0,float('inf'),float('inf'),float('inf'),float('inf'),0,0,0])  # divides by 0, hence inf
# print(vec)
# print(random.uniform(min(vec.tolist()), max(vec.tolist()))) # get number from [-inf, inf] = nan


# ======================================================================================

# tally = 0
# for i in range(1000):
#   if random.random() + random.random() > 1.5:
#     tally += 1
# print(tally)

# random.random() < random.random() = 50%
# random.random() <= random.random() = ~51%
# random.random() + random.random() > 1 = 50%
# random.random() + random.random() > 1.5 = 12.5%

