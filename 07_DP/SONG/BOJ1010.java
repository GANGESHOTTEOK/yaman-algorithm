package algorithmWeek2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ1010 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int[][] dp = new int[30][30];
		for(int i=0; i<30; i++) {
			dp[i][0] = 1;
			dp[i][i] = 1;
		}
		for(int i=2; i<30; i++) {
			for(int j=1; j<30; j++) {
				dp[i][j] = dp[i-1][j-1] + dp[i-1][j];
			}
		}
		
		int N = Integer.parseInt(br.readLine());
		for(int testcase=0; testcase<N; testcase++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			int W = Integer.parseInt(st.nextToken());
			int E = Integer.parseInt(st.nextToken());
			
			sb.append(dp[E][W] + "\n");
		}
		
		System.out.print(sb);
	}
}
