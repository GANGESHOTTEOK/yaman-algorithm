#include <bits/stdc++.h>

using namespace std;

int x[3], y[3];

double ccw(){
    return (x[0]*y[1] - x[1]*y[0] + x[1]*y[2] - x[2]*y[1] + x[2]*y[0] - x[0]*y[2]) / 2.0;
}

void init(){
    for(int i = 0; i < 3; i++){
        cin >> x[i] >> y[i];
    }
}

void solve(){
    double state = ccw();
    if(state > 0) cout << 1;
    else if(state < 0) cout << -1;
    else cout << 0;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    init();
    solve();

    return 0;
}

