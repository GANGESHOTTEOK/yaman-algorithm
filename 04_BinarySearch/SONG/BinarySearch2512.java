package algorithmStudy;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class BinarySearch2512 {
	static int[] request;
	static int N, M;	
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
		N = Integer.parseInt(br.readLine());
		request = new int[N];
		
		String[] temp = br.readLine().split(" ");
		for(int i=0; i<N; i++) {
			request[i] = Integer.parseInt(temp[i]);
		}
		
		Arrays.sort(request);
		
		M = Integer.parseInt(br.readLine());
		int limit = binarySearch();
		
		bw.write(""+limit);
		bw.close();
	}
	
	private static int binarySearch() {
		int start = 0;
		int end = request[N-1];
		int limit = 0;
		
		while(start <= end) {
			int mid = (start+end)/2; //current limit
			int total = 0;
			
			for(int i=0; i<N; i++) {
				if(mid > request[i]) {
					total += request[i];
				}
				else {
					total += mid;
				}
			}
			
			if(total > M) {
				end = mid - 1;
			}
			else if(total <= M) {
				limit = mid;
				start = mid + 1;
			}
		}
		return limit;
	}

}
