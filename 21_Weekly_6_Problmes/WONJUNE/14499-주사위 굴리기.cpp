#include <bits/stdc++.h>

using namespace std;

int N,M,x,y,K;
int board[21][21];
int dice[6] = {0,};
int dx[4] = {1,-1,0,0};
int dy[4] = {0,0,-1,1};

void rolling(int& dir){
    int temp;
    switch(dir){
        case 1:
            temp = dice[0];
            dice[0] = dice[3];
            dice[3] = dice[5];
            dice[5] = dice[2];
            dice[2] = temp;
            break;
        case 2:
            temp = dice[0];
            dice[0] = dice[2];
            dice[2] = dice[5];
            dice[5] = dice[3];
            dice[3] = temp;
            break;
        case 3:
            temp = dice[0];
            dice[0] = dice[1];
            dice[1] = dice[5];
            dice[5] = dice[4];
            dice[4] = temp;
            break;
        case 4:
            temp = dice[0];
            dice[0] = dice[4];
            dice[4] = dice[5];
            dice[5] = dice[1];
            dice[1] = temp;
            break;
    }
}

void init(){
    cin >> N >> M >> y >> x >> K;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
            cin >> board[i][j];
        }
    }
}

void solve(){
    int dir;
    for(int i = 0; i < K; i++){
        cin >> dir;
        switch(dir){
            case 1:
                if(x == M-1) continue;
                break;
            case 2:
                if(x == 0) continue;
                break;
            case 3:
                if(y == 0) continue;
                break;
            case 4:
                if(y == N-1) continue;
                break;
        }
        rolling(dir);
        x += dx[dir-1];
        y += dy[dir-1];
        if(board[y][x] == 0){
            board[y][x] = dice[5];
        }
        else{
            dice[5] = board[y][x];
            board[y][x] = 0;
        }
        cout << dice[0] << "\n";
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    init();
    solve();

    return 0;
}

