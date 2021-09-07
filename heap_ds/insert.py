# Implementing max heap #
# Attempts 1 through 3 implement divide-n-conquer
# Attempt 4 implements ...

# INSTRUCTIONS:
#
# We have to swap the new element with the parent's node if parent < node.
# So, as per max heap, all the higher nodes are present towards the start of the array.
# Potentially, we have to iterate the first half of the array.
#
# NOTE:
#
# This is not a sorting algorithm
# Elements at a same node could be out of order but that's fine. Why?
#

# Attempt #1:
# def insert(new_element):
#   # 1. insert at last, leaf node
#   length = len(array)
#   array.append(new_element)

#   #2. initialize i as the length of the array
#   # if the element fits in the first half of the array
#   i = length
#   left = int(i/2)
#   count = 0
#   while(left >= 0):
#     if(array[i] > array[left]):
#       count += 1
#       array[i], array[left] = array[left], array[i]
#       i = left
#       left = int(left/2)

#     if(i == 0):
#       break

#   print(array)
#   print(count)

# ====================================================================>>>>

# # Attempt #2:
# def insert(new_element):
#   # 1. insert at last, leaf node
#   length = len(array)
#   array.append(new_element)
#   count = 0

#   #
#   #2. initialize i as the length of the array
#   # if the element fits in the first half of the array
#   end = length
#   first_half_mid = end//2

#   #
#   # 3. runs through first half : DONE
#   # print(array)
#   if(array[length//2] < array[end]):
#     print("I am in the first half")
#     while(end != first_half_mid):
#       count +=1
#       if(array[end] > array[first_half_mid]):
#         array[end], array[first_half_mid] = array[first_half_mid], array[end]
#       # print(array)
#       end = first_half_mid
#       first_half_mid = end//2
#   else:
#     #
#     # 4. runs through second half
#     print("I am in the second half")
#     end = length
#     initial = (end//2) + 1
#     second_half_mid = (initial + length)//2

#     while(end != second_half_mid):
#       count +=1
#       if(array[end] > array[second_half_mid]):
#         array[end], array[second_half_mid] = array[second_half_mid], array[end]
#       end = second_half_mid
#       second_half_mid = (initial + second_half_mid)//2

#   print(count)
#   print(array)

# ====================================================================>>>>

# # Attempt #3:
# def insert(new_element):
#   start = 0
#   end = len(array)
#   insert.count = 0

#   print('Input:', array)

#   array.append(new_element)

#   # recursion
#   arrange_recursively(array, start, end)

#   print('Output:', array)
#   print('No. of iterations:', insert.count)
#   print('\n')

# def arrange_recursively(_array, start, end):
#   if(start != end):
#     print('Looping start: {} through end: {}'.format(start, end))
#     insert.count += 1

#     # divide into half equal parts
#     mid = ((start + end)//2)

#     print('Index: start: {}; end: {}; mid: {}'.format(start, end, mid))
#     print('Value: end: {}; mid: {}'.format(_array[end], _array[mid]))

#     # 1. iterating through first half of the array when end > mid
#     # 2. else, iterating through second half of the array when mid > end
#     if(_array[end] > _array[mid]):
#       _array[end], _array[mid] = _array[mid], _array[end]
#       end = mid
#       arrange_recursively(_array, start, end)
#     else:
#       _array[end], _array[mid+1] = _array[mid+1], _array[end]
#       start = mid + 1
#       arrange_recursively(_array, start, end)


# print('Inserting element is in the first half ...')
# Index: start: 0; end: 1; mid: 0
# array = [10, 8, 7, 6, 4, 5, 3, 2, 0, 1];
# insert(12)
# O/P: [12, 10, 8, 6, 4, 7, 3, 2, 0, 1, 5]
# => Time complexity = O(logN) ~ 4

# Index: start: 4; end: 5; mid: 3
# array = [8,7,4,3,1];
# insert(6)
# O/P: [8, 7, 6, 3, 1, 4]
# => Time complexity = O(logN) ~ 2

