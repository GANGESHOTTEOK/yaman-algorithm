#include <bits/stdc++.h>
using namespace std;
int N, M, a, b, c;
using tiii = tuple<int, int, int>;
set<tiii> edges;
vector<int> parent(1001);

int findParent(int node) {
    if(parent[node] == node) return node;
    return parent[node] = findParent(parent[node]);
}

void mergeSet(int a, int b) {
    int A = findParent(a), B = findParent(b);
    if(A != B) parent[B] = A;
}

int main() {
    cin >> N >> M;

    while(cin >> a >> b >> c) edges.emplace(c, a, b);
    for(int i=1;i<=N;i++) parent[i] = i;

    int cost, from, to, answer = 0;

    for(auto &edge : edges) {
        tie(cost, from, to) = edge;
        for(int i)
        if(findParent(from) == findParent(to)) continue;
        mergeSet(from, to);
        answer += cost;
    }
    cout << answer;
}