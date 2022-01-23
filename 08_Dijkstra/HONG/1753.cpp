#include <bits/stdc++.h>
using namespace std;
int V, E, start, u, v, w;
vector<int> dp(20001, INT_MAX);
using pii = pair<int, int>;
vector<pii> adj[300001];
priority_queue<pii, vector<pii>, greater<pii>> pq;

int main() {
    cin >> V >> E >> start;
    for(int i=0; i<E && cin >> u >> v >> w; i++)
        adj[u].emplace_back(w, v); // cost, dest
    
    dp[start] = 0;
    pq.push({0, start}); // cost, vertex

    while(!pq.empty()) {
        int curr = pq.top().second;
        int curr_dist = pq.top().first;
        pq.pop();
        if(dp[curr] < curr_dist) continue;

        for(auto &edge : adj[curr]) {
            int next = edge.second;
            int next_dist = edge.first + dp[curr];
            if(next_dist >= dp[next]) continue;
            dp[next] = next_dist;
            pq.push({next_dist, next});
        }
    }

    for(int i=1;i<=V;i++) 
        if(dp[i]==INT_MAX) cout << "INF\n";
        else cout << dp[i] << '\n';
}