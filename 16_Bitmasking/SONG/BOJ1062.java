package bit;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ1062 {

	static int N, K, max=0;
	static String[] word;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		
		if(K < 5) {
			System.out.print(0);
			return;
		} else if(K == 26) {
			System.out.print(N);
			return;
		} else {
			word = new String[N];
			for(int i = 0; i < N; i++) {
				String input = br.readLine();
				word[i] = input.substring(4, input.length()-4);
			}
			
			int flag = 0;
			flag |= 1 << ('a'-'a');
			flag |= 1 << ('n'-'a');
			flag |= 1 << ('t'-'a');
			flag |= 1 << ('i'-'a');
			flag |= 1 << ('c'-'a');
			
			K -= 5;
			comb(0, 0, flag);
			
			System.out.print(max);
		}
	}
	
	public static void comb(int idx, int k, int flag) {
		if(k == K) {
			int cnt = 0;
			for(int i = 0; i < N; i++) {
				if(read(i, flag)) cnt++;
			}
			max = Math.max(max, cnt);
			return;
		}
		
		for(int i = idx; i < 26; i++) {
			if((flag & 1<<i) != 0) continue;
			comb(i+1, k+1, flag|(1<<i));
		}
	}
	
	public static boolean read(int idx, int flag) {
		for(int i = 0; i < word[idx].length(); i++) {
			if((flag & (1 << word[idx].charAt(i)-'a')) == 0) return false;
		}
		return true;
	}
}