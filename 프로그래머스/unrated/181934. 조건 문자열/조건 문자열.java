class Solution {
    public int solution(String ineq, String eq, int n, int m) {
        if ((ineq.equals(">") && eq.equals("=") && n >= m) ||
            (ineq.equals("<") && eq.equals("=") && n <= m) ||
            (ineq.equals(">") && eq.equals("!") && n > m) ||
            (ineq.equals("<") && eq.equals("!") && n < m)) {
            return 1;
        } else {
            return 0;
        }
    }
}