import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class Main{
    //생성된 조합 저장
    static List<List<Integer>> results = new ArrayList<>();
    //현재 선택된 숫자 저장
    static int[] selectedNumbers;
    
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        while(true){
            //입력
            String input = sc.nextLine();
            //종료 조건 : 입력이 0일 때
            if (input.equals("0")){
                break;
            }
            
            String[] parts = input.split(" ");
            //첫 번째 숫자(k) : 숫자의 개수 
            int k = Integer.parseInt(parts[0]);
            int[] S = new int[k];
            for (int i=0 ; i<k ; i++){
                S[i] = Integer.parseInt(parts[i+1]);
            }
            
            //6개 숫자 선택 배열 초기화
            selectedNumbers = new int[6];
            //이전 테스트 케이스 결과 초기화
            results.clear();
            //조합 생성
            backtrack(S, 0, 0);
            
            //결과 출력
            for (List<Integer> comb : results){
                for (int num : comb){
                    System.out.print(num + " ");
                }
                System.out.println();
            }
            System.out.println();
        }
        sc.close();
    }
    
    //조합 생성
    static void backtrack(int[] S, int start, int depth){
        //6개 숫자가 선택되면 결과 저장
        if(depth == 6){
            List<Integer> comb = new ArrayList<>();
            for (int num : selectedNumbers){
                comb.add(num);
            }
            results.add(comb);
            return;
        }
        //조합
        for(int i=start ; i<S.length ; i++){
            //현재 숫자 선택
            selectedNumbers[depth] = S[i];
            //다음 숫자 선택
            backtrack(S, i+1, depth+1);
        }
    }
}