#include <bits/stdc++.h>

using namespace std;

int TC, N, M, W;
long long dist[501] = {0,};
vector<tuple<int, int, int>> edge;

void init(){
    cin >> N >> M >> W;
    memset(dist, 0, sizeof(dist));
    edge = vector<tuple<int,int,int>>();
}

void solve(){
    int S,E,T;
    for(int i = 0; i < M; i++){
        cin >> S >> E >> T;
        edge.emplace_back(S,E,T);
        edge.emplace_back(E,S,T);
    }
    
    for(int i = 0; i < W; i++){
        cin >> S >> E >> T;
        edge.emplace_back(S,E,-T);
    }

    int from, to, cost;
    for(int i = 0; i < N; i++){
        for(auto e : edge){
            tie(from, to, cost) = e;
            if(dist[from] + cost < dist[to]){
                dist[to] = dist[from] + cost;
            }
        }
    }
    
    for(auto e : edge){
        tie(from, to, cost) = e;
        if(dist[from] + cost < dist[to]){
            cout << "YES" << "\n";
            return;
        }
    }
    cout << "NO" << "\n";
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> TC;
    while(TC--){
        init();
        solve();
    }

    return 0;
}

