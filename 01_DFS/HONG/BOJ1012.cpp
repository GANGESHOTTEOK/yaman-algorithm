#include <bits/stdc++.h>
using namespace std;
int T, M, N, K; string inp;

void input(vector<vector<bool> > &map) {
    int i, j, k = K;
    while(k--){
        cin >> i >> j;
        map[j][i] = true;
    }
}

int searchBaechu(vector<vector<bool> > &map, int i, int j) {
    int count = 1;
    map[i][j] = false;
    if(j!=M-1 && map[i][j+1]) count += searchBaechu(map, i, j+1);
    if(i!=N-1 && map[i+1][j]) count += searchBaechu(map, i+1, j);
    if(j!=0   && map[i][j-1]) count += searchBaechu(map, i, j-1);
    if(i!=0   && map[i-1][j]) count += searchBaechu(map, i-1, j);
    return count;
}

int main() {
    cin >> T;
    while(T--) {
        cin >> M >> N >> K;
        vector<vector<bool> > map(N, vector<bool>(M));
        input(map);
        int count = 0;
        for(int i=0;i<N;i++) for(int j=0;j<M;j++) 
            if(map[i][j]) {
                searchBaechu(map, i, j);
                count++;
            }
        cout << count << '\n'; 
    }
}