"""
Top N Elements

=====

Problem statement: To persist top 10 elements

This uses min-heap data structure where locating the minimum element in the list is easy to find.
If the new element is less the minimum, we can simply ignore or else, we should swap them with the minimum in the list.

Complexity:
Insert = O(logN)
Pop the minimum = O(1)
Maintain the min heap = O(logN)

Worst case complexity = Insert + Pop + Maintain = O(logN) + O(1) + O(logN)
Best case complexity = O(1)
"""

from min_heap import MinHeap;

class TopNElements:
  def __init__(self, n):
    self.n = n
    self.heap = MinHeap()

  def insert(self, element):
    # Verify if length of the heap has reached the limit `n`
    if(self.validate() == True):
      # Pops out the minimum element from the heap if the new element is larger, thus maintaining the `n`
      if(element > self.heap.min()):
        self.heap.delete()
      else:
        return

    # Insert the element
    self.heap.insert(element);

  def validate(self):
    # returns True if queue length is upto maximum
    return (len(self.elements()) == self.n)

  def extract(self):
    return self.elements()[::-1]

  def elements(self):
    return self.heap.array


klass = TopNElements(5)
klass.insert(10)
klass.insert(2)
klass.insert(5)
klass.insert(8)
klass.insert(7)
print('Elements in the min heap:', klass.heap.array)

print('\n')

# Should not be inserted as this is smaller than the minimum in the heap
print('New element:', 1)
klass.insert(1)
print('Elements in the max heap:', klass.heap.array)
print('Top N elements:', klass.extract())

print('\n')

# Should be inserted as this is greater than the minimum in the heap and will be the minimum
print('New element:', 4)
klass.insert(4)
print('Elements in the max heap:', klass.heap.array)
print('Top N elements:', klass.extract())

print('\n')

# Should be inserted as this is greater than the minimum in the heap and will be the maximum
print('New element:', 20)
klass.insert(20)
print('Elements in the max heap:', klass.heap.array)
print('Top N elements:', klass.extract())
