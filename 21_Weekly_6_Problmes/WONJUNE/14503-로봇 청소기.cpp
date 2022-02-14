#include <bits/stdc++.h>

using namespace std;

int N, M, r, c, d;
int room[51][51];
int dx[4] = {0,1,0,-1};
int dy[4] = {-1,0,1,0};

void init(){
    cin >> N >> M >> r >> c >> d;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
            cin >> room[i][j];
        }
    }
}

void solve(){
    int cnt = 0;
    int check = 0;
    while(1){
        if(room[r][c] != 2){
            check = 0;
            room[r][c] = 2;
            cnt++;
        }
        d -= 1;
        if(d < 0) d = 3;

        if(room[r+dy[d]][c+dx[d]] == 0){
            r += dy[d];
            c += dx[d];
            continue;
        }
        else{
            check++;
            if(check == 4){
                r = r + dy[(d+2)%4];
                c = c + dx[(d+2)%4];
                if(room[r][c] == 1){
                    cout << cnt;
                    return;
                }
                check = 0;
            }
        }
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

