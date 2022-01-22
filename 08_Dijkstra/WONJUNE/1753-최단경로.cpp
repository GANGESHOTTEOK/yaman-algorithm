#include <bits/stdc++.h>
#define INF 200'001

using namespace std;

int V,E;
int K;
vector<map<int,int>> edge;
int dist[20001];
bool visited[20001] = {0,};

void init(){
    cin >> V >> E >> K;
    edge = vector<map<int,int>>(V+1);
    for(int i = 1; i <= V; i++){
        dist[i] = INF;
    }
    
    int from, to, cost;
    for(int i = 0; i < E; i++){
        cin >> from >> to >> cost;
        edge[from][to] = edge[from][to] ? min(edge[from][to], cost) : cost;
    }
}

void solve(){
    priority_queue<pair<int,int>> pq;
    dist[K] = 0;
    pq.push({0,K});
    while(!pq.empty()){
        auto p = pq.top();
        pq.pop();
        if(visited[p.second]) continue;
        for(auto e : edge[p.second]){
            if(dist[e.first] > -p.first + e.second){
                dist[e.first] = -p.first + e.second;
                pq.push({p.first - e.second, e.first});
            }
        }
        visited[p.second] = true;
    }
    for(int i = 1; i <= V; i++){
        if(dist[i] != INF){
            cout << dist[i] << "\n";
        }
        else{
            cout << "INF\n";
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

