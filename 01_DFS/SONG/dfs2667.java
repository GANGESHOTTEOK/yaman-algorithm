package algorithmStudy;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class dfs2667 {
	static int n;
	static int[][] map;
	static ArrayList<Integer> area;
	static int count = 0;
	static int house = 0;
	
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		n = input.nextInt();
		map = new int[n][n];
		area = new ArrayList<Integer>();
		
		/* input */
		for(int i=0; i<n; i++) {
			String str = input.next();
			for(int j=0; j<n; j++) {
				map[i][j] = str.charAt(j)-'0';
			}
		}
		
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				if(map[i][j] == 1) {
					house = 0;
					dfs(i,j);
					area.add(house);
				}
			}
		}
				
		Collections.sort(area);
		
		/* output */
		System.out.println(area.size());
		for(int i=0; i<area.size(); i++) {
			System.out.println(area.get(i));
		}
	}

	
	public static void dfs(int x, int y) {
		house++;
		map[x][y] = 0;
		
		if( 0 <= x-1 && map[x-1][y] == 1 ) dfs(x-1,y); //up
		if( x+1 <n && map[x+1][y] == 1) dfs(x+1,y); //down
		if( 0 <= y-1 && map[x][y-1] == 1 ) dfs(x,y-1); //left
		if( y+1 < n && map[x][y+1] == 1 ) dfs(x,y+1); //right
	}
}
