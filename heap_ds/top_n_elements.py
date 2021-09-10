"""
Top N Elements

=====

Problem statement: To persist top 10 elements

This uses min-heap data structure where locating the minimum element in the list is easy to find.
If the new element is less the minimum, we can simply ignore or else, we should swap them with the minimum in the list.

Complexity:
k = top K (size of heap)
n => total no. of elements from which top K has to be derived

Insert = O(logN)
Pop the minimum = O(1)
Maintain the min heap = O(logN)


k => top K (size of heap)
n => total no. of elements from which top K has to be derived

O(1) + (O(1) + O(lgk)) => if n >> k => O(1) + O(1) + O(c) => O(1) (constant time)
Total running time: O(n) * O(1) => O(n)

----

Any other when sorting n and get top k => O(nlgn)

----

Worst case complexity = Duplicate check + Swap + Maintain = O(k) + O(1) + O(logk) => O(k) + O(1) + O(C)
So, total running time: O(n) * O(1) => O(n)

Best case complexity = O(1)
"""

from min_heap import MinHeap;

class TopNElements:
  def __init__(self, n):
    self.n = n
    self.heap = MinHeap()

  def insert(self, element):
    # Skip if the element exists in the heap
    if(self.isDuplicate(element) == True):
      return

    # Verify if length of the heap has reached the limit `n`
    if(self.isSizeExceeded() == True):
      # Pops out the minimum element from the heap if the new element is larger, thus maintaining the `n`
      if(element > self.heap.min()):
        self.heap.swap_minimum(element)
      else:
        return
    else:
      # Insert the element
      self.heap.insert(element);

  def isSizeExceeded(self):
    # returns True if queue length has its maximum limit
    return (len(self.elements()) == self.n)

  def isDuplicate(self, element):
    return(element in self.elements())

  def extract(self):
    return self.elements()[::-1]

  def elements(self):
    return self.heap.array

