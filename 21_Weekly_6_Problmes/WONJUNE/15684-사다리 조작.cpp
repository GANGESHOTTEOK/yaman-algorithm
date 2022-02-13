#include <bits/stdc++.h>

using namespace std;

int N, M, H;
bool ladder[31][11];
int cnt = 0, ans = 4;
pair<int,int> lastLadder = {1,1};

bool check(){
    for(int i = 1; i <= N; i++){
        int goal = i;
        for(int j = 1; j <= H; j++){
            if(ladder[j][goal]){
                goal++;
            }
            else if(ladder[j][goal-1]){
                goal--;
            }
        }
        if(goal != i) return false;
    }
    return true;
}

pair<int,int> findLadder(){
    int y,x;
    tie(y,x) = lastLadder;
    while(y <= H){
        if(!ladder[y][x] && !ladder[y][x-1] && !ladder[y][x+1]){
            return lastLadder = {y,x};
        }
        else{
            if(++x == N){
                x = 1;
                y++;
            }
        }
    }
    return lastLadder = {0,0};
}

void backTracking(int cnt){
    if(check()) ans = min(ans, cnt);
    if(cnt == 3) return;

    auto newLadder = findLadder();
    while(newLadder.first && newLadder.second){
        ladder[newLadder.first][newLadder.second] = true;
        backTracking(cnt+1);
        ladder[newLadder.first][newLadder.second] = false;
        lastLadder = {newLadder.first, newLadder.second+1};
        if(lastLadder.second == N){
            lastLadder.second = 1;
            lastLadder.first++;
        }
        newLadder = findLadder();
    }
}

void init(){
    cin >> N >> M >> H;
    for(int i = 0; i <= H; i++){
        for(int j = 0; j <= N+1; j++){
            ladder[i][j] = false;
        }
    }
    int y,x;
    for(int i = 0; i < M; i++){
        cin >> y >> x;
        ladder[y][x] = true;
    }
}

void solve(){
    backTracking(0);
    if(ans == 4){
        cout << -1;
    }
    else{
        cout << ans;
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

