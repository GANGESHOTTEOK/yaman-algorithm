#include <bits/stdc++.h>
using namespace std;
int n, m, a, b, c;
vector<vector<int>> dist(101, vector<int>(101, INT_MAX));

int main() {
    cin >> n >> m;
    for(int i=1;i<=m;i++) {
        cin >> a >> b >> c;
        dist[a][b] = min(dist[a][b], c);
    }

    for(int i=1;i<=n;i++) dist[i][i] = 0;

    for(int i=1;i<=n;i++) 
        for(int j=1;j<=n;j++) 
            for(int k=1;k<=n;k++) 
                if(dist[j][i]==INT_MAX || dist[i][k]==INT_MAX) continue;
                else dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k]);

    for(int i=1;i<=n;i++) {
        for(int j=1;j<=n;j++) 
            if(dist[i][j] == INT_MAX) cout << "0 ";
            else cout << dist[i][j] << ' ';
        cout << endl;
    }
}