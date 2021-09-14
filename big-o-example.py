import time

start_time = time.time() # start the stopwatch

def print_time_elapsed():
    end_time = time.time() # stop the stopwatch
    time_elapsed = end_time - start_time
    time_elapsed = round(time_elapsed, 2) # round it to a nice number
    print(f"{time_elapsed} seconds have passed")

#######################################
huge_haystack = ['hay'] * 100000000 # data set of size n (10million)
huge_haystack.append('needle')

# Constant O(1)
# Number of operations stays constant as input increases
def find_needle_in_haystack(arr):
    needle_from_the_sewing_kit = "needle" # O(1)
    return needle_from_the_sewing_kit

# find_needle_in_haystack(huge_haystack)
# print_time_elapsed()

# Linear O(n)
# Number of operations increases linearly with the input
def find_needle_in_haystack(arr):
    for i in range(len(huge_haystack)):
        if huge_haystack[i] == 'needle':
            return i

# find_needle_in_haystack(huge_haystack)
# print_time_elapsed()

# # Quadratic O(n^2)
# number of operations increases by a power of two as input increases
def find_needle_in_haystack(arr):
    num_operations = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            num_operations += 1
            print(num_operations)

small_haystack = ['hay'] * 1000
find_needle_in_haystack(small_haystack)

# Logarithmic O(log(n))
# Halving the problem space (input) with each operation - phonebook!

# Like a binary search
# Split the haystack into two haystacks
# Use a metal detector

# And repeatedly repeat the above three steps with the remaining halves of the 
# haystack
