#include <bits/stdc++.h>
using namespace std;

int main() {
    int x1, x2, x3, y1, y2, y3;
    cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;

    int result = x1*y2+x2*y3+x3*y1 - y1*x2-y2*x3-y3*x1;

    if(result > 0) cout << "1";
    else if(result < 0) cout << "-1";
    else cout << "0";
}
