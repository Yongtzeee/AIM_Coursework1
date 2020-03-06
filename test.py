import random
import numpy as np




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