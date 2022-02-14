#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, M, x, y, K, num;
    cin >> N >> M >> x >> y >> K;

    vector<vector<int>> board(N, vector<int>(M));  // 지도
    vector<int> cmd;                               // 명령
    int dice[7] = {0, 0, 0, 0, 0, 0, 0};           // 주사위

    pair<int, int> cmd_direction[5];  // 명령에 따른 움직이는 방향
    cmd_direction[1] = {0, +1};
    cmd_direction[2] = {0, -1};
    cmd_direction[3] = {-1, 0};
    cmd_direction[4] = {+1, 0};

    // 지도 입력 부분
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> num;
            board[i][j] = num;
        }
    }
    // 명령어 입력 부분
    for (int i = 0; i < K; i++) {
        cin >> num;
        cmd.push_back(num);
    }

    int d1 = dice[1];  // 주사위 위
    int d2 = dice[2];  // 주사위 앞
    int d3 = dice[3];  // 주사위 뒤
    int d4 = dice[4];  // 주사위 왼쪽
    int d5 = dice[5];  // 주사위 오른쪽
    int d6 = dice[6];  // 주사위 아래
    int nowx = x;
    int nowy = y;
    int nextx, nexty;

    for (int i = 0; i < cmd.size(); i++) {
        int direction = cmd[i];
        nextx = nowx + cmd_direction[direction].first;
        nexty = nowy + cmd_direction[direction].second;

        // 범위 안에 있으면 이동 및 출력, 범위를 벗어나면 무시
        if (0 <= nextx && nextx < N && 0 <= nexty && nexty < M) {
            // 이동
            nowx = nextx;
            nowy = nexty;

            // 주사위 굴리기
            switch (direction) {
                case 1:  // 동쪽 (오른쪽)
                    dice[1] = d4; dice[4] = d6; dice[6] = d5; dice[5] = d1; break;
                case 2:  // 서쪽 (왼쪽)
                    dice[1] = d5; dice[5] = d6; dice[6] = d4; dice[4] = d1; break;
                case 3:  // 북쪽 (위)
                    dice[1] = d3; dice[3] = d6; dice[6] = d2; dice[2] = d1; break;
                case 4:  // 남쪽 (아래)
                    dice[1] = d2; dice[2] = d6; dice[6] = d3; dice[3] = d1; break;
                default: break;
            }

            // 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사
            if (board[nowx][nowy] == 0)
                board[nowx][nowy] = dice[6];
            // 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.
            else {
                dice[6] = board[nowx][nowy];
                board[nowx][nowy] = 0;
            }
            d1 = dice[1], d2 = dice[2], d3 = dice[3], d4 = dice[4], d5 = dice[5], d6 = dice[6];

            // 주사위 위 숫자 출력
            cout << dice[1] << '\n';
        }
    }

    return 0;
}