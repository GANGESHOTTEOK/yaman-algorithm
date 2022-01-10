package algorithmWeek2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Lotto {
	static StringBuilder sb = new StringBuilder();
	static int k = 1; //while
	static int[] S;
	static int[] answer;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
		while(k != 0) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			k = Integer.parseInt(st.nextToken());
			S = new int[k];
			answer = new int[6];
			for(int i=0; i<k; i++) {
				S[i] = Integer.parseInt(st.nextToken());
			}
			
			DFS(0,0);
			sb.append("\n");
		}
		br.close();
		
		System.out.println(sb);
	}
	
	public static void DFS(int d, int v) {
		if(d == 6) {                	// 깊이가 6이면 하나의 경우의 수를 다 찾았으므로 답에 추가하고 리턴
			for(int num : answer) {		// 그러면 직전(깊이 5)으로 돌아가서 다른 수로 넘어감
				sb.append(num + " ");
			}
			sb.append("\n");
		}
		else {
			for(int i=v; i<k; i++) {
				answer[d] = S[i];
				DFS(d+1, i+1);
			}
		}
	}
}
