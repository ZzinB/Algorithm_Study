import java.util.Scanner;
import java.util.Stack;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        //입력
        int T = sc.nextInt();
        sc.nextLine();
        
        for(int i=0 ; i<T ; i++){
            String input = sc.nextLine();
            System.out.println(solution(input) ? "YES" : "NO");
        }
        sc.close();
    }
    
    private static boolean solution(String s){
        Stack<Character> stack = new Stack<>();
        
        //문자열의 각 문자에 대해
        for(char ch : s.toCharArray()){
            //'(' 스택에 추가
            if(ch == '('){
                stack.push(ch);
            } else if(ch == ')'){
                if(stack.isEmpty()){
                    //스택이 비어있으면 짝이 없는 ')'
                    return false;
                }
                //짝이 맞는 '('는 제거
                stack.pop();
            }
        }
        return stack.isEmpty();
    }
}