def convert(number):
  remainders = []
  current_number = number
  to_binary = []

  while True:
    quotient  = current_number / 2
    remainder = current_number % 2
    current_number = quotient
    remainders.append(remainder)

    if quotient == 1 or quotient == 0:
      break

  if quotient != 0:
    to_binary.append(quotient)
  to_binary += remainders[::-1]

  print(''.join(str(element) for element in to_binary))

convert(8)
# convert(1)
