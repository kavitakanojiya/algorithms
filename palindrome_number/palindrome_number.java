class Solution {
    public boolean isPalindrome(int x) {
        // 1. Constraints
        // 1.1 Skip negative numbers
        // 1.2 First remainder should be greater than 0 and number should not be 0
        if((x < 0) || (x % 10 == 0 && x != 0)) {
            return false;
        }
        // 1.3 -2^31 <= x <= 2^31 - 1
        if(x > Integer.MAX_VALUE) {
            return false;
        }

        // 2. Quotient and Remainder will help to reverse the integer.
        // 2.1 Initialize the remainder to 0
        int dividend = 0;
        // 2.2 Run through halfway as long as x > dividend
        while(x > dividend) {
            // 2.3 Capture the remainder in the multiples of 10
            dividend = dividend * 10 + x % 10;
            // 2.4 Divide and reduce x by 10, 
            x /= 10;
        }

        // 3. Return true if:
        // 3.1 when x is even-sized and x will always be equal to dividend right at halfway
        // 3.2 when x is odd-sized, then dividend will be always be greater than x. So, factorize dividend by 10 and it will be equal to x
        // 3.3 Else, false
        if(dividend == x || (dividend / 10 == x)) {
            return true;
        }
        else {
            return false;
        }
    }
}