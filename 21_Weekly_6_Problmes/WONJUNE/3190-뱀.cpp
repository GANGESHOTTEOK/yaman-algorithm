#include <bits/stdc++.h>

using namespace std;

int N, K, L;

pair<int,int> board[102][102];
vector<pair<int,char>> turn;

void init(){
    cin >> N >> K;
    for(int i = 0; i < N+2; i++){
        board[0][i] = {3,0};
        board[N+1][i] = {3,0};
    }
    for(int i = 1; i < N+1; i++){
        board[i][0] = {3,0};
        for(int j = 1; j < N+1; j++){
            board[i][j] = {0,0};
        }
        board[i][N+1] = {3,0};
    }
    int c, r;
    for(int i = 0; i < K; i++){
        cin >> c >> r;
        board[c][r] = {1,0};
    }
    cin >> L;
    int X;
    char C;
    for(int i = 0; i < L; i++){
        cin >> X >> C;
        turn.emplace_back(X,C);
    }
    turn.emplace_back(100001,'L');
}

void solve(){
    pair<int,int> head = {1,1},tail = {1,1};
    int dx[4] = {1,0,-1,0};
    int dy[4] = {0,1,0,-1};
    int dir = 0; //right, down, left, up
    int t = 0;
    int turnIdx = 0;

    board[head.first][head.second] = {2,dir};

    while(t <= 10000){
        t++;
        head.first += dy[dir];
        head.second += dx[dir];

        if(t == turn[turnIdx].first){
            if(turn[turnIdx].second == 'L'){
                dir--;
                if(dir < 0) dir = 3;
            }
            else{
                dir++;
                if(dir > 3) dir = 0;
            }
            turnIdx++;
        }

        switch(board[head.first][head.second].first){
            case 1:
                board[head.first][head.second] = {2,dir};
                break;
            case 2:
            case 3:
                cout << t;
                return;
            default:
                board[head.first][head.second] = {2,dir};
                int tailDir = board[tail.first][tail.second].second;
                board[tail.first][tail.second].first = 0;
                tail.first += dy[tailDir];
                tail.second += dx[tailDir];
        }
    }
    cout << t;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    init();
    solve();

    return 0;
}

