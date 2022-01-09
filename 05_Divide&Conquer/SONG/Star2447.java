package algorithmStudy;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Star2447 {

	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(br.readLine());
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				star(i, j);
			}
			sb.append("\n");
		}
		bw.write(sb+"\n");
		bw.close();
	}

	static void star(int y, int x) {
		while (true) {
			if (y == 0)
				break;
			if (y % 3 == 1 && x % 3 == 1) {
				sb.append(" ");
				return;
			}
			y /= 3;
			x /= 3;
		}
		sb.append("*");
	}
}
