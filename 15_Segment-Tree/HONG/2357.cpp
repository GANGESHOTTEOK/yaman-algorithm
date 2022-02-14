#include <bits/stdc++.h>
using namespace std;
using pll = pair<long, long>;
using ll = long long;
int N, M, n, a, b; 
vector<ll> num;
vector<pll> tree;

void input() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> N >> M;
    num.resize(N+1);
    tree.resize(1 << (int)ceil(log2(N) + 1));
    for(int i=1;i<=N;i++) cin >> num[i];
}

pll init(ll start, ll end, ll idx) {
    if(start == end) return tree[idx] = {num[start], num[start]};
    int mid = (start + end) / 2;
    pll left = init(start, mid, 2*idx), right = init(mid+1, end, 2*idx+1);
    return tree[idx] = {min(left.first, right.first), max(left.second, right.second)};
}

pll findMinMax(ll start, ll end, ll idx, ll left, ll right) {
    if(left > end || right < start) return {LLONG_MAX, LLONG_MIN};
    if(left <= start && end <= right) return {tree[idx].first, tree[idx].second};
    int mid = (start + end) / 2;
    pll l = findMinMax(start, mid, 2*idx, left, right), r = findMinMax(mid+1, end, 2*idx+1, left, right);
    return {min(l.first, r.first), max(l.second, r.second)};
}

int main() {
    input();
    init(1, N, 1);
    // for(int i=1;i<=tree.size();i++) cout << tree[i].first << ' ' << tree[i].second << endl; cout << endl;  

    while(cin >> a >> b) {
        auto res = findMinMax(1, N, 1, a, b);
        cout << res.first << ' ' << res.second << '\n';
    }
}