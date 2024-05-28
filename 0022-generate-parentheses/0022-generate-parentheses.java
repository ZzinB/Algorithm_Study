class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        generate(result, "", n, n);
        return result;
    }

    // 괄호 조합(재귀)
    private void generate(List<String> result, String current, int open, int close) {
        // 남은 여는 괄호와 닫는 괄호의 수가 모두 0이 되면? -> 올바른 조합
        if (open == 0 && close == 0) {
            result.add(current);
            return;
        }

        // 여는 괄호를 추가할 수 있는 경우
        if (open > 0) {
            generate(result, current + "(", open - 1, close);
        }

        // 닫는 괄호를 추가할 수 있는 경우
        if (close > open) {
            generate(result, current + ")", open, close - 1);
        }
    }
}