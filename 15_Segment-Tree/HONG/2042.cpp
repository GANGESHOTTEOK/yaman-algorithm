#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int N, n, M, K;
ll a, b, c, arr[1000001];

void input() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> N >> M >> K;
    for(int i=1;i<=N;i++) cin >> arr[i];
}

ll init(vector<ll> &tree, int start, int end, int node) {
    if(start == end) return tree[node] = arr[start];
    int mid = (start + end) / 2;
    return tree[node] = init(tree, start, mid, node*2) + init(tree, mid+1, end, node*2+1);
}

ll sum(vector<ll> &tree, int start, int end, int node, int left, int right) {
    if(left > end || right < start) return 0;
    if(left <= start && end <= right) return tree[node];
    int mid = (start + end) / 2;
    return sum(tree, start, mid, node*2, left, right) + sum(tree, mid+1, end, node*2+1, left, right);
}

void update(vector<ll> &tree, int start, int end, int node, int target, ll diff) {
    if(target > end || target < start) return;
    tree[node] += diff;
    
    int mid = (start + end) / 2;
    if(start != end) {
        update(tree, start, mid, node*2, target, diff);
        update(tree, mid+1, end, node*2+1, target, diff);
    }
}

int main() {
    input();

    vector<ll> tree(1 << (int)ceil(log2(N) + 1));
    init(tree, 1, N, 1);

    while(cin >> a >> b >> c)
        if(a==2) cout << sum(tree, 1, N, 1, b, c) << '\n';
        else {
            update(tree, 1, N, 1, b, c-arr[b]);
            arr[b] = c;
        }
}
