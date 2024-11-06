import java.util.*;

public class Main {
    static int N;
    static int[][] S;
    static int result = Integer.MAX_VALUE;
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 입력 받기
        N = sc.nextInt();
        S = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                S[i][j] = sc.nextInt();
            }
        }

        // 팀을 나누는 함수 호출
        divideTeams(0, 0, new boolean[N]);

        // 결과 출력
        System.out.println(result);
        sc.close();
    }

    // 팀을 나누는 함수
    static void divideTeams(int idx, int cnt, boolean[] team) {
        // 스타트팀에 N/2명이 선택되면 링크팀은 나머지 사람들로 자동으로 결정됨
        if (cnt == N / 2) {
            solution(team);
            return;
        }

        // idx부터 시작하여 N명 중에서 N/2명을 선택
        for (int i = idx; i < N; i++) {
            if (!team[i]) {
                team[i] = true; // 스타트팀에 포함
                divideTeams(i + 1, cnt + 1, team);
                team[i] = false; // 선택하지 않음
            }
        }
    }

    // 능력치 차이 계산 함수
    static void solution(boolean[] team) {
        int start = 0;
        int link = 0;

        // 스타트팀 능력치 계산
        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                if (team[i] && team[j]) {
                    start += S[i][j] + S[j][i];
                } else if (!team[i] && !team[j]) {
                    link += S[i][j] + S[j][i];
                }
            }
        }

        // 능력치 차이 계산
        int diff = Math.abs(start - link);
        result = Math.min(result, diff);
    }
}
