#include <bits/stdc++.h>

using namespace std;

int N, M, K;
long long tree[1 << 21] = {0, };
int leaf = 1;

void treeInit(long long val, int idx, int pos, int left, int right){
    if(left == right){
        tree[pos] = val;
        return;
    }

    int mid = (left+right)/2;
    if(idx <= mid){
        tree[pos] += val;
        treeInit(val, idx, 2*pos, left, mid);
    }
    else if(mid < idx){
        tree[pos] += val;
        treeInit(val, idx, 2*pos+1, mid+1, right);
    }
}

int treeUpdate(long long val, int idx, int pos, int left, int right){
    long long diff = 0;
    if(left == right){
        diff = tree[pos] - val;
        tree[pos] = val;
        return diff;
    }

    int mid = (left+right)/2;
    if(idx <= mid){
        diff = treeUpdate(val, idx, 2*pos, left, mid); 
        tree[pos] -= diff;
    }
    else if(mid < idx){
        diff = treeUpdate(val, idx, 2*pos+1, mid+1, right);
        tree[pos] -= diff;
    }
    return diff;
}

long long treeSum(int start, int end, int pos, int left, int right){
    long long sum = 0;

    if(start == left && end == right){
        return tree[pos];
    }

    int mid = (left+right)/2;
    if(end <= mid){
        sum += treeSum(start, end, 2*pos, left, mid);
    }
    else if(mid+1 <= start){
        sum += treeSum(start, end, 2*pos+1, mid+1, right);
    }
    else{
        sum += treeSum(start, mid, 2*pos, left, mid);
        sum += treeSum(mid+1, end, 2*pos+1, mid+1, right);
    }
    return sum;
}

void init(){
    cin >> N >> M >> K;
    while(leaf < N){
        leaf <<= 1;
    }
}

void solve(){
    long long value;
    for(int i = 1; i <= N; i++){
        cin >> value;
        treeInit(value, i, 1, 1, leaf);
    }

    int a, b;
    long long c;
    for(int i = 0; i < M+K; i++){
        cin >> a >> b >> c;
        if(a == 1){
            treeUpdate(c, b, 1, 1, leaf);
        }
        else{
            cout << treeSum(b, (int)c, 1, 1, leaf) << "\n";
        }
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

