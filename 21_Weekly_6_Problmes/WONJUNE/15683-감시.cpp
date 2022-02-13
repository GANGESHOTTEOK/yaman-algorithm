#include <bits/stdc++.h>

using namespace std;

int N, M;
int room[8][9];
vector<pair<int,int>> cctv;
int rotation[6] = {0, 4, 2, 4, 4, 1};
bool dir[6][4] = {
    {false, false, false, false},
    {true, false, false, false},
    {true, false, true, false},
    {true, true, false, false},
    {true, true, false, true},
    {true, true, true, true},
};
int dx[4] = {0,1,0,-1};
int dy[4] = {1,0,-1,0};
int cnt = 0, ans = 70;

void backTracking(int idx){
    if(idx == cctv.size()){
        ans = min(cnt, ans);
        return;
    }

    int y,x;
    tie(y,x) = cctv[idx];
    int type = room[y][x];
    for(int i = 0; i < rotation[type]; i++){
        for(int j = 0; j < 4; j++){
            if(dir[type][(i+j)%4]){
                int sy = y, sx = x;
                sy += dy[j];
                sx += dx[j];
                while(0 <= sy && sy < N && 0 <= sx && sx < M){
                    if(room[sy][sx] < 0){
                        room[sy][sx] -= 1;
                    }
                    else if(room[sy][sx] == 0){
                        room[sy][sx] -= 1;
                        cnt--;
                    }
                    else if(room[sy][sx] == 6){
                        break;
                    }
                    sy += dy[j];
                    sx += dx[j];
                }
            }
        }
        backTracking(idx+1);
        for(int j = 0; j < 4; j++){
            if(dir[type][(i+j)%4]){
                int sy = y, sx = x;
                sy += dy[j];
                sx += dx[j];
                while(0 <= sy && sy < N && 0 <= sx && sx < M){
                    if(room[sy][sx] < 0){
                        room[sy][sx] += 1;
                        if(room[sy][sx] == 0){
                            cnt++;
                        }
                    }
                    else if(room[sy][sx] == 6){
                        break;
                    }
                    sy += dy[j];
                    sx += dx[j];
                }
            }
        }
    }
}

void init(){
    cin >> N >> M;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
            cin >> room[i][j];
            if(1 <= room[i][j] && room[i][j] <= 5){
                cctv.emplace_back(i,j);
            }
            else if(room[i][j] == 0){
                cnt++;
            }
        }
    }
}

void solve(){
    backTracking(0);
    cout << ans;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    init();
    solve();

    return 0;
}

