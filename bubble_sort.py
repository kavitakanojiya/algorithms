# array = [10,9,8,7,6,5,4,3,2,1]
# array = [5,4,3,2,1]
array = [1,2,3,4,5]


def bubble_sort(array):
  length = len(array)
  iterations = 0

  modified = False

  for i in range(length):
    # iterations += 1
    for j in range(length - i - 1):
      iterations += 1  # n - 1
      if array[j] > array[j+1]:
        array[j], array[j+1] = array[j+1], array[j]
        modified = True
    if modified == False:
      break

  print("No. of iterations: {}").format(iterations)
  return array


print("Original array : {}".format(array))
bubble_sort(array)
print("Sorted array : {}".format(array))