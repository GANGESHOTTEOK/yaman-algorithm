#include <bits/stdc++.h>
using namespace std;

int main() {
    int V, E, u, v;
    cin >> V >> E;
    vector<list<int>> network(V+1, list<int>());
    while(E-- && cin >> u >> v) {
        network[u].push_back(v);
        network[v].push_back(u);
    }

    int count = 0;
    queue<int> q;
    vector<bool> visited(V+1);
    visited[1] = true;
    q.push(1);

    while(!q.empty()) {
        int curr = q.front();
        q.pop();

        for(auto &node : network[curr]) {
            if(visited[node]) continue;
            count++;
            visited[node] = true;
            q.push(node);
        }
    }
    cout << count;
}