def fibonacci(number):
  summation = 0
  next_number = 0
  previous_number = 0
  for num in (range(number - 1)):
    if num == 0:
      next_number = 0
      previous_number = 0
    elif num == 1:
      next_number = 1
      previous_number = 0
      summation = next_number + previous_number
    else:
      previous_number = next_number
      next_number = summation
      summation = next_number + previous_number

  return summation

print(fibonacci(8))
