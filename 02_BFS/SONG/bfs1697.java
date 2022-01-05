package algorithmStudy;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;

public class bfs1697 {

	private static int N;
	private static int K;
	private static int[] location = new int[100001];
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String[] temp = br.readLine().trim().split(" ");
		N = Integer.parseInt(temp[0]);
		K = Integer.parseInt(temp[1]);
		
		/* output */
		bw.write(""+bfs(N));
		bw.flush();
		bw.close();
	}
	
	public static int bfs(int n) {
		Queue<Integer> q = new LinkedList<Integer>();
		
		q.offer(n);
		location[n] = 0;
		
		while(!q.isEmpty()) {
			int x = q.poll();
			
			if(x == K) {
				return location[x];
			}
			if(0 <= x-1 && location[x-1] == 0) { //x-1
				q.offer(x-1);
				location[x-1] = location[x]+1; // +1sec
			}
			if(x+1 <= 100000 && location[x+1] == 0) { // x+1
				q.offer(x+1);
				location[x+1] = location[x]+1;
			}
			if(2*x <= 100000 && location[2*x] == 0) { // 2*x
				q.offer(2*x);
				location[2*x] = location[x]+1;
			}
		}
		return -1; // fail
	}
}
