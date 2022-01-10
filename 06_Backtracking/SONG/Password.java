package algorithmWeek2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Password {

	static char[] arr;
	static boolean[] tf;
	static int c, l;
	
	public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] temp = br.readLine().trim().split(" ");
        l = Integer.parseInt(temp[0]);
        c = Integer.parseInt(temp[1]);

		arr = new char[c];
		tf = new boolean[c];

		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < c; i++) {
			arr[i] = st.nextToken().charAt(0);
		}
		Arrays.sort(arr);
		
		dfs(0, 0, 0, 0);
		br.close();
	}

	public static void dfs(int start, int depth, int consonant, int vowel) {

		for (int i = start; i < c; i++) {
			tf[i] = true;
			if (arr[i] == 'a' || arr[i] == 'e' || arr[i] == 'i' || arr[i] == 'o' || arr[i] == 'u')
				dfs(i + 1, depth + 1, consonant, vowel + 1);
			else
				dfs(i + 1, depth + 1, consonant + 1, vowel);
			tf[i] = false;
		}
		
		if (depth == l && consonant >= 2 && vowel >= 1) {
			for (int i = 0; i < c; i++) {
				if (tf[i] == true)
					System.out.print(arr[i]);
			}
			System.out.println("");
			return;
		}

	}
}