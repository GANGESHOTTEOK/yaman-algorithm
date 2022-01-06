package algorithmStudy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class greedy1946 {
	static int T;
	static int N;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		T = Integer.parseInt(br.readLine());
		
		for(int t=0; t<T; t++) {
			N = Integer.parseInt(br.readLine());
			ArrayList<int[]> p = new ArrayList<int[]>();	

			/* input */
			for(int i=0; i<N; i++) {
				String[] temp = br.readLine().trim().split(" ");
				p.add(new int[] {Integer.parseInt(temp[0]), Integer.parseInt(temp[1])});
			}
		
			Collections.sort(p, new Comparator<int[]>() {
				@Override
	            public int compare(int[] o1, int[] o2) {
	                return o1[0] - o2[0];
	            }
			});
						
			int count = 1;
			int cutline = p.get(0)[1];
			for(int i=1; i<N; i++) {
				if(p.get(i)[1] < cutline) {
					count++;
					cutline = p.get(i)[1];
				}
			}
			
			System.out.println(count);
		}
	}
}
