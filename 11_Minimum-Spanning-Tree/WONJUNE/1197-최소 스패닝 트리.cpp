#include <bits/stdc++.h>

using namespace std;

int V,E;
int parent[10001];
long long weight = 0;
priority_queue<tuple<int,int,int>> pq;

int findParent(int x){
    if(x == parent[x]) return x;
    else return parent[x] = findParent(parent[x]);
}

bool sameParent(int x, int y){
    x = findParent(x);
    y = findParent(y);
    if(x == y) return true;
    else return false;
}

void init(){
    cin >> V >> E;
    for(int i = 1; i <= V; i++)
        parent[i] = i;
    
    int from, to, cost;
    for(int i = 0; i < E; i++){
        cin >> from >> to >> cost;
        pq.push({-cost, from, to});
    }
}

void solve(){
    while(!pq.empty()){
        int from, to, cost;
        tie(cost, from, to) = pq.top();
        pq.pop();

        if(!sameParent(from, to)){
            weight += -cost;
            parent[findParent(from)] = to;
        }
    }
    cout << weight;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    init();
    solve();

    return 0;
}

