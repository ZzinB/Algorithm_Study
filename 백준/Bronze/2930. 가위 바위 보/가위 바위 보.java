import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N; // 친구의 수
    static int R; // 라운드 수

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // 라운드 수 입력
        R = Integer.parseInt(br.readLine());
        // 상근이의 손 모양 입력
        char[] sanggeun = br.readLine().toCharArray();

        // 친구의 수 입력
        N = Integer.parseInt(br.readLine());
        char[][] friends = new char[N][R]; // 친구들의 손 모양을 저장할 배열
        for(int i = 0; i < N; i++){
            friends[i] = br.readLine().toCharArray(); // 각 친구의 손 모양 입력
        }

        // 실제 점수 계산
        int score = 0;
        for(int j = 0; j < R; j++){
            for(int i = 0; i < N; i++){
                score += getScore(sanggeun[j], friends[i][j]); // 점수 계산
            }
        }

        // 최적의 점수 계산
        int bestScore = 0;
        for(int j = 0; j < R; j++){
            int rScore = 0; // 바위로 이길 점수
            int sScore = 0; // 가위로 이길 점수
            int pScore = 0; // 보로 이길 점수
            for(int i = 0; i < N; i++){
                rScore += getScore('R', friends[i][j]);
                sScore += getScore('S', friends[i][j]);
                pScore += getScore('P', friends[i][j]);
            }
            // 최대 점수 선택
            bestScore += Math.max(rScore, Math.max(sScore, pScore));
        }

        // 결과 출력
        System.out.println(score);
        System.out.println(bestScore);
    }

    // 점수 계산 메서드
    public static int getScore(char sanggeun, char friend) {
        if(sanggeun == friend)
            return 1; // 비김
        switch (sanggeun) {
            case 'R':
                return friend == 'S' ? 2 : 0; // 바위 vs 가위
            case 'S':
                return friend == 'P' ? 2 : 0; // 가위 vs 보
            case 'P':
                return friend == 'R' ? 2 : 0; // 보 vs 바위
            default: 
                return 0; // 잘못된 입력에 대한 기본값
        }
    }
}
