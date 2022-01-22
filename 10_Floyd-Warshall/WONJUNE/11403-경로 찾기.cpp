#include <bits/stdc++.h>

using namespace std;

int N;
bool graph[101][101];

void init(){
    cin >> N;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            cin >> graph[i][j];
        }
    }
}

void solve(){
    for(int k = 0; k < N; k++){
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                if(graph[i][k] && graph[k][j]){
                    graph[i][j] = true;
                }
            }
        }
    }

    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j ++){
            cout << graph[i][j] << " ";
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

