#include <bits/stdc++.h>
#include <memory.h>
#define INF 900'000'000LL

using namespace std;

int N, M;

vector<tuple<int,int,int>> graph;
long long dist[501];

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> N >> M;
    for(int i = 1; i < N+1; i++){
        dist[i] = INF;
    }

    int A,B,C;
    for(int i = 0; i < M; i++){
        cin >> A >> B >> C;
        graph.emplace_back(A,B,C);
    }

    dist[1] = 0;
    for(int i = 1; i <= N-1; i++){
        for(int v = 0; v < M; v++){
            int from, to, cost;
            tie(from, to, cost) = graph[v];
            if(dist[from] != INF && dist[from] + cost < dist[to]){
                dist[to] = dist[from] + cost;
            }
        }
    }

    for(int v = 0; v < M; v++){
        int from, to, cost;
        tie(from, to, cost) = graph[v];
        if(dist[from] != INF && dist[from] + cost < dist[to]){
            cout << -1 << "\n";
            return 0;
        }
    }

    for(int i = 2; i < N+1; i++){
        if(dist[i] == INF) cout << -1 << "\n";
        else cout << dist[i] << "\n";
    }

    return 0;
}

