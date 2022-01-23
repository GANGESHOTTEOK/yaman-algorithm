#include <bits/stdc++.h>
using namespace std;
int N, M, T;

int comb[30][30];

int combination(int n, int r) {
    if(comb[n][r]) return comb[n][r];

    if(n==r | r==0) {
        comb[n][r] = 1;
        return 1;
    }
    comb[n][r] = combination(n-1, r) + combination(n-1, r-1);
    return comb[n][r];
}

int main() {
    cin >> T;
    comb[0][0] = comb[1][0] = comb[0][1] = 1;
    while(T-- && cin >> N >> M) cout << combination(M, N) << '\n';
}