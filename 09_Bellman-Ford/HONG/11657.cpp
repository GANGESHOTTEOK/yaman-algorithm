#include <bits/stdc++.h>
using namespace std;

int N, M, A, B, C;
using tiii = tuple<int, int, int>; // from to cost
vector<tiii> edges;
vector<long> dist(501, LONG_MAX);

int main() {
    cin >> N >> M;
    while(cin >> A >> B >> C) 
        edges.emplace_back(A, B, C);

    dist[1] = 0;
    
    for(int i=1;i<N;i++) for(int j=0;j<M;j++) {
        int from = get<0>(edges[j]);
        int to   = get<1>(edges[j]);
        int cost = get<2>(edges[j]);

        if(dist[from] == LONG_MAX) continue;
        dist[to] = min(dist[to], dist[from] + cost);
    }

    for(int i=1;i<N;i++) for(int j=0;j<M;j++) {
        int from = get<0>(edges[j]);
        int to   = get<1>(edges[j]);
        int cost = get<2>(edges[j]);

        if(dist[from] != LONG_MAX && dist[to] > dist[from] + cost) {
            cout << "-1";
            exit(0);
        }            
    }

    for(int i=2;i<=N;i++) 
        if(dist[i]==LONG_MAX) cout << "-1\n";
        else cout << dist[i] << endl;
}