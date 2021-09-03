# Attempt #1
# def call_to_graph():
#   array = [None, 6, 4, 5, 3, 2, 0, 1]
#   level = 0
#   index = 1

#   # Level 0 has [6]
#   caret = 2**level - 1
#   print("Level {} has elements: {}", level, array[caret:2**level+caret])
#   level += 1

#   # level = 1, level #1 has [4,5]
#   caret = 2**level - 1
#   print("Level {} has elements: {}", level, array[caret:2**level+caret])
#   level += 1

#   # level = 2, level #1 has [3,2,0,1]
#   caret = 2**level - 1
#   print("Level {} has elements: {}", level, array[caret:2**level+caret])
#   level += 1


# Attempt #2
# def call_to_graph():
#   array = [None, 6, 4, 5, 3, 2, 0, 1]
#   current_level = 0
#   index = 1

#   while True:
#     caret = 2**current_level
#     print("Level {} has elements {}:", current_level, array[index:index+caret])
#     current_level += 1
#     index += caret
#     if index >= len(array):
#       break

# Attempt #3
def call_to_graph():
  array = [6, 4, 5, 3, 2, 0, 1]
  current_level = 0
  index = 0

  while True:
    caret = 2**current_level
    print("Level {} has elements {}:", current_level, array[index:index+caret])
    current_level += 1
    index += caret
    if index >= len(array):
      break

call_to_graph()

# Time complexity = log2(N) = 2.8 =~ 3
