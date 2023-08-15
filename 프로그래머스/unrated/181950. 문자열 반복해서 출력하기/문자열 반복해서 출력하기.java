import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        int n = sc.nextInt();
        
        String repeatedString = "";
        for (int i = 0; i < n; i++) {
            repeatedString += str;
        }

        System.out.println(repeatedString);
    }
}