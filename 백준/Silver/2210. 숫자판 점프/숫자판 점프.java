import java.util.Scanner;
import java.util.HashSet;

public class Main{
    static int[][] board = new int[5][5];
    static HashSet<String> nums = new HashSet<>();
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        //입력
        for (int i=0 ; i<5 ; i++){
            for(int j=0 ; j<5 ; j++){
                board[i][j] = sc.nextInt();
            }
        }
        
        for (int i=0 ; i<5 ; i++){
            for(int j=0 ; j<5 ; j++){
                dfs(i, j, "", 0);
            }
        }
        System.out.println(nums.size());
        sc.close();
    }
    
    static void dfs(int x, int y, String current, int depth){
        //6자리 만드면 종료
        if (depth == 6){
            nums.add(current);
            return;
        }
        
        // 현재 위치의 숫자를 문자열에 추가
        current += board[x][y];
        
        //상하좌우 이동
        for(int d=0 ; d<4 ; d++){
            int newX = x + dx[d];
            int newY = y + dy[d];
            
            //범위 내에서 다음 위치로 이동
            if (newX >= 0 && newY >= 0 && newX < 5 && newY < 5){
                dfs(newX, newY, current, depth+1);
            }
        }
    }
}