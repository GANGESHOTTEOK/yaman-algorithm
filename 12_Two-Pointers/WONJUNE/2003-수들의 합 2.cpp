#include <bits/stdc++.h>

using namespace std;

int N, M, ans = 0;
vector<int> vec;

void init(){
    cin >> N >> M;
    vec.resize(N+1);

    for(int i = 1; i <= N; i++){
        cin >> vec[i];
        vec[i] += vec[i-1];
    }
}

void solve(){
    int i = 0, j = 0;
    while(1){
        if(i < N && vec[j] - vec[i] > M){
            i++;
        }
        else if(j < N && vec[j] - vec[i] < M){
            j++;
        }
        else if(vec[j] - vec[i] == M){
            ans++;
            if(i < N) i++;
            if(j < N) j++;
        }
        else{
            if(i < N) i++;
            if(j < N) j++;
        }

        if(i == N && j == N) break;
    }
    cout << ans;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    init();
    solve();

    return 0;
}

