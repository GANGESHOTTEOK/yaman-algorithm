#include <bits/stdc++.h>
using namespace std;

int ccw(int x1, int x2, int x3, int y1, int y2, int y3) {
    return (x1*y2+x2*y3+x3*y1 - y1*x2-y2*x3-y3*x1) / 2;
}

int main() {
    int N; cin >> N;
    vector<pair<int, int>> points;

    int x, y, sum=0;
    while(cin >> x >> y) points.emplace_back(x, y);

    for(auto &p : points) {
        if(p == points[0]) continue;
        sum += ccw()
    }
}