package two_pointer;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ2003 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		int arr[] = new int[10001];
		st = new StringTokenizer(br.readLine());
		for(int i=0; i<N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		int sum = 0, start = 0, end = 0;
		int cnt = 0;
		while(end <= N) {
			if(sum < M) {
				sum += arr[end++];
			}
			else if(sum > M) {
				sum -= arr[start++];
			}
			else {
				cnt++;
				sum -= arr[start++];
			}
		}
		
		System.out.print(cnt);
	}

}
