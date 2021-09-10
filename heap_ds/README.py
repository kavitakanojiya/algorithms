from min_heap import MinHeap;
from max_heap import MaxHeap;
from top_n_elements import TopNElements;

#
# Sample data to learn MaxHeap
#
#
# Sample #1 #
def data1():
  klass = MaxHeap()
  klass.insert(80)
  klass.insert(70)
  klass.insert(100)
  klass.insert(0)
  klass.insert(40)
  klass.insert(50)
  klass.insert(30)
  klass.insert(20)
  klass.insert(60)
  klass.insert(10)
  print('Final array after all inserts:', klass.array)

  print('Max element from the heap:', klass.max())

  print('\n');
  print('Heap elements at every level:')
  klass.tree()
  print('\n');

  klass.delete()
  print('Final array after a delete/s:', klass.array)

# Sample #2 #
def data2():
  klass = MaxHeap()
  klass.insert(3)
  klass.insert(2)
  klass.insert(1)
  print('Final array after all inserts:', klass.array)

  print('Max element from the heap:', klass.max())

  print('\n');
  print('Heap elements at every level:')
  klass.tree()
  print('\n');

  klass.delete()
  print('Printing final array delete/s:', klass.array)

print('=================================== MaxHeap with sample data #1 ===================================');
data1();
print('\n');
print('=================================== MaxHeap with sample data #2 ===================================');
data2();


#
# Sample data to learn MinHeap
#
#
def data3():
  klass = MinHeap()
  klass.insert(3)
  klass.insert(1)
  klass.insert(2)
  klass.insert(0)
  klass.insert(-1)
  print('Array after all inserts:', klass.array)

  print('Minimum element:', klass.min())

  print('\n');
  print('Heap elements at every level:')
  klass.tree()
  print('\n');

  klass.delete()
  print('Array after delete/s:', klass.array)

def data4():
  klass = MinHeap()
  klass.insert(5)
  klass.insert(10)
  klass.insert(9)
  klass.insert(8)
  klass.insert(7)
  print('Array after all inserts:', klass.array)

  print('Minimum element:', klass.min())

  print('\n');
  print('Heap elements at every level:')
  klass.tree()
  print('\n');

  klass.delete()
  print('Array after delete/s:', klass.array)

print('\n');
print('=================================== MinHeap with sample data #1 ===================================');
data3();
print('\n');
print('=================================== MinHeap with sample data #2 ===================================');
data4();


#
# Sample data to learn TopNElements
#
#
def data5():
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
  print('Elements in the min heap:', klass.heap.array)
  print('Top N elements:', klass.extract())

  print('\n')

  # Should be inserted as this is greater than the minimum in the heap and will be the minimum
  print('New element:', 4)
  klass.insert(4)
  print('Elements in the min heap:', klass.heap.array)
  print('Top N elements:', klass.extract())

  print('\n')

  # Should be inserted as this is greater than the minimum in the heap and will be the maximum
  print('New element:', 20)
  klass.insert(20)
  print('Elements in the min heap:', klass.heap.array)
  print('Top N elements:', klass.extract())

  # Should not be inserted as it already exists in the heap
  print('New element:', 20)
  klass.insert(20)
  print('Elements in the min heap:', klass.heap.array)
  print('Top N elements:', klass.extract())

print('\n');
print('=================================== TopNElements with sample data #1 ===================================');
data5();