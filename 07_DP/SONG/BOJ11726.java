package algorithmWeek2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ11726 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		if(n == 1) System.out.print(1);
		else{
			int dp[] = new int[n+1];
		
			dp[1] = 1;
			dp[2] = 2;
			for(int i=3;i<=n;i++) {
				dp[i] = dp[i-1] + dp[i-2];
				dp[i] = dp[i]%10007;
			}
			System.out.print(dp[n]);
		}
		br.close();
	}

}
