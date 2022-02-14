#include <bits/stdc++.h>

using namespace std;

int N, L;
int road[202][101];
int ans = 0;

void init(){
    cin >> N >> L;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            cin >> road[i][j];
        }
    }
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            road[N+i][j] = road[j][i];
        }
    }
}

void solve(){
    for(int i = 0; i < 2*N; i++){
        int cnt = 1;
        int pre = road[i][0];
        bool check = true, pass = true;
        for(int j = 1; j < N; j++){
            int cur = road[i][j];
            if(pre == cur){
                cnt++;
                if(!check && cnt >= L){
                    cnt -= L;
                    check = true;
                }
            }
            else if(pre-1 == cur){
                if(!check){
                    pass = false;
                    break;
                }
                cnt = 1;
                if(cnt < L){
                    check = false;
                }
                else{
                    cnt = 0;
                }
            }
            else if(pre+1 == cur){
                if(cnt < L){
                    pass = false;
                    break;
                }
                else{
                    cnt = 1;
                }
            }
            else{
                pass = false;
                break;
            }
            pre = cur;
        }
        if(pass && check){
            ans++;
        }
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

