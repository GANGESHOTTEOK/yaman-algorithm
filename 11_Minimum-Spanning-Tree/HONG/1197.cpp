#include <bits/stdc++.h>
using namespace std;
int V, E, A, B, C;
vector<int> parent(10001);
using tiii = tuple<int, int, int>;
set<tiii> edges;

int findParent(int a) {
    return parent[a] == a ? a : parent[a] = findParent(parent[a]);
}

void mergeSet(int a, int b) {
    int A = findParent(a);
    int B = findParent(b);
    if(A != B) parent[B] = A;
}

int main() {
    cin >> V >> E;

    while(cin >> A >> B >> C) edges.emplace(C, A, B);
    for(int i=1;i<=V;i++) parent[i] = i;

    int cost, from, to, answer = 0;
    for(auto &edge : edges) {
        tie(cost, from, to) = edge;
        if(findParent(from) == findParent(to)) continue;
        mergeSet(from, to);
        answer += cost;
    }
    cout << answer;
}