class Solution {
    public int maximalSquare(char[][] matrix) {
        int n = matrix.length;
        if (n == 0) return 0;
        int m = matrix[0].length;

        int[] dp = new int[m + 1];
        int max = 0, prev = 0;

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                int temp = dp[j];
                if (matrix[i - 1][j - 1] == '1') {
                    // dp[j] 값을 갱신, 현재 위치에서 가능한 가장 큰 정사각형의 변의 길이 계산
                    dp[j] = Math.min(dp[j], Math.min(dp[j - 1], prev)) + 1;
                    // 최대 변의 길이 갱신
                    max = Math.max(dp[j], max);
                } else {
                    // 행렬의 현재 값이 '0'인 경우, dp[j]를 0으로 설정
                    dp[j] = 0;
                }
                // prev를 갱신하여 다음 열의 dp[j-1]로 사용
                prev = temp;
            }
        }
        // 가장 큰 정사각형의 면적 반환
        return max * max;
    }
}