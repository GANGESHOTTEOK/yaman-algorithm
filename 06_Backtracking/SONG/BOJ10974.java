package algorithmWeek2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ10974 {
	static int N;
	static boolean[] checked;
	static int[] answer;
	static StringBuilder sb;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
		N = Integer.parseInt(br.readLine());
		checked = new boolean[N];
		answer = new int[N];
		
		sb = new StringBuilder();
		permutation(0);
		
		System.out.print(sb);
	}
	
	static void permutation(int count) {
        if(count == N) {
        	for(int num : answer)
        		sb.append(num + " ");
        	sb.append("\n");
        	return;
        }

        for (int i = 0; i < N; i++) {
            if(checked[i]) continue;
            answer[count] = i+1;
            checked[i] = true;
            permutation(count + 1);
            checked[i] = false;
        }
    }
}
