'''
Ask:
In a calendar, events are scheduled. There are a few overalapping events. Merge the overalapping events into one event taking the minimum of the start time and maximum of the end time.

Input:
[[6, 7], [7, 8], [8, 10], [9, 11], [10, 14], [14, 15], [16, 17]]

Output:
[[6, 7], [7, 8], [8, 14], [14, 15], [16, 17]]

Considerations:
1. Time is in am-pm format.
2. Events are in sorted order.
'''

array = [[6, 7], [7, 8], [8, 10], [9, 11], [10, 14], [14, 15], [16, 17]]

stack  = list()
output = []

length = len(array)

for index in range(length):
  is_last_index = index == length - 1
  if stac
  print('index: {}, element: {}, next element: {}, is_last_index: {}').format(index, array[index], array[index+1], is_last_index)
