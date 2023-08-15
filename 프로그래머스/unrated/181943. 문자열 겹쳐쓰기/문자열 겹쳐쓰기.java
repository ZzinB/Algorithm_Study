class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        StringBuilder result = new StringBuilder(my_string);
        
        for (int i = s, j = 0; j < overwrite_string.length(); i++, j++) {
            result.setCharAt(i, overwrite_string.charAt(j));
        }
        
        return result.toString();
    }
}