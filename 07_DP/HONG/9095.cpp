#include <bits/stdc++.h>
using namespace std;
int T, n, dp[12];

int solve(int n) {
    if(dp[n]) return dp[n];
    dp[n] = solve(n-1) + solve(n-2) + solve(n-3);
    return dp[n];
}

int main() {
    cin >> T;
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 4;
    while(T-- && cin >> n) cout << solve(n) << '\n';
}