#include <bits/stdc++.h>
using namespace std;

int N;     // 보드 크기
int K;     // 사과의 개수
int a, b;  // 사과의 위치
int L;     // 뱀의 방향 변환 횟수

// 방향 변환 정보
int X;   // 초
char C;  // 회전 방향

// 뱀의 몸 방향을 바꾸는 함수
void rotate(int& x, int& y, char& now_dir, char rotate) {
    // 왼쪽 회전
    if (rotate == 'L') {
        switch (now_dir) {
            case 'u': now_dir = 'l'; break;
            case 'd': now_dir = 'r'; break;
            case 'l': now_dir = 'd'; break;
            case 'r': now_dir = 'u'; break;
            default : break;
        }
    }
    // 오른쪽 회전
    else {
        switch (now_dir) {
            case 'u': now_dir = 'r'; break;
            case 'd': now_dir = 'l'; break;
            case 'l': now_dir = 'u'; break;
            case 'r': now_dir = 'd'; break;
            default :break;
        }
    }
}

// 뱀을 한 칸 움직이는 함수
void just_move(int& x, int& y, char& now_dir) {
    switch (now_dir) {
        case 'u': x--; break;
        case 'd': x++; break;
        case 'l': y--; break;
        case 'r': y++; break;
        default :break;
    }
}

int main(void) {
    cin >> N;
    vector<vector<int>> board(N, vector<int>(N, 0));  // 0: 아무것도 없음, 1: 사과, 2: 몸통
    deque<pair<int, int>> snake;                      // 뱀

    cin >> K;
    for (int i = 0; i < K; i++) {
        cin >> a >> b;
        board[a - 1][b - 1] = 1;  // 사과
    }

    cin >> L;
    deque<pair<int, char>> direction;
    for (int i = 0; i < L; i++) {
        cin >> X >> C;
        direction.push_back({X, C});
    }

    int time = 1;        // 시간
    int x = 0, y = 0;    // 현재 위치
    char now_dir = 'r';  // 현재 방향 u: 위 d: 아래 l: 왼쪽 r: 오른쪽

    while (true) {
        // 일단 꼬리 늘리기
        board[x][y] = 2;
        snake.push_front({x, y});

        // 대가리 집어넣기
        just_move(x, y, now_dir);

        // 방향을 바꿀 때가 되면 방향을 바꾸기
        if (direction[0].first == time) {  // X초가 끝나면
            if (direction[0].second == 'L') {
                // 왼쪽 회전
                rotate(x, y, now_dir, 'L');
            } else {
                // 오른쪽 회전
                rotate(x, y, now_dir, 'R');
            }
            direction.pop_front();
        }

        // 벽이나 몸에 충돌하는지 확인하기 -> 만약 충돌한다면 break
        if (x <= -1 || x >= N || y <= -1 || y >= N) {
            break;
        }
        if (board[x][y] == 2) {
            break;
        }

        // 사과가 있는지 확인하기
        if (board[x][y] == 0) {
            // 사과가 없으므로 꼬리를 자르기
            auto tail = snake.back();
            board[tail.first][tail.second] = 0;
            snake.pop_back();
        }

        time++;
    }

    cout << time;
    return 0;
}