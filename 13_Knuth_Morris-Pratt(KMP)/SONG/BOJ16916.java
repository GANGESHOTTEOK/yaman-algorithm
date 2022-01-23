package KMP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ16916 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String S = br.readLine();
		String P = br.readLine();
		
		int[] pattern = new int[P.length()];
		
		int j = 0;
		for(int i=1; i<P.length(); i++) {
			while(j > 0 && P.charAt(i) != P.charAt(j)) {
				j = pattern[j-1];
			}
			if(P.charAt(i) == P.charAt(j)) pattern[i] = ++j;
		}
		
		j = 0;
		for(int i=0; i<S.length(); i++) {
			while(j > 0 && S.charAt(i) != P.charAt(j)) j = pattern[j-1];
			if(S.charAt(i) == P.charAt(j)) {
				if(j == P.length()-1) {
					System.out.print(1);
					return;
				}
				else {
					++j;
				}
			}
		}
		
		System.out.println(0);
	}
}
