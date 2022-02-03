#include <bits/stdc++.h>

using namespace std;

double x[10000], y[10000];
int N; 
double sum = 0;

double ccw(double x1, double x2, double x3, double y1, double y2, double y3) {
    double rtn = x1*y2 + x2*y3 + x3*y1;
    rtn -= y1*x2 + y2*x3 + y3*x1;
    return rtn / 2.0;
}

void init(){
    cin >> N;
    for(int i=0;i<N;i++)
        cin >> x[i] >> y[i];
}

void solve(){
    for(int i=1;i<N-1;i++)
        sum += ccw(x[0], x[i], x[i+1], y[0], y[i], y[i+1]);
    cout << fixed;
    cout.precision(1);
    cout << abs(sum);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    init();
    solve();
    
    return 0;
}
