class Solution:
  def reverse(self, x: int) -> int:
    is_neg = x < 0
    
    if is_neg == True:
      x = x*(-1)

    reverse = 0
    while(x != 0):
      remainder = x % 10
      x =  x // 10
      reverse = reverse * 10 + remainder

    if is_neg == True:
      reverse = reverse*(-1)

    if((reverse >= -2**31) and (reverse <= (2**31 - 1))) == False:
      return 0
    else:
      return(reverse)

klass = Solution()

# Reversing `2147483648` overflows, returning 0
output = klass.reverse(2147483648)
print("2147483648:", output)

# Reversing `123` is a valid 32-bit signed integer
output = klass.reverse(123)
print("123:", output)

# Reversing `-123` is a valid 32-bit signed integer, maintaining the sign as is
output = klass.reverse(-123)
print("-123:", output)

# Reversing `-2147483648` is not a valid 32-bit signed integer, returning 0
output = klass.reverse(-2147483648)
print("-2147483648:", output)
