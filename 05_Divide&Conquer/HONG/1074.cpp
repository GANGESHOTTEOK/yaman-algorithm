#include <bits/stdc++.h>
using namespace std;
int N, r, c;

int getOrder(int N, int r, int c) {
    if(N == 0) return 0;
    int order = 0, half = pow(2, N-1);

    if(r < half && c < half) order += getOrder(N-1, r, c);
    else if(r < half && c >= half) order += pow(2, 2*N-2) + getOrder(N-1, r, c-half);
    else if(r >= half && c < half) order += 2 * pow(2, 2*N-2) + getOrder(N-1, r-half, c);
    else order += 3 * pow(2, 2*N-2) + getOrder(N-1, r-half, c-half);

    return order;
}

int main() {
    cin >> N >> r >> c;
    cout << getOrder(N, r, c);
}