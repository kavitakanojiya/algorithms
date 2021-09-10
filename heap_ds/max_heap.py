class MaxHeap:
  def __init__(self):
    self.array = []

  def insert(self, element):
    """
    When invoked, inserts a new element to the heap and rebalances to maintain the property of the max heap.
    Every insert takes O(logN) time to rebalance.

    Insert happens from the leaf node where the new element is added
    """

    # Append the new element to the array
    self.array.append(element)
    length = len(self.array)

    # Terminate if the array has only 1 element
    if(length == 1):
      return
    self.insert_heapify(length-1, length)

  def delete(self):
    """
    When invoked, pops out the root element from the heap and rebalances to maintain the property of the max heap.
    Every delete takes O(logN) time to rebalance.
    """
    last_element = self.array[-1]
    self.array[0] = last_element
    self.array.pop()

    self.delete_heapify(0, len(self.array))

  def tree(self):
    """
    Handy method that groups elements at the same level and prints.
    """
    i = 0
    start = 0
    end = 2**i
    while(start < len(self.array)-1):
      print("Current level {}: {}".format(i, self.array[start:end]))
      i += 1
      start = end
      end += 2**i

  def max(self):
    """
    Returns the max element from the heap which is the root node.
    Finding the max element takes O(1) time.
    """
    return self.array[0]

  def insert_heapify(self, new_element_position, length):
    """
    This is a bottom-top approach.

    Steps:
    1. Add the new element at the leaf node i.e. at the end of the array
    2. Compare the leaf node with its immediate parent
       2.1 Parent node could be calculated as (currentElementPosition - 1)//2 to get the floor integer
       2.2 If the parent is smaller than the new element, swap them
       2.3 If the parent is greater than the new element, stop the iteration
    3. Perform #2 recursively
    """

    # Terminate if the current position less than 0
    if(new_element_position == 0):
      return

    # Compute position of its immediate parent
    parent_position = (new_element_position - 1) // 2

    # Swap if the current element is smaller than the parent
    if(self.array[parent_position] < self.array[new_element_position]):
      self.array[parent_position], self.array[new_element_position] = self.array[new_element_position], self.array[parent_position]
      # Perform this recursively until the root node so the heap is balanced
      self.insert_heapify(parent_position, length)

  def delete_heapify(self, current_position, length):
    """
    This removes the max value from the heap which is 0th element.
    This is a top-bottom approach.

    Steps:
    1. Pick the leaf node i.e. last element from the array and move it to the root node
    2. Compare this element with the left and right children
       2.1 Left node could be calculated as (2*currentElementPosition + 1)//2
       2.2 Right node could be calculated as (2*currentElementPosition + 2)//2
       2.3 Replace the root element with either left or right if the root element is smaller than either of them
       2.4 If the root element is greater than both the children, stop the iteration
    3. Perform #2 recursively
    """

    # Starts with the root position and considers it the largest element
    largest = current_position
    # Calculates left and right children position
    left = 2*current_position + 1
    right = 2*current_position + 2


    # Stop if position of children is beyond the length of the array
    if(left > length or right > length):
      return

    # Considers the left child as the largest if it is greater than the current element
    if(left < length and self.array[largest] < self.array[left]):
      largest = left

    # Considers the right child as the largest if it is greater than the left element
    if(right < length and self.array[largest] < self.array[right]):
      largest = right

    # Swap with the current element with the child only if the child is greater
    self.array[largest], self.array[current_position] = self.array[current_position], self.array[largest]
    # Iterate recursively until it stops
    self.delete_heapify(largest, length)
