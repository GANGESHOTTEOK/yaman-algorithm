#include <bits/stdc++.h>

using namespace std;

int N, M, ans = 0;
int parent[1001];
priority_queue<tuple<int,int,int>> pq;

int findParent(int x){
    if(x == parent[x]) return x;
    else return findParent(parent[x]);
}

bool sameParent(int x, int y){
    x = findParent(x);
    y = findParent(y);
    if(x == y) return true;
    else return false;
}

void init(){
    cin >> N >> M;
    for(int i = 1; i < N; i++)
        parent[i] = i;

    int from, to, cost;
    for(int i = 0; i < M; i++){
        cin >> from >> to >> cost;
        pq.push({-cost, from, to});
    }
}

void solve(){
    int from, to, cost;
    while(!pq.empty()){
        tie(cost, from, to) = pq.top();
        pq.pop();
        if(!sameParent(from, to)){
            ans += -cost;
            parent[findParent(from)] = to;
        }
    }
    cout << ans;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    init();
    solve();
    
    return 0;
}

