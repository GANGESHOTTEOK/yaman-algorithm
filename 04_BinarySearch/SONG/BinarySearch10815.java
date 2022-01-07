package algorithmStudy;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class BinarySearch10815 {
	static int[] card;
	static int N;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
		N = Integer.parseInt(br.readLine());
		card = new int[N];
		String[] temp = br.readLine().split(" ");
		for(int i=0; i<N; i++) {
			card[i] = Integer.parseInt(temp[i]);
		}
		Arrays.sort(card);
		
		StringBuilder result = new StringBuilder();
		int M = Integer.parseInt(br.readLine());
		temp = br.readLine().split(" ");
		for(int i=0; i<M; i++) {
			int num = binarySearch(Integer.parseInt(temp[i]));
			result.append(num + " ");
		}
		bw.write(result+"\n");
		bw.close();
		br.close();
	}

	private static int binarySearch(int num) {
		int start = 0;
		int end = N-1;
		
		while(start <= end) {
			int index = (start+end)/2;
			if(card[index] == num) {
				return 1;
			}
			else if(card[index] < num) {
				start = index+1;
			}
			else {
				end = index-1;
			}
		}
		return 0;
	}

}
