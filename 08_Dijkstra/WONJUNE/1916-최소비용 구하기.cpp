#include <bits/stdc++.h>
#define INF 100'000'001

using namespace std;

int N, M;
int S, E;
int dist[1001]; 
bool visited[1001] = {0,};
vector<vector<pair<int,int>>> edge;

void init(){
    cin >> N >> M;
    for(int i = 1; i <= N; i++){
        dist[i] = INF;
    }
    edge.resize(N+1);

    int from,to,cost;
    for(int i = 0; i < M; i++){
        cin >> from >> to >> cost;
        edge[from].emplace_back(to, cost);
    }
    cin >> S >> E;
}

void solve(){
    priority_queue<pair<int,int>> q;
    dist[S] = 0;
    q.push({0,S});
    while(!q.empty()){
        auto p = q.top();
        q.pop();
        if(visited[p.second]) continue;
        for(auto t : edge[p.second]){
            if(dist[t.first] > -p.first + t.second){
                dist[t.first] = -p.first + t.second;
                q.push({-dist[t.first],t.first});
            }
        }
        visited[p.second] = true;
    }
    cout << dist[E];
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    init();
    solve();

    return 0;
}

