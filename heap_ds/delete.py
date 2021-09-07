# Given: Existing array should maintain the property of the max heap

def max_heapify(array, index, length):
	#
  # maintain the property of max heap

  # Step 1: Consider the element at `index` is largest
  largest = index
  # Step 2: Compute left child
  left = 2*index + 1
  # Step 3: Compute right child
  right = 2*index + 2

  # print('Left: {}; Right: {}; Largest: {}; Array: {}'.format(left, right, largest, array))

  # Step 4: Exit if either left or right exceeds the length of the array
  if(left > length or right > length):
    return

  # Step 5: Set the largest as left child index if the left child is greater than the one at `index`
  if(left < length and array[left] > array[largest]):
    largest = left

  # Step 6: Set the largest as right child index if the right child is greater than the one at `index`.
  if(right < length and array[right] > array[largest]):
    largest = right

  # Step 7: Swap the element at `index` with the element at `largest` only if largest is not the current node
  # Perform the iteration recursively
  if(largest != index and largest < length):
    array[largest], array[index] = array[index], array[largest]
    max_heapify(array, largest, length)
    delete.count += 1
  #

def delete(array):
  print('Input:', array)

  # pick the last element
  last_element = array[len(array) - 1]
  # move the last element at the root
  array[0] = last_element
  array.pop()

  delete.count = 0

  # balance the max heap
  max_heapify(array, 0, len(array))
  print('Output:', array)
  print('No. of iterations:', delete.count)

# array = [2,8,7,4,3,1];
# max_heapify(array, 0, len(array))

# array = [8,7,4,3,1];
# delete(array)

# when the root node be deleted i.e. O(logN) =~ 3
array = [100, 80, 70, 60, 40, 50, 30, 20, 10, 0];
delete(array)
