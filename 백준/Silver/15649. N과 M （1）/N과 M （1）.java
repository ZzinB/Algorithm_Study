import java.util.*;

public class Main {
    static int N, M; // N: 자연수의 범위, M: 수열의 길이
    static boolean[] visited; // 각 수의 선택 여부
    static List<Integer> seq = new ArrayList<>(); // 현재 수열

    public static void main(String[] args) {
        //입력
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt(); 
        M = sc.nextInt(); 
        visited = new boolean[N + 1]; 
        
        solution(0); // 수열 생성 시작
    }

    static void solution(int depth) {
        // 종료(출력)조건 : 현재 선택한 수의 개수가 M과 같으면 
        if (depth == M) {
            for (int num : seq) {
                System.out.print(num + " "); 
            }
            System.out.println();
            return;
        }
        
        // 1부터 N까지의 수를 반복
        for (int i = 1; i <= N; i++) {
            if (!visited[i]) { // 아직 선택되지 않은 수일 경우
                visited[i] = true; // 수를 선택
                seq.add(i); // 수열에 수 추가
                solution(depth + 1); // 다음 수 선택
                seq.remove(seq.size() - 1); // 마지막 수 제거 (백트래킹)
                visited[i] = false; 
            }
        }
    }
}
