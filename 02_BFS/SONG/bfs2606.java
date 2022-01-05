package algorithmStudy;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;

public class bfs2606 {

	private static int n;
	private static int k;
	private static int[][] computer;
	private static int[] visit;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		n = Integer.parseInt(br.readLine());
		k = Integer.parseInt(br.readLine());
		
		computer = new int[n][n];
		visit = new int[n];
		
		/* input */
		for(int i=0; i<k; i++) {
			String[] temp = br.readLine().trim().split(" ");
			int c1 = Integer.parseInt(temp[0]);
			int c2 = Integer.parseInt(temp[1]);
			computer[c1-1][c2-1] = computer[c2-1][c1-1] = 1;
		}
		
		/* output */
		bw.write(""+bfs(0));
		bw.flush();
		bw.close();
	}
	
	public static int bfs(int c) {
		int count = 0;
		Queue<Integer> q = new LinkedList<Integer>();
		
		q.offer(c);
		while(!q.isEmpty()) {
			int x = q.poll();
			visit[x] = 1;
			for(int i=0; i<n; i++) {
				if(computer[x][i] == 1 && visit[i] != 1) {
					q.offer(i);
					visit[i] = 1;
					count++;
				}
			}
		}
		return count;
	}
}
