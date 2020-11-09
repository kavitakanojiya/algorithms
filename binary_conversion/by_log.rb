#### TODO:
# AIM: Convert a number into its binary form.

# Approack 1: Very simple
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
#  Start with x = 0
#  Max power to 2 closest to 5 is 2.
#  Capture in Hash as { 2 => 1 }
#  Deduct 5 - 2**2 = 1
#  Again, Max power to 2 closest to 1 is 0.
#  Capture in Hash as { 0 => 1 }
#  ... Repeat similarly unless we get 0 in the end as the least of power 2.
module BinaryConversion
  class ByLog
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
      power_to_x = 2**Math.log2(@number).ceil
      while true
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

p BinaryConversion::ByLog.new(number: 9).convert
#>> [1, 0, 0, 1]

# calculated incorrect
p BinaryConversion::ByLog.new(number: 100).convert
#>> [1, 1, 0, 0, 1, 0, 0]
