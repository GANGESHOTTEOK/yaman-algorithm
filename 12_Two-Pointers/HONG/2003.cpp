#include <bits/stdc++.h>
using namespace std;
int N, M, A[10001];

int main() {
    cin >> N >> M;
    for(int i=0;i<N;i++) cin >> A[i];

    int l = 0, r = 0, cnt = 0, sum = 0;
    while(1) {
        
        if(sum >= M) sum -= A[l++];
        else if(r > N) break;
        else sum += A[r++];

        if(sum == M) cnt++;
    }
    cout << cnt;
}