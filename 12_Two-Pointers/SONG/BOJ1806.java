package two_pointer;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ1806 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int S = Integer.parseInt(st.nextToken());
		
		int arr[] = new int[100001];
		st = new StringTokenizer(br.readLine());
		for(int i=0; i<N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		int min = 100000;
		int sum = 0, start = 0, end = 0;
		while(end <= N) {
			if(sum < S) {
				sum += arr[end++];
			}
			else {
				if(end - start < min) min = end - start;
				sum -= arr[start++];
			}
		}
		if(min == 100000) min = 0;
		System.out.print(min);
	
	}

}
