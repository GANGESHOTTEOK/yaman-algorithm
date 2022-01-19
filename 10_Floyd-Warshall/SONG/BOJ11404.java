package floyd_warshall;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ11404 {
	static int N, M;
	static int arr[][];
	static final int INF = 1000000000;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		M = Integer.parseInt(br.readLine());
		
		arr = new int[N+1][N+1];
		for(int i=1; i<=N; i++) {
			for(int j=1; j<=N; j++) {
				if(i == j) continue;
				arr[i][j] = INF;
			}
		}
		
		while(M-->0) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			arr[a][b] = Math.min(arr[a][b], c);
		}
		
		floyd();
		
		StringBuilder sb = new StringBuilder();
		for(int i=1; i<=N; i++) {
			for(int j=1; j<=N; j++) {
				if(arr[i][j] >= INF) sb.append("0 ");
			    else sb.append(arr[i][j] + " ");
			}
			sb.append("\n");
		}
		System.out.print(sb.toString());
	}
	
	static void floyd() {
		for(int k=1; k<=N; k++) {
			for(int i=1; i<=N; i++) {
				for(int j=1; j<=N; j++) {
					arr[i][j] = Math.min(arr[i][j],  arr[i][k] + arr[k][j]);
				}
			}
		}
	}
}
