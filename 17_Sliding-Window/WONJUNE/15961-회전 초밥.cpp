#include <bits/stdc++.h>

using namespace std;

int N,d,k,c;
vector<int> vec;
int num[3001] = {0,};
int cnt = 0, ans = 0;

void init(){
    cin >> N >> d >> k >> c;
    vec.resize(N+k);
    for(int i = 0; i < N; i++){
        cin >> vec[i];
    }
    for(int i = 0; i < k; i++){
        vec[N+i] = vec[i];
    }
    for(int i = 0; i < k; i++){
        if(num[vec[i]] == 0){
            cnt++;
        }
        num[vec[i]]++;
    }
}

void solve(){
    for(int i = 0; i < N; i++){
        int coupon = !num[c] ? 1 : 0;
        cnt += coupon;
        ans = max(ans, cnt);
        cnt -= coupon;
        if(num[vec[i]] == 1){
            cnt--;
        }
        num[vec[i]]--;
        if(num[vec[i+k]] == 0){
            cnt++;
        }
        num[vec[i+k]]++;
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

