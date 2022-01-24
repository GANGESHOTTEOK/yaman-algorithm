package algorithmWeek2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ11727 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int dp[] = new int[1001];
		
		dp[1] = 1;
		dp[2] = 3;
		
		for(int i=3; i<=n; i++) {
			dp[i] = dp[i-1] + dp[i-2]*2;
			dp[i] = dp[i]%10007;
		}
		System.out.print(dp[n]);
	}

}
