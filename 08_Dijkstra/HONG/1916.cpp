#include <bits/stdc++.h>
using namespace std;
int N, M, from, to, cost;
vector<int> dp(1001, INT_MAX);
using pii = pair<int, int>; // first = cost, second = dest
vector<pii> adj[100001];
priority_queue<pii, vector<pii>, greater<pii>> pq;

int main() {
    cin >> N >> M;
    for(int i=0;i<M;i++) {
        cin >> from >> to >> cost;
        adj[from].emplace_back(to, cost);
    }
    cin >> from >> to;

    dp[0] = dp[from] = 0;
    pq.push({0, from});
    
    while(!pq.empty()) {
        int curr = pq.top().second;
        int curr_cost = pq.top().first;

        pq.pop();
        if(dp[curr] < curr_cost) continue;

        for(auto &edge : adj[curr]) {
            int next = edge.first;
            int next_cost = dp[curr] + edge.second;
            if(dp[next] <= next_cost) continue;
            dp[next] = next_cost;
            pq.push({next_cost, next});
        }
        
    }
    cout << dp[to];
}