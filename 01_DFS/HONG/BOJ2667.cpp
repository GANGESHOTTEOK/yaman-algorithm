#include <bits/stdc++.h>
using namespace std;
int N; string inp;

void input(vector<vector<bool>> &map, int N) {
    
    for(int i=0;i<N;i++){
        cin >> inp;
        for(int j=0;j<N;j++)
            if(inp[j]=='1') map[i][j] = true;
    }
}

int countHouses(vector<vector<bool>> &map, int i, int j) {
    int count = 1;
    map[i][j] = false;
    if(j!=N-1 && map[i][j+1]) count += countHouses(map, i, j+1);
    if(i!=N-1 && map[i+1][j]) count += countHouses(map, i+1, j);
    if(j!=0   && map[i][j-1]) count += countHouses(map, i, j-1);
    if(i!=0   && map[i-1][j]) count += countHouses(map, i-1, j);
    return count;
}

int main() {
    cin >> N;
    vector<vector<bool> > map(N, vector<bool>(N));
    multiset<int> complex;

    input(map, N);

    for(int i=0;i<N;i++) for(int j=0;j<N;j++) 
        if(map[i][j]) complex.insert(countHouses(map, i, j));

    cout << complex.size() << '\n';
    for(auto &w : complex) cout << w << '\n';
}