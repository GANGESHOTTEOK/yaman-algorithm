#include <bits/stdc++.h>

using namespace std;

int dp[2][3] = {0,};
int N;

void init(){
    cin >> N;
    int a,b,c;
    cin >> dp[0][0] >> dp[0][1] >> dp[0][2];
    for(int i = 0; i < 3; i++){
        dp[1][i] = dp[0][i];
    }
}

void solve(){
    int a,b,c;
    int temp[3];
    for(int i = 1; i < N; i++){
        cin >> a >> b >> c;
        temp[0] = a + min(dp[0][0], dp[0][1]);
        temp[1] = b + min({dp[0][0], dp[0][1], dp[0][2]});
        temp[2] = c + min(dp[0][1], dp[0][2]);

        for(int j = 0; j < 3; j++){
            dp[0][j] = temp[j];
        }

        temp[0] = a + max(dp[1][0], dp[1][1]);
        temp[1] = b + max({dp[1][0], dp[1][1], dp[1][2]});
        temp[2] = c + max(dp[1][1], dp[1][2]);

        for(int j = 0; j < 3; j++){
            dp[1][j] = temp[j];
        }
    }

    cout << max({dp[1][0], dp[1][1], dp[1][2]}) << " " << min({dp[0][0], dp[0][1], dp[0][2]});
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    init();
    solve();

    return 0;
}

