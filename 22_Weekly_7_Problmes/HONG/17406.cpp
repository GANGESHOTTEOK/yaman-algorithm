#include <bits/stdc++.h>
using namespace std;
int N, M, K, r, c, s, result = INT_MAX;

void rotate(vector<vector<int>> &A, int r, int c, int s) {
    int x = r-s, y = c-s, temp = A[x][y];
    for(int i=r-s+1;i<=r+s;i++) A[x++][y] = A[i][y];
    for(int i=c-s+1;i<=c+s;i++) A[x][y++] = A[x][i];
    for(int i=r+s-1;i>=r-s;i--) A[x--][y] = A[i][y];
    for(int i=c+s-1;i>=c-s;i--) A[x][y--] = A[x][i];
    A[x][y+1] = temp;
}

int getValue(vector<vector<int>> &A) {
    priority_queue<int> sums;
    for(int i=1;i<=N;i++) {
        int sum=0;
        for(int j=1;j<=M;j++) sum+=A[i][j];
        sums.push(-sum);
    }
    return -sums.top();
}

int main() {
    cin >> N >> M >> K;
    vector<tuple<int, int, int>> query;
    vector<vector<int>> A(N+1, vector<int>(M+1));
    for(int i=1;i<=N;i++) for(int j=1;j<=M;j++) cin >> A[i][j];
    while(K-- && cin >> r >> c >> s) query.emplace_back(r, c, s);
    sort(query.begin(), query.end());

    do {
        vector<vector<int>> B(A);
        for(auto &q : query) {
            tie(r, c, s) = q;
            for(int i=1;i<=s;i++) rotate(B, r, c, i);
        }
        result = min(result, getValue(B));
    } while(next_permutation(query.begin(), query.end()));

    cout << result;
}