#include <bits/stdc++.h>
using namespace std;
using tiii = tuple<int, int, int>;
int TC, N, M, W, S, E, T;

bool bellman_ford(vector<tiii> edges) {
    vector<long> dist(N+1, 0);
    dist[1] = 0;
    int from, to, cost;

    for(int i=0;i<N-1;i++)
        for(auto &t : edges) {
            tie(from, to, cost) = t;
            dist[to] = min(dist[to], dist[from] + cost);
        }

    for(auto &t : edges) {
        tie(from, to, cost) = t;
        if(dist[to] > dist[from] + cost) return true;
    }
    return false;
}

int main() {
    cin >> TC;
    while(TC--) {
        cin >> N >> M >> W;
        vector<tiii> edges;
        for(int m=M; M-- && cin >> S >> E >> T;) {
            edges.emplace_back(S, E, T);
            edges.emplace_back(E, S, T);
        }
        for(int w=W; w-- && cin >> S >> E >> T;)
            edges.emplace_back(S, E, -T);

        if(bellman_ford(edges)) cout << "YES\n";
        else cout << "NO\n";
    }
}