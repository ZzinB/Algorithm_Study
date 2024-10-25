import java.util.Scanner;

public class Main{
    static int cnt = 0;
    
    public static void main(String[] args){
        //입력
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int S = sc.nextInt();
        int[] nums = new int[N];
        
        for(int i=0 ; i<N ; i++){
            nums[i] = sc.nextInt();
        }
        
        solution(nums, N, S, 0, 0);
        
        if (S == 0) cnt--;
        
        System.out.println(cnt);
    }
    
    //부분수열의 합
    static void solution(int[] nums, int N, int S, int index, int sum){
        if(index == N){
            if(sum == S) cnt++;
            return;
        }
        //현재 원소 포함하지 않음
        solution(nums, N, S, index+1, sum);
        //현재 원소 포함
        solution(nums, N, S, index+1, sum+nums[index]);
    }
}