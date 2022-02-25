import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ15683 {
	static int n;
	static int m;
	static int blindSpot;
	static int[] dr = new int[] {-1, 0, 1, 0}; // 북동남서
	static int[] dc = new int[] {0, 1, 0, -1};
	static int[][] map;
	static List<List<Integer>> cctvList;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		map = new int[n][m];

		cctvList = new ArrayList<>();
		List<Integer> cctv;
		for (int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j=0; j<m; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
				if ((map[i][j] > 0) && (map[i][j] < 6)) { // 1~5, cctv일 때
					cctv = new ArrayList<>(); // cctv 좌표 (i,j) 저장하고
					cctv.add(i);
					cctv.add(j);
					cctvList.add(cctv); // cctv 리스트에 넣기
				}
			}
		}
		blindSpot = n*m; // 전부 사각지대에서 시작
		dfs(0);
		System.out.println(blindSpot);
	}
	
	public static void dfs(int depth) {
		if (depth == cctvList.size()) { // 깊이가 cctv 개수랑 같아지면 한 가지 탐색 완료
			int num = 0;
			for (int i=0; i<n; i++) {
				for (int j=0; j<m; j++) {
					if (map[i][j] == 0) // 남은 사각지대 개수 세기
						num++;
				}
			}
			if (num < blindSpot) // 최댓값 저장
				blindSpot = num;
			return;
		}

		List<Integer> cctv = cctvList.get(depth); // 현재 cctv
		int r = cctv.get(0);
		int c = cctv.get(1);

		switch (map[r][c]) {
		case 1: // 한쪽 방향
			for (int i=0; i<4; i++) { // 4방향 어디로 돌릴지 고려
				observe(r, c, dr[i], dc[i]);
				dfs(depth+1);
				release(r, c, dr[i], dc[i]);
			}
			break;
		case 2: // 양방향(서로 반대로)
			for (int i=0; i<2; i++) { // 동서 또는 남북
				observe(r, c, dr[i], dc[i]);
				observe(r, c, dr[i+2], dc[i+2]);
				dfs(depth+1);
				release(r, c, dr[i], dc[i]);
				release(r, c, dr[i+2], dc[i+2]);
			}
			break;
		case 3: // 두 방향(직각)
			for (int i=0; i<4; i++) { // 직각이라 경우의 수 4개
				observe(r, c, dr[i], dc[i]);
				observe(r, c, dr[(i+1)%4], dc[(i+1)%4]);
				dfs(depth+1);
				release(r, c, dr[i], dc[i]);
				release(r, c, dr[(i+1)%4], dc[(i+1)%4]);
			}
			break;
		case 4: // 세 방향
			for (int i=0; i<4; i++) { // 경우의 수 4개
				observe(r, c, dr[i], dc[i]);
				observe(r, c, dr[(i+1)%4], dc[(i+1)%4]);
				observe(r, c, dr[(i+3)%4], dc[(i+3)%4]);
				dfs(depth+1);
				release(r, c, dr[i], dc[i]);
				release(r, c, dr[(i+1)%4], dc[(i+1)%4]);
				release(r, c, dr[(i+3)%4], dc[(i+3)%4]);
			}
			break;
		case 5: // 네 방향 전부
			for (int i=0; i<4; i++) { // 경우의 수는 하나임
				observe(r, c, dr[i], dc[i]);
			}
			dfs(depth+1);
			for (int i=0; i<4; i++) {
				release(r, c, dr[i], dc[i]);
			}
			break;
		}
	}
	
	public static void observe(int r, int c, int dRow, int dCol) { // 감시
		int row = r;
		int col = c;
		while (row>=0 && row<n && col>=0 && col<m && map[row][col] != 6) { // 범위 안에서 그 방향으로 계속
			if (map[row][col] <= 0) // 현재 사각지대(0)를 감시, 이미 감시중이라도 감시 처리
				map[row][col]--;
			row += dRow;
			col += dCol;
		}
	}
	
	public static void release(int r, int c, int dRow, int dCol) { // 감시 해제
		int row = r;
		int col = c;
		while (row>=0 && row<n && col>=0 && col<m && map[row][col] != 6) {
			if (map[row][col] < 0)
				map[row][col]++; // 다시 사각지대로 가는게 아니라 카메라 하나만 없애는거
			row += dRow;
			col += dCol;
		}
	}

}