import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        //입력받기
        String input = sc.nextLine();
        String[] nums = input.split(" ");
        
        //비내림차순인지 판별
        boolean isNonDecreasing = true;
        for (int i=1 ; i<nums.length ; i++){
            int current = Integer.parseInt(nums[i]);
            int previous = Integer.parseInt(nums[i-1]);
            if (current < previous){
                isNonDecreasing = false;
                break;
            }
        }
        
        //결과
        if (isNonDecreasing){
            System.out.println("Good");
        } else{
            System.out.println("Bad");
        }
        
        sc.close();
    }
}