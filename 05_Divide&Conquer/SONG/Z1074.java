package algorithmStudy;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Z1074 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String[] temp = br.readLine().split(" ");
		int N = Integer.parseInt(temp[0]);
		int r = Integer.parseInt(temp[1]);
		int c = Integer.parseInt(temp[2]);

		bw.write(""+z(N, r, c));
		bw.close();
	}
	
	public static int z(int N, int r, int c) {
		if(N == 0) {
			return 0;
		}
		else {
			int d = 1<<(N-1);
			if(r<d && c<d) {
				return z(N-1, r, c);
			}
			else if(r<d && c>=d) {
				return (d*d) + z(N-1, r, c-d);
			}
			else if(r>=d && c<d) {
				return (d*d*2) + z(N-1, r-d, c);
			}
			else {
				return (d*d*3) + z(N-1, r-d, c-d);
			}
		}
	}

}
