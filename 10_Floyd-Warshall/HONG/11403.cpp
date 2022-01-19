#include<bits/stdc++.h>
using namespace std;
int N, a, b;

int main() {
    cin >> N;
    vector<vector<int>> matrix(N, vector<int>(N, INT_MAX));

    for(int i=0;i<N;i++)
        for(int j=0;j<N;j++)
            cin >> matrix[i][j];

    for(int i=0;i<N;i++)
        for(int j=0;j<N;j++)
            for(int k=0;k<N;k++) {
                if(matrix[j][i] && matrix[i][k]) matrix[j][k] = 1;
            }

    for(int i=0;i<N;i++) {
        for(int j=0;j<N;j++) cout << matrix[i][j] << ' ';
        cout << '\n';
    }
}