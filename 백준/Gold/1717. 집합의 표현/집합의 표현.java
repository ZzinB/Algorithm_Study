import java.util.*;
import java.io.*;

public class Main{
    public static int[] parent;
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        parent = new int[N+1];
        for (int i=0 ; i<=N ; i++){ //대표 노드를 자신으로 초기화
            parent[i] = i;
        }
        for(int i=0 ; i<M ; i++){
            int question = sc.nextInt();
            int a = sc.nextInt();
            int b = sc.nextInt();
            if(question == 0){ //집합 1개로 합치기
                union(a, b);
            }else{  //가튼 집합의 원소인지 확인
                if(checksame(a, b)){
                    System.out.println("YES");
                }else{
                    System.out.println("NO");
                }
            }
        }
    }
    public static void union(int a, int b){ //union연산
        a = find(a);
        b = find(b);
        if (a != b){
            parent[b] = a;
        }
    }
    public static int find(int a){ //find연산
        if(a == parent[a])
            return a;
        else
            return parent[a] = find(parent[a]);
    }
    public static boolean checksame(int a, int b){
        a = find(a);
        b = find(b);
        if(a == b){
            return true;
        }
        return false;
    }
}