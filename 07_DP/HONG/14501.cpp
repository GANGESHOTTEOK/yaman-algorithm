#include <bits/stdc++.h>
using namespace std;
int N, T[16], P[16], dp[16];

int main() {
    cin >> N;
    for(int i=1;i<=N;i++) cin >> T[i] >> P[i];

    for(int i=1;i<=N;i++)
        for(int j=0;j<i;j++)
            if(j + T[j] <= i && T[i] + i <= N+1)
                dp[i] = max(dp[i], dp[j] + P[i]);

    cout << *max_element(dp, dp+N+1);
}