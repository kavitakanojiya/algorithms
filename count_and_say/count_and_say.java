
class Solution {
    public String countAndSay(int n) {
        // Start from input "1".
        String input = "1";

        // As per the constraint: 1 <= n <= 30.
        if(n > 0 && n <= 30) {
            // Loop starts from 0. However, counting starts from the second iteration.
            int i = 1;
            // Iterate recursively.
            while(i < n) {
                input = transform(input);
                // Increment i.
                i++;
            }
        }

        // If constraint is not satisfied, "1" is returned.
        return input; 
    }

    public String transform(String str) {
        // 1. Convert string to an char array
        char[] char_array = str.toCharArray();
        // 2. Caret is set to the first element of the character array.
        // This ensures the first element as visited in the array.
        char caret = char_array[0];
        // 3. Captures the occurrences of the character.
        // Since we defaulted current character to the first element, current counter is set to 1.
        int current_counter = 1;
        StringBuilder sb = new StringBuilder();

        // 4. Start from the second element in the character array
        for(int i = 1; i < char_array.length; i++) {
            // 4.1 IF: Increment the current counter if the current element matches with the caret
            // This means we are still seeing the occurrences of the caret.
            if(char_array[i] == caret) {
                current_counter += 1;
            }
            // 4.2 ELSE: If the current element does not match with the caret, push the number of occurrences and the caret to the string builder.
            else {
                sb.append(Integer.toString(current_counter));
                sb.append(caret);
                // 4.3 Initialize the caret to the current element and increment the current_counter.
                caret = char_array[i];
                current_counter = 1;
            }
        }

        // 5. Last element will be unvisited from 4.3.
        // Capturing the caret and current counter as it is.
        sb.append(Integer.toString(current_counter));
        sb.append(caret);

        // 6. Form a string.
        return sb.toString();
    }
}
