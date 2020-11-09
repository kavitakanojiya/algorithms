# Using Kadane's algorithm
# Complexity comes down to O(n) i.e. linear

def maximum_sum_from_subarray(array):
  no_of_iterations = 0

  length = len(array)
  max_current = array[0]
  max_global  = array[0]

  for element in array[1:]:
    adjacent_sum = element + max_current
    max_current  = max(element, adjacent_sum)
    max_global   = max(max_global, max_current)
    no_of_iterations += 1

  print('No. of iterations: {}').format(no_of_iterations)
  return max_global

# array = [1, 5, -1, 0, 10]
# => 15

# array = [0, -1, -5, 0, -4]
# => 0

array = [1, -3, 2, 1, -1]
# => 3

# array = [-2, 3, 2, -1]

# array = [0,1,2,3]
# => 6

# array = [-1,0,1]
# => 1

# array =  [-4,-3,-2,-1]
# => -1

# array = [2, 3, -3, -1, 2, 1, 5, -3]
# => 9

output = maximum_sum_from_subarray(array)
print(output)
