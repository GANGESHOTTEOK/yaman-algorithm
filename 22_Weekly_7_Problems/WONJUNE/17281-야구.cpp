#include <bits/stdc++.h>

using namespace std;

int N;
int person = 9;
int ability[50][10];
int ans = 0;
int order[9] = {0, };
bool orderCheck[9] = {false, };

void init(){
    cin >> N;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < person; j++){
            cin >> ability[i][j];
        }
    }
}

void play(){
    int point = 0;
    int o = 0;
    for(int i = 0; i < N; i++){
        int out = 0;
        bool base[3] = {false, };
        while(out != 3){
            switch(ability[i][order[o]]){
                case 1:
                    if(base[2]) point++;
                    base[2] = base[1];
                    base[1] = base[0];
                    base[0] = true;
                    break;
                case 2:
                    if(base[2]) point++, base[2] = false;
                    if(base[1]) point++, base[1] = false;
                    base[2] = base[0];
                    base[0] = false;
                    base[1] = true;
                    break;
                case 3:
                    for(int j = 0; j < 3; j++){
                        if(base[j]) point++;
                        base[j] = false;
                    }
                    base[2] = true;
                    break;
                case 4:
                    for(int j = 0; j < 3; j++){
                        if(base[j]) point++;
                        base[j] = false;
                    }
                    point++;
                    break;
                default:
                    out++;
            }
            o++;
            o %= person;
        }
    }
    ans = max(ans, point);
}

void backTracking(int idx){
    if(idx == 3) idx++;
    if(idx == person) {
        play();
        return;
    }
    for(int i = 0; i < person; i++){
        if(!orderCheck[i]){
            order[idx] = i;
            orderCheck[i] = true;
            backTracking(idx+1);
            orderCheck[i] = false;
        }
    }
}

void solve(){
    order[3] = 0;
    orderCheck[0] = true;
    backTracking(0);

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

