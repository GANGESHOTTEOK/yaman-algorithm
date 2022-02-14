#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, M, x, y, K, num;
    cin >> N >> M >> x >> y >> K;

    vector<vector<int>> board(N, vector<int>(M));  // ����
    vector<int> cmd;                               // ���
    int dice[7] = {0, 0, 0, 0, 0, 0, 0};           // �ֻ���

    pair<int, int> cmd_direction[5];  // ��ɿ� ���� �����̴� ����
    cmd_direction[1] = {0, +1};
    cmd_direction[2] = {0, -1};
    cmd_direction[3] = {-1, 0};
    cmd_direction[4] = {+1, 0};

    // ���� �Է� �κ�
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> num;
            board[i][j] = num;
        }
    }
    // ��ɾ� �Է� �κ�
    for (int i = 0; i < K; i++) {
        cin >> num;
        cmd.push_back(num);
    }

    int d1 = dice[1];  // �ֻ��� ��
    int d2 = dice[2];  // �ֻ��� ��
    int d3 = dice[3];  // �ֻ��� ��
    int d4 = dice[4];  // �ֻ��� ����
    int d5 = dice[5];  // �ֻ��� ������
    int d6 = dice[6];  // �ֻ��� �Ʒ�
    int nowx = x;
    int nowy = y;
    int nextx, nexty;

    for (int i = 0; i < cmd.size(); i++) {
        int direction = cmd[i];
        nextx = nowx + cmd_direction[direction].first;
        nexty = nowy + cmd_direction[direction].second;

        // ���� �ȿ� ������ �̵� �� ���, ������ ����� ����
        if (0 <= nextx && nextx < N && 0 <= nexty && nexty < M) {
            // �̵�
            nowx = nextx;
            nowy = nexty;

            // �ֻ��� ������
            switch (direction) {
                case 1:  // ���� (������)
                    dice[1] = d4; dice[4] = d6; dice[6] = d5; dice[5] = d1; break;
                case 2:  // ���� (����)
                    dice[1] = d5; dice[5] = d6; dice[6] = d4; dice[4] = d1; break;
                case 3:  // ���� (��)
                    dice[1] = d3; dice[3] = d6; dice[6] = d2; dice[2] = d1; break;
                case 4:  // ���� (�Ʒ�)
                    dice[1] = d2; dice[2] = d6; dice[6] = d3; dice[3] = d1; break;
                default: break;
            }

            // �̵��� ĭ�� ���� �ִ� ���� 0�̸�, �ֻ����� �ٴڸ鿡 ���� �ִ� ���� ĭ�� ����
            if (board[nowx][nowy] == 0)
                board[nowx][nowy] = dice[6];
            // 0�� �ƴ� ��쿡�� ĭ�� ���� �ִ� ���� �ֻ����� �ٴڸ����� ����Ǹ�, ĭ�� ���� �ִ� ���� 0�� �ȴ�.
            else {
                dice[6] = board[nowx][nowy];
                board[nowx][nowy] = 0;
            }
            d1 = dice[1], d2 = dice[2], d3 = dice[3], d4 = dice[4], d5 = dice[5], d6 = dice[6];

            // �ֻ��� �� ���� ���
            cout << dice[1] << '\n';
        }
    }

    return 0;
}