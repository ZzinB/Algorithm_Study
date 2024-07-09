import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int T = sc.nextInt();
        while (T-- > 0) {
            int n = sc.nextInt();
            int[][] stickers = new int[2][n];

            for (int i = 0; i < 2; i++) {
                for (int j = 0; j < n; j++) {
                    stickers[i][j] = sc.nextInt();
                }
            }

            System.out.println(getMaxScore(n, stickers));
        }
        
        sc.close();
    }

    private static int getMaxScore(int n, int[][] stickers) {
        if (n == 1) {
            return Math.max(stickers[0][0], stickers[1][0]);
        }

        int[][] dp = new int[2][n];
        dp[0][0] = stickers[0][0];
        dp[1][0] = stickers[1][0];
        dp[0][1] = stickers[1][0] + stickers[0][1];
        dp[1][1] = stickers[0][0] + stickers[1][1];

        for (int i = 2; i < n; i++) {
            dp[0][i] = Math.max(dp[1][i - 1], dp[1][i - 2]) + stickers[0][i];
            dp[1][i] = Math.max(dp[0][i - 1], dp[0][i - 2]) + stickers[1][i];
        }

        return Math.max(dp[0][n - 1], dp[1][n - 1]);
    }
}
