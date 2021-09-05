# Implementing max heap #

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

# Attempt #2:
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
#   if(array[length//2] < array[end]):
#     print("I am in the first half")
#     while(end != first_half_mid):
#       count +=1
#       if(array[end] > array[first_half_mid]):
#         array[end], array[first_half_mid] = array[first_half_mid], array[end]
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

def insert(new_element):
  length = len(array)
  array.append(new_element)

  # recursion

print('Inserting element is in the first half ...')
array = [10, 8, 7, 6, 4, 5, 3, 2, 0, 1];
insert(12)

# array = [8,7,4,3,1];
# insert(6)

# print('Inserting element is in the second half ...')
# array = [100, 80, 70, 60, 40, 50, 30, 20, 0, 10];
# insert(35)

# print('Inserting element is at the center, but will be a part of the first half ...')
# array = [8, 7, 5, 3, 1]
# insert(6)

# Time complexity: log2(N) =~ 2.8 =~ 3
