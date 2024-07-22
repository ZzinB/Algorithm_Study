import java.io.*;
import static java.lang.Integer.parseInt;

public class Main {
    static final int SEAT = 41;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = parseInt(br.readLine());
        int m = parseInt(br.readLine());

        int[] vip = new int[m]; // 고정석 저장
        int[] dp = new int[SEAT]; // dp 초기화 41개 좌석
        
        for (int i = 0; i < m; i++) vip[i] = parseInt(br.readLine()); // vip 입력 받기
        
        dp[0] = 1;
        dp[1] = 1;
        dp[2] = 2;
        
        for (int i = 3; i <= n; i++) dp[i] = dp[i - 1] + dp[i - 2]; // n번까지 설정
        
        int answer = 1; // n == 1일 때 answer는 1
        
        int preIdx = 0; // 곱셉을 위한 이전 위치
        for (int idx : vip) {
            answer *= dp[idx - preIdx - 1]; // 인덱스 - 이전 인덱스 - 1을 함으로써 연속된 좌석을 길이 구하기
            preIdx = idx; // 인덱스를 업데이트하여 dp 길이
        }
        
        answer *= dp[n - preIdx]; // 마지막 고정석으로부터 연속된 좌석 dp
        System.out.println(answer);
    }
}