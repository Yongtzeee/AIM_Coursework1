import random
import numpy as np




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