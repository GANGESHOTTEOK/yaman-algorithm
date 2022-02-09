import java.io.*;
import java.util.StringTokenizer;
/**
 * BOJ14503 - 로봇청소기
 */
public class BOJ14503 {
    public static int N, M;
    public static int[][] map;
    public static int cnt = 0;
    public static int[] dr = {-1, 0, 1, 0}; // 북,동,남,서
    public static int[] dc = {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new int[N][M];

        st = new StringTokenizer(br.readLine());
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        clean(r, c, d);

        System.out.println(cnt);
    }

    public static void clean(int row, int col, int direction) {
        // 1. 현재 위치를 청소한다.
        if (map[row][col] == 0) {
            map[row][col] = 2;
            cnt++;
        }

        // 2. 왼쪽방향부터
        boolean flag = false;
        int origin = direction;
        for (int i = 0; i < 4; i++) {
            int next_d = (direction + 3) % 4;
            int next_r = row + dr[next_d];
            int next_c = col + dc[next_d];

            if (next_r > 0 && next_c > 0 && next_r < N && next_c < M) {
                if (map[next_r][next_c] == 0) {   // case A
                    clean(next_r, next_c, next_d);
                    flag = true;
                    break;
                }
            }
            // case B
            direction = (direction + 3) % 4; // 왼쪽으로 회전
        }

        if (!flag) {
            int next_d = (origin + 2) % 4; // 후진
            int next_br = row + dr[next_d];
            int next_bc = col + dc[next_d];

            if (next_br > 0 && next_bc > 0 && next_br < N && next_bc < M) { // case C
                if (map[next_br][next_bc] != 1) {
                    clean(next_br, next_bc, origin); // 후진한 지점에서 다시 탐색 시작
                }
            }
        }
        // 종료되면 case D
    }
}