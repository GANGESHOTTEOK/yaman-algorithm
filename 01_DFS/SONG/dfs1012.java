package algorithmStudy;

import java.util.ArrayList;
import java.util.Scanner;

public class dfs1012 {
	static int T, M, N, K;
	static int[][] map;
	static int cnt;
	
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		T = input.nextInt();
		
		for(int t=0; t<T; t++) {	
			M = input.nextInt();
			N = input.nextInt();
			K = input.nextInt();
			map = new int[M][N];
			cnt = 0;
			
			/* input */
			for(int i=0; i<K; i++) {
				int x = input.nextInt();
				int y = input.nextInt();
				map[x][y] = 1;
			}
			
			for(int i=0; i<M; i++) {
				for(int j=0; j<N; j++) {
					if(map[i][j] == 1) {
						cnt++;
						dfs(i,j);
					}
				}
			}
			
			System.out.println(cnt);
		}
	}
	
	public static void dfs(int x, int y) {
		map[x][y] = 0;
		
		if( 0 <= x-1 && map[x-1][y] == 1 ) dfs(x-1,y); //up
		if( x+1 <M && map[x+1][y] == 1) dfs(x+1,y); //down
		if( 0 <= y-1 && map[x][y-1] == 1 ) dfs(x,y-1); //left
		if( y+1 < N && map[x][y+1] == 1 ) dfs(x,y+1); //right
	}

}
