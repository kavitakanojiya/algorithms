def armstrong_number(number):
  array = []
  initial_divisor = 10
  current_number = number
  quotient = number

  while quotient > 0:
    remainder = current_number % initial_divisor
    quotient = current_number / initial_divisor
    array.append(remainder)

    current_number = quotient
  
  cubic_sum = 0
  for element in array:
    cubic_value = element ** 3
    cubic_sum += cubic_value

  if cubic_sum == number:
    print('Armstrong number')
  else:
    print('Not an Armstrong number')

armstrong_number(153)
armstrong_number(370)
armstrong_number(371)
armstrong_number(372)
