#include <bits/stdc++.h>
#define INF 10'000'001

using namespace std;

int N,M;
int graph[101][101];

void init(){
    cin >> N >> M;

    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            graph[i][j] = INF;
        }
        graph[i][i] = 0;
    }

    int from, to, cost;
    for(int i = 0; i < M; i++){
        cin >> from >> to >> cost;
        graph[from-1][to-1] = min(graph[from-1][to-1], cost);
    }
}

void solve(){
    for(int k = 0; k < N; k++){
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                if(graph[i][k] == INF || graph[k][j] == INF) continue;
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j]);
            }
        }
    }

    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            if(graph[i][j] != INF){
                cout << graph[i][j] << " ";
            }
            else{
                cout << 0 << " ";
            }
        }
        cout << "\n";
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