# breaking with attempt #3
# print('Inserting element is in the second half ...')
# Index: start: 4; end: 5; mid: 3
# array = [100, 80, 70, 60, 40, 50, 30, 20, 0, 10];
# insert(35)
# O/P: [100, 80, 70, 60, 40, 50, 35, 30, 20, 10, 0]
# => Time complexity = O(logN) ~ 4

# breaking with attempt #3
# print('Inserting element is at the center, but will be a part of the first half ...')
# Index: start: 4; end: 5; mid: 3
# array = [8, 7, 5, 3, 1]
# insert(6)
# O/P: [8, 7, 6, 3, 1, 5]
# => Time complexity = O(logN) ~ 2


# breaking with attempt #3
# Index: start: 2; end: 4; mid: 2
# array = [100, 80, 70, 60, 40, 50, 30, 20, 0, 10];
# insert(55)
# O/P: [100, 80, 70, 60, 55, 40, 30, 20, 0, 10, 50]
# Time complexity: log2(N) =~ 4

# Status: Won't work
# Traversing through with divide-n-conquer does not guarantee the parent of new element (added as a child node)
# Whereas expectation is the inserted element should replace its immediate parent.
# Max heap does not sort element but ensures the children nodes are less than the parent node.
# ====================================================================>>>>

# # Attempt #4:
def insert(new_element):
  print('Input:', array)
  print('New element to be inserted:', new_element)
  # Implementation: starts here
  #
  insert.count = 0
  array.append(new_element)
  arrange_recursively(array, len(array) - 1)
  #
  # Implementation: ends here

  print('Output:', array)
  print('No. of iterations:', insert.count)
  print('\n')

def arrange_recursively(array, new_element_position):
  if(new_element_position <= 0):
    return

  parent_position = (new_element_position - 1) // 2

  if(array[parent_position] < array[new_element_position]):
    insert.count += 1
    array[parent_position], array[new_element_position] = array[new_element_position], array[parent_position]
    arrange_recursively(array, parent_position)

array = [10, 8, 7, 6, 4, 5, 3, 2, 0, 1];
insert(12)
# Actual O/P: [12, 10, 7, 6, 8, 5, 3, 2, 0, 1, 4]
# Expected O/P: [12, 10, 7, 6, 8, 5, 3, 2, 0, 1, 4]
# 

array = [8,7,4,3,1];
insert(6)
# Actual O/P: [8, 7, 6, 3, 1, 4]
# Expected O/P: [8, 7, 6, 3, 1, 4]

array = [100, 80, 70, 60, 40, 50, 30, 20, 0, 10];
insert(35)
# Actual O/P:  [100, 80, 70, 60, 40, 50, 30, 20, 0, 10, 35]
# Expected O/P: [100, 80, 70, 60, 40, 50, 30, 20, 0, 10, 35]

array = [8, 7, 5, 3, 1]
insert(6)
# Actual O/P: [8, 7, 6, 3, 1, 5]
# Expected O/P: [8, 7, 6, 3, 1, 5]

array = [100, 80, 70, 60, 40, 50, 30, 20, 0, 10];
insert(55)
# Actual O/P: [100, 80, 70, 60, 55, 50, 30, 20, 0, 10, 40]
# Expected O/P: [100, 80, 70, 60, 55, 50, 30, 20, 0, 10, 40]

array = [100, 80, 70, 60, 40, 50, 30, 20, 0, 10];
insert(101)
# Actual O/P: [101, 100, 70, 60, 80, 50, 30, 20, 0, 10, 40]
# Expected O/P: [101, 100, 70, 60, 80, 50, 30, 20, 0, 10, 40]

# Best case: when the new element is maximum in the heap = O(logN) =~ 3
# Worst case: when the new element is minimum among the child nodes = O(logN) =~ 0
#
# Verified from: https://visualgo.net/en/heap
