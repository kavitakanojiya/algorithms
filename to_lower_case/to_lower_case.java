class Solution {
    public String toLowerCase(String str) {
        char[] char_array = str.toCharArray();
        StringBuilder builder = new StringBuilder();
        for(char x : char_array) {
            if(isUpperCase(x)){
                char lower_chr = toLowerCase(x);
                builder.append(lower_chr);
            }
            else {
                builder.append(x);
            }
        }

        return builder.toString();
    }
    
    public boolean isUpperCase(char chr) {
        return 'A' <= chr && chr <= 'Z';
    }
    
    public char toLowerCase(char chr) {
        int ascii = (int)chr + 32;
        char lower_case = (char) ascii;
        return lower_case;
    }
}
