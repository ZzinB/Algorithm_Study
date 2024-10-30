import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        
        // 입력
        Scanner sc = new Scanner(System.in);
        
        int day = sc.nextInt();
        int[] cars = new int[5];
        for (int i = 0; i < 5; i++) {
            cars[i] = sc.nextInt();
        }
        
        int cnt = 0;
        
        for (int car : cars) {
            if (car == day) {
                cnt++; 
            }
        }
        
        System.out.println(cnt);
        
        sc.close();
    }
}
