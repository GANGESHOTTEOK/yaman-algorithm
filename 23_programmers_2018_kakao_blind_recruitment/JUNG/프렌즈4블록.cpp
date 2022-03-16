#include <bits/stdc++.h>
#define MAX 30
using namespace std;

int M, N;
char board[MAX][MAX];  // 입력받은 보드
bool cnt[MAX][MAX];    // 숫자를 셌는지 확인하는 2차원 배열

void input_data(int m, int n, vector<string> input) {
    M = m;
    N = n;
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            board[i][j] = input[i][j];
        }
    }
}

bool check_if_twobytwo(int y, int x) {
    if (board[y][x] != 'Z' &&
        board[y][x] == board[y][x + 1] &&
        board[y][x] == board[y + 1][x] &&
        board[y][x] == board[y + 1][x + 1])
        return true;
    else
        return false;
}

int get_cnt(int y, int x) {
    int ret = 0;

    if (!cnt[y][x]) {
        cnt[y][x] = true;
        ret++;
    }
    if (!cnt[y][x + 1]) {
        cnt[y][x + 1] = true;
        ret++;
    }
    if (!cnt[y + 1][x]) {
        cnt[y + 1][x] = true;
        ret++;
    }
    if (!cnt[y + 1][x + 1]) {
        cnt[y + 1][x + 1] = true;
        ret++;
    }

    return ret;
}

void erase_character() {
    for (int y = 0; y < M; y++) {
        for (int x = 0; x < N; x++) {
            if (cnt[y][x]) board[y][x] = 'Z';
        }
    }
}

void drop_character() {
    // 한 열씩 순회
    for (int x = 0; x < N; x++) {
        // 밑에서부터 위로 한 칸씩
        for (int y = M - 1; y > 0; y--) {
            // 'Z'이면
            if (board[y][x] == 'Z') {
                // 'Z'의 바로 위 캐릭터와 자리를 바꿔준다.
                for (int i = y - 1; i >= 0; i--) {
                    if (board[i][x] != 'Z') {
                        char temp = board[y][x];
                        board[y][x] = board[i][x];
                        board[i][x] = temp;
                        break;
                    }
                }
            }
        }
    }
}

void reset_cnt() {
    for (int y = 0; y < M; y++) {
        for (int x = 0; x < N; x++) {
            cnt[y][x] = false;
        }
    }
}

int solution(int m, int n, vector<string> input) {
    int answer = 0;
    input_data(m, n, input);

    while (true) {
        bool end_flag = true;
        for (int y = 0; y < M - 1; y++) {
            for (int x = 0; x < N - 1; x++) {
                if (check_if_twobytwo(y, x)) {
                    answer += get_cnt(y, x);
                    end_flag = false;
                }
            }
        }

        if (end_flag) break;

        // 캐릭터 지우기
        erase_character();
        // 밑으로 떨어뜨리기
        drop_character();
        // cnt 초기화시키기
        reset_cnt();
    }

    return answer;
}