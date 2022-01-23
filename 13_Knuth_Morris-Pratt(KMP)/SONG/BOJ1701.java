package KMP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ1701 {
	static int result = -1;

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		
		for(int i=0; i<str.length(); i++) {
			result = Math.max(result, kmp(str.substring(i, str.length())));
		}
		
		System.out.println(result);
	}
	
	private static int kmp(String s) {
		int j = 0;
		int max = 0;
		int table[] = new int[s.length()];
		
		for(int i=1; i<s.length(); i++) {
			while(j > 0 && s.charAt(i) != s.charAt(j)) {
				j = table[j - 1];
			}
		
			if(s.charAt(i) == s.charAt(j)) {
				max = Math.max(max, table[i] = ++j);
			}
		}
		return max;
	}

}
