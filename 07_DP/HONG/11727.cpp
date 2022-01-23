#include <bits/stdc++.h>
using namespace std;
long long n, dp[1001];

int solve(int n) {
    if(dp[n]) return dp[n];
    dp[n] = (solve(n-1) + 2*solve(n-2)) % 10007;
    return dp[n];
}

int main() {
    cin >> n;
    dp[1] = 1;
    dp[2] = 3;
    cout << solve(n);
}