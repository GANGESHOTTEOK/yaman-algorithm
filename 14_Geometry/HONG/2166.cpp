#include <bits/stdc++.h>
using namespace std;
double x[10000], y[10000];

double ccw(long long x1, long long x2, long long x3, long long y1, long long y2, long long y3) {
    double rtn = x1*y2 + x2*y3 + x3*y1;
    rtn -= y1*x2 + y2*x3 + y3*x1;
    return rtn / 2.0;
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int N; cin >> N;
    for(int i=0;i<N;i++) cin >> x[i] >> y[i];
    
    double sum = 0;

    for(int i=1;i<N-1;i++)
        sum += ccw(x[0], x[i], x[i+1], y[0], y[i], y[i+1]);
    
    printf("%.1lf", abs(sum));
}