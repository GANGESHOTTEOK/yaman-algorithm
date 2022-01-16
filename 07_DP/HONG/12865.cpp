#include <bits/stdc++.h>
using namespace std;

int N, W, V, K;
int dp[101][100001];
vector<pair<int, int>> items(1, {0, 0});

int main() {
    cin >> N >> K;
    while(cin >> W >> V) items.emplace_back(W, V);

    for(int i=1;i<=N;i++) for(int j=1;j<=K;j++) {
        if(j < items[i].first) dp[i][j] = dp[i-1][j];
        else dp[i][j] = max(dp[i-1][j], dp[i-1][j - items[i].first] + items[i].second);
    }
    cout << dp[N][K];
}