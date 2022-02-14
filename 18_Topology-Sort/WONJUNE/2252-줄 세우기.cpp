#include <bits/stdc++.h>

using namespace std;

int N, M;
vector<vector<int>> parent;
int num[32001] = {0,};

void init(){
    cin >> N >> M;
    parent.resize(N+1);
    int A,B;
    for(int i = 0; i < M; i++){
        cin >> A >> B;
        parent[A].emplace_back(B);
        num[B]++;
    }
}

void solve(){
    queue<int> q;

    for(int i = 1; i <= N; i++){
        if(!num[i]) q.push(i);
    }

    while(!q.empty()){
        auto p = q.front();
        q.pop();
        cout << p << " ";
        for(auto t : parent[p]){
            num[t]--;
            if(!num[t]) q.push(t);
        }
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    init();
    solve();

    return 0;
}

