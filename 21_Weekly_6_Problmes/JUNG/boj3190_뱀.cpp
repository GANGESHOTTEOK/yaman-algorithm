#include <bits/stdc++.h>
using namespace std;

int N;     // ���� ũ��
int K;     // ����� ����
int a, b;  // ����� ��ġ
int L;     // ���� ���� ��ȯ Ƚ��

// ���� ��ȯ ����
int X;   // ��
char C;  // ȸ�� ����

// ���� �� ������ �ٲٴ� �Լ�
void rotate(int& x, int& y, char& now_dir, char rotate) {
    // ���� ȸ��
    if (rotate == 'L') {
        switch (now_dir) {
            case 'u': now_dir = 'l'; break;
            case 'd': now_dir = 'r'; break;
            case 'l': now_dir = 'd'; break;
            case 'r': now_dir = 'u'; break;
            default : break;
        }
    }
    // ������ ȸ��
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

// ���� �� ĭ �����̴� �Լ�
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
    vector<vector<int>> board(N, vector<int>(N, 0));  // 0: �ƹ��͵� ����, 1: ���, 2: ����
    deque<pair<int, int>> snake;                      // ��

    cin >> K;
    for (int i = 0; i < K; i++) {
        cin >> a >> b;
        board[a - 1][b - 1] = 1;  // ���
    }

    cin >> L;
    deque<pair<int, char>> direction;
    for (int i = 0; i < L; i++) {
        cin >> X >> C;
        direction.push_back({X, C});
    }

    int time = 1;        // �ð�
    int x = 0, y = 0;    // ���� ��ġ
    char now_dir = 'r';  // ���� ���� u: �� d: �Ʒ� l: ���� r: ������

    while (true) {
        // �ϴ� ���� �ø���
        board[x][y] = 2;
        snake.push_front({x, y});

        // �밡�� ����ֱ�
        just_move(x, y, now_dir);

        // ������ �ٲ� ���� �Ǹ� ������ �ٲٱ�
        if (direction[0].first == time) {  // X�ʰ� ������
            if (direction[0].second == 'L') {
                // ���� ȸ��
                rotate(x, y, now_dir, 'L');
            } else {
                // ������ ȸ��
                rotate(x, y, now_dir, 'R');
            }
            direction.pop_front();
        }

        // ���̳� ���� �浹�ϴ��� Ȯ���ϱ� -> ���� �浹�Ѵٸ� break
        if (x <= -1 || x >= N || y <= -1 || y >= N) {
            break;
        }
        if (board[x][y] == 2) {
            break;
        }

        // ����� �ִ��� Ȯ���ϱ�
        if (board[x][y] == 0) {
            // ����� �����Ƿ� ������ �ڸ���
            auto tail = snake.back();
            board[tail.first][tail.second] = 0;
            snake.pop_back();
        }

        time++;
    }

    cout << time;
    return 0;
}