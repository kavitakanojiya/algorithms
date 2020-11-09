# AIM: Convert a number into its binary form.

# Approack 2: Very simple
# Binary represents in the form of 0 and 1.
# The idea is to grab the nearest power of 2 that is less than expected number and decrement henceforth.
# For example, 
# 1. Start from x = 0
# 2. Either a number will be a perfect power of 2 or lie nearby
# 3. If a number is a perfect power of 2:
#    3.a Then assign the power position with 1 and exit.
# 4. If a number lies nearby of powers of 2:
#    4.a Find nearest powers of 2 that is less than expected number.
#    4.b Collect this power in hash.
#    4.c Start decrementing by the powersf of 2.
# Example:
#  Number = 5, Hash = {}
#  Divide by 2 to limit the extent we calculate 2**x i.e quotient
#  Start with quotient until we reach a number that will return 2**quotient and decrement it.
#    Every value decremented must override quotient.
#    Do this until we get 2**quotient that is less than a number.
#    Once we achieve `quotient`, capture this quotient and mark it as 1 to represent binary form of that power.
#    Deduct 2**quotient from number such that we now calcluate for the remaining limit.
#  Do this repeatitively until we have quotient == 1.
#  Break
#  Generate an array with values as 1 and 0 accordingly.
module BinaryConversion
  class MaxPowerTo2
    def initialize(number:)
      @number = number
      @binary_hash = {}
    end

    def convert
      iterate
      polish
    end

    def iterate
      quotient = @number/2
      power_to_x = 2**quotient
      while true
        power_to_x = 2**quotient

        if power_to_x > @number
          quotient = quotient - 1
          power_to_x = 2**quotient
        else
          @binary_hash.merge!(quotient => 1)
          @number = @number - 2**quotient
          quotient = quotient - 1
        end
        if quotient == -1
          break
        end
      end
    end

    def polish
      # create an array of max position in `y`
      binary = Array.new(@binary_hash.keys.max)
      # Insert element in `binary` matching position in `y`
      @binary_hash.each do |key, value|
        binary[key] = value
      end
      # Replace all nil values with 0 in `binary`
      binary.each_with_index do |value, index|
        binary[index] = 0 if binary[index].nil?
      end

      binary.reverse!
    end
  end
end

p BinaryConversion::MaxPowerTo2.new(number: 9).convert
#>> [1, 0, 0, 1]

p BinaryConversion::MaxPowerTo2.new(number: 100).convert
#>> [1, 1, 0, 0, 1, 0, 0]
