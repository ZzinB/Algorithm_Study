import java.util.*;
import java.io.*;

public class Main {
	static int[] parent;
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int m = Integer.parseInt(br.readLine());
		
		int[][] arr = new int[n + 1][n + 1];
		for(int i = 1; i <= n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for(int j = 1; j <= n; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		int[] route = new int[m + 1];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i = 1; i <= m; i++) {
			route[i] = Integer.parseInt(st.nextToken());
		}
		
		parent = new int[n + 1];
		for(int i = 1; i <= n; i++) {
			parent[i] = i;
		}
		
		for(int i = 1; i <= n; i++) {
			for(int j = 1; j <= n; j++) {
				if(arr[i][j] == 1) {
					union(i, j);
				}
			}
		}
		// 여행 계획 도시들이 1개의 대표 도시로 연결돼 있는지 확인하기 
		int index = find(route[1]);
		for(int i = 2; i < route.length; i++) {
			if(index != find(route[i])) {
				System.out.println("NO");
				return;
			}
		}
		System.out.println("YES");
	}

	private static void union(int i, int j) {
		i = find(i);
		j = find(j);
		if(i != j) {
			parent[j] = i;
		}
	}

	private static int find(int j) {
		if(parent[j] == j) {
			return j;
		}
		else {
			return parent[j] = find(parent[j]);
		}
	}
}
