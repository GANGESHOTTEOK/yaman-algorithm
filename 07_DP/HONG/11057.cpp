#include <bits/stdc++.h>
using namespace std;
int N, comb[1010][1001];

int getComb(int n, int r) {
    if(comb[n][r]) return comb[n][r];
    if(r == 0 || r == n) return 1;

    comb[n][r] = (getComb(n-1, r) + getComb(n-1, r-1)) % 10007;
    return comb[n][r];
}

int main() {
    cin >> N;
    cout << getComb(9 + N, N);
}