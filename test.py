import random
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import statistics

from scipy import stats




# ======================================================================================

# # --- Interpolate and clipping

# arr = [72.7000, 74.8100, 69.0400, 69.5000, 54.7900, 73.1500, 74., 9.5800, 74.2900, 72., 9.7400, 63.6500, 72.0200, 73.4300, 70.5900, 69.9400, 9.7400, 72.3100, 72.8400, 22.8600, 46.5500, 71.9500, 64.6500, 30.3900, 72.0500, 75.4700, 76.2100, 74.6500, 9.7400, 73.6900, 45.2000, 66.9600, 68.0800, 74.6200, 56.6600, 73.4900, 76.7700, 73.9900, 27.9900, 62.8900, 9.7400, 76.3700, 9.7400, 35.5100, 9.7400, 69.4800, 66.0200, 71.7000, 71.9800, 22.9100, 71.6200, 72.1700, 60.7000, 72.3500, 72.9200, 75.5800, 66.7300, 70.2900, 36.7000, 72.7600, 71.2600, 71.9500, 71.2200, 74.5500, 64.7000, 70.6800, 67.0600, 75.3300, 59.9300, 50.0700, 73.9000, 23.9100, 10.2800, 73.8000, 13.0100, 9.7400, 28.5900, 74.1600, 9.7400, 73.6500, 60.7200, 48.5400, 74.6600, 16.8500, 73.8900, 32.0400, 74.0900, 9.5800, 71.9800, 10.2800, 67.8200, 70.2900, 73.4300, 10.2800, 71.7900, 66.7300, 10.2800, 75.5700, 67.0200, 76.6500]
# print("Original array: {}".format(arr))
# avg_arr = np.mean(arr)
# std_arr = np.std(arr)
# print("Mean of array: {}".format(avg_arr))
# print("Standard deviation of array: {}".format(std_arr))
# a_new_arr_interp = np.interp(arr, [avg_arr - (1 * std_arr), avg_arr + (1 * std_arr)], [0, 1])
# print("Interpolated array: {}".format(a_new_arr_interp))
# print("(Interpolated - Original): {}".format(a_new_arr_interp - arr))
# prev_arr_interp = a_new_arr_interp
# np.clip(a_new_arr_interp, 0, 0.99999999999, out=a_new_arr_interp)
# print("Clipped after interpolation array: {}".format(a_new_arr_interp))
# print("(Clipped - Interpolate): {}".format(a_new_arr_interp - prev_arr_interp))

# # Clipping is extra step as interpolating will already convert outliers to the max / min value in the new array


# ======================================================================================

# # --- determines the average number of tries needed before a collision is hit

# limit = 1000  # can generate up to this integer value
# trials = 1000 # number of trials to conduct
# max_tries = 250 # max number of tries in a trial
# collision_indexes = []
# for trial in range(trials):
#   numbers = []
#   for i in range(max_tries):
#     number = random.randint(0,limit)
#     if number in numbers:
#       # print("Collision occured at {} with number {}".format(numbers.index(number), number))
#       collision_indexes.append(i)
#       break
    
#     numbers.append(number)

# # print("The list: {}".format(numbers))
# # print("Length of list: {}".format(len(numbers)))

# print("Average collision index: {}".format(statistics.mean(collision_indexes)))


# ======================================================================================

# # --- performs circular shift

# arr = [i for i in range(10)]
# # circular-shift right once
# temp = arr[len(arr)-1]
# for ind in range(len(arr)-1, 0, -1):
#   arr[ind] = arr[ind-1]
# arr[0] = temp
# print(arr)


# ======================================================================================

# # --- divide by inf

# vec = np.divide([1,2,3,4,5,-6,-7,-8,-9,-10], [0,0,0,float('inf'),float('inf'),float('inf'),float('inf'),0,0,0])  # divides by 0, hence inf
# print(vec)
# print(random.uniform(min(vec.tolist()), max(vec.tolist()))) # get number from [-inf, inf] = nan


# ======================================================================================

# # --- tests for different random rates

# tally = 0
# for i in range(1000):
#   if random.random() + random.random() > 1.5:
#     tally += 1
# print(tally)

# random.random() < random.random() = 50%
# random.random() <= random.random() = ~51%
# random.random() + random.random() > 1 = 50%
# random.random() + random.random() > 1.5 = 12.5%

