#include <bits/stdc++.h>
using namespace std;
int N, M, n, a, b, num[100001];

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> N >> M;

    for(int i=1;i<=N;i++) cin >> num[i];

    for(auto &w : num) cout << w << ' '; cout << endl;

    while(cin >> a >> b) {
        cout << num[a-1] << ' ' << num[b-1] << '\n';
    }
}