package algorithmWeek2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ11057 {
	// 1로끝나면 1~9 3으로 끝나면 그뒤에 3~9,, 이렇게 올 수 있으니까..
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        
        int dp[] = new int[11];
        dp[0] = 1; // 0으로 끝나는 오르막수의 개수
        while(n >= 0) {
        	for(int i=1; i<10; i++) { // 1~9로 끝나는 오르막수 개수 갱신
        		dp[i] = (dp[i-1] + dp[i]) % 10007;
        	}
        	n--;
        }
        System.out.println(dp[9]); // n자리까지 왔을 때 9로 끝나는 개수까지 다 더한값
	}
}
