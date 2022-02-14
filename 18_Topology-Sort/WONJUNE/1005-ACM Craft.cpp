#include <bits/stdc++.h>

using namespace std;

int N, K, W;
int cost[1001] = {0,};
vector<vector<int>> pre;
int parent[1001] = {0,};

void init(){
    pre = vector<vector<int>>();
    cin >> N >> K;
    pre.resize(N+1);
    for(int i = 1; i <= N; i++){
        cin >> cost[i];
        parent[i] = 0;
    }
    
    int X, Y;
    for(int i = 0; i < K; i++){
        cin >> X >> Y;
        pre[X].emplace_back(Y);
        parent[Y]++;
    }
    cin >> W;
}

void solve(){
    priority_queue<pair<int,int>> pq;
    for(int i = 1; i <= N; i++){
        if(parent[i] == 0){
            pq.push({-cost[i],i});
        }
    }

    while(!pq.empty()){
        auto p = pq.top();
        pq.pop();
        if(p.second == W){
            cout << -p.first << "\n";
            return;
        }

        for(auto pr: pre[p.second]){
            parent[pr]--;
            if(parent[pr] == 0){
                pq.push({p.first - cost[pr], pr});
            }
        }
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    int T;
    cin >> T;
    while(T--){
        init();
        solve();
    }

    return 0;
}

