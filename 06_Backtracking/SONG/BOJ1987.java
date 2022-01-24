package algorithmWeek2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ1987 {
	static int R, C;
	static int[][] board;
	static boolean[] alpha;
	static int[] dx = {0, 0, -1, 1};
	static int[] dy = {-1, 1, 0, 0};
	static int max = 1;
	static int count = 1;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		
		alpha = new boolean[26]; // 알파벳 대문자는 26개
		board = new int[R][C];
		for(int i=0; i<R; i++) {
			String temp = br.readLine();
			for(int j=0; j<C; j++) {
				board[i][j] = temp.charAt(j) - 'A';
			}
		}
		DFS(0,0);
		System.out.println(max);	
	}
	
	static void DFS(int y, int x) {
		alpha[board[y][x]] = true;
		
		for(int i=0; i<4; i++) {
			int X = dx[i] + x;
			int Y = dy[i] + y;
			
			if(X < 0 || Y < 0 || X >= C || Y >= R) continue;
			if(alpha[board[Y][X]]) continue;
			
			if(max < count+1) max = count + 1;
			count += 1;
			DFS(Y, X);
		}
		count--;
		alpha[board[y][x]] = false;
	}
}
