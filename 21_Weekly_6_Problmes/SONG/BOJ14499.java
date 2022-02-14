import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ14499 {
    static int N, M, K;
    static int x,y;
    static int[][] map;
    static int[] dice = new int[6];
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        x = Integer.parseInt(st.nextToken());
        y = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        map = new int[N][M];
        for(int i=0; i<N; i++) {
                st = new StringTokenizer(br.readLine());
            for(int j=0; j<M; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<K; i++) {
            int roll = Integer.parseInt(st.nextToken());
            if(roll == 1) {
                if(check(0, 1)) {
                    dice1();
                    map();
                }
            } else if(roll == 2) {
                if(check(0, -1)) {
                    dice2();
                    map();
                }
            } else if(roll == 3) {
                if(check(-1, 0)) {
                    dice3();
                    map();
                }
            } else { // roll == 4
                if(check(1, 0)) {
                    dice4();
                    map();
                }
            }
        }
        System.out.println(sb.toString());
    }

    static boolean check(int _x, int _y) { // 가능한 명령인지 체크하고 가능하면 위치 이동
        if( x+_x >= N || x+_x <0 || y+_y >= M || y+_y < 0) return false;
        x = x+_x;
        y = y+_y;
        return true;
    }

    static void map() {
        if(map[x][y] == 0) { // 이동한 칸의 수가 0이면
            map[x][y] = dice[3]; // 주사위 바닥에 있는 수가 그 칸에 복사 됨
        }
        else { // 아니면 칸에 쓰인 수가 주사위 바닥으로
            dice[3] = map[x][y];
            map[x][y] = 0;
        }
        sb.append(dice[0] + "\n");
    }

    static void dice1() { // 동쪽
        int temp = dice[5];
        dice[5] = dice[3];
        dice[3] = dice[2];
        dice[2] = dice[0];
        dice[0] = temp;
    }

    static void dice2() { // 서쪽
        int temp = dice[0];
        dice[0] = dice[2];
        dice[2] = dice[3];
        dice[3] = dice[5];
        dice[5] = temp;
    }

    static void dice3() { // 북쪽
        int temp = dice[0];
        dice[0] = dice[1];
        dice[1] = dice[3];
        dice[3] = dice[4];
        dice[4] = temp;
    }

    static void dice4() { // 남쪽
        int temp = dice[4];
        dice[4] = dice[3];
        dice[3] = dice[1];
        dice[1] = dice[0];
        dice[0] = temp;
    }
}
