class Solution {
    public int hammingDistance(int x, int y) {
        int counter = 0;
        int integer_size = 32;
        for(int i = 0; i < integer_size; i++) {
            if((x & 1) != (y & 1)) {
                counter += 1;
            }
            x >>= 1;
            y >>= 1;
        }
        return counter;
    }
}
