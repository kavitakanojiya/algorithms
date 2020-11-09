# palindrome: when the word is odd in count.
# word = "madam"

# palindrome: when the word is even in count.
word = 'redder'

# !palindrome: when the word is odd in count.
# word = 'radac'

# !palindrome: when the word is even in count.
# word = 'proble'

length   = len(word)
quotient = length / 2;

output = True

for index in range(quotient):
  current_character  = word[index].lower()
  opposite_character = word[(length - 1) - index].lower()

  if current_character == opposite_character:
    output = output & True
  else:
    output = output & False
  

if output == True:
  print('palindrome: {}').format(word)
else:
  print('not palindrome: {}').format(word)
