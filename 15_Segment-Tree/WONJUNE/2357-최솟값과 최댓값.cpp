#include <bits/stdc++.h>
#define INF 1'000'000'001

using namespace std;

int N, M;
pair<int,int> tree[1 << 19];
int leaf = 1;

void treeInit(int val, int idx, int pos, int left, int right){
    tree[pos] = {min(tree[pos].first, val), max(tree[pos].second, val)};
    if(left == right){
        return;
    }
    int mid = (left+right)/2;
    if(idx <= mid){
        treeInit(val, idx, 2*pos, left, mid);
    }
    else if(mid < idx){
        treeInit(val, idx, 2*pos+1, mid+1, right);
    }
}

pair<int,int> findMinMax(int start, int end, int pos, int left, int right){
    if(start <= left && right <= end){
        return tree[pos];
    }

    pair<int,int> MinMax = {INF, 0}, tmp;
    int mid = (left+right)/2;

    if(end <= mid){
        tmp = findMinMax(start, end, 2*pos, left, mid);
        MinMax = {min(MinMax.first, tmp.first), max(MinMax.second, tmp.second)};
    }
    else if(mid < start){
        tmp = findMinMax(start, end, 2*pos+1, mid+1, right);
        MinMax = {min(MinMax.first, tmp.first), max(MinMax.second, tmp.second)};
    }
    else if(start <= mid && mid < end){
        tmp = findMinMax(start, mid, 2*pos, left, mid);
        MinMax = {min(MinMax.first, tmp.first), max(MinMax.second, tmp.second)};
        tmp = findMinMax(mid+1, end, 2*pos+1, mid+1, right);
        MinMax = {min(MinMax.first, tmp.first), max(MinMax.second, tmp.second)};
    }

    return MinMax;
}

void init(){
    cin >> N >> M;
    while(leaf < N){
        leaf <<= 1;
    }
    for(int i = 1; i <= 2*leaf; i++){
        tree[i] = {INF, 0};
    }
}

void solve(){
    int val, start, end;
    for(int i = 1; i <= N; i++){
        cin >> val;
        treeInit(val, i, 1, 1, leaf);
    }
    for(int i = 0; i < M; i++){
        cin >> start >> end;
        auto res = findMinMax(start, end, 1, 1, leaf);
        cout << res.first << " " << res.second << "\n";
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    init();
    solve();

    return 0;
}

