#include <bits/stdc++.h>

using namespace std;

int N, M, D;
vector<pair<int,int>> enemy;
vector<pair<int,int>> archer;

void attack(vector<pair<int,int>> c){
    int turn = 0;

}

void backTracking(int idx){
    archer.emplace_back(N,idx);

    if(archer.size() == 3){
        attack(enemy);

        return;
    }

    for(int i = idx+1; i < M; i++){
        backTracking(i);
    }

}

void init(){
    cin >> N >> M >> D;
    for(int i = 0; i < N; i++){
        bool temp;
        for(int j = 0; j < M; j++){
            cin >> temp;
            if(temp) enemy.emplace_back(i,j);
        }
    }
    sort(enemy.begin(), enemy.end());
}

void solve(){
    for(int i = 0; i < M;i ++){
        backTracking(i);
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

