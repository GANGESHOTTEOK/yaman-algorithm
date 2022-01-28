#include <bits/stdc++.h>

using namespace std;

int N, K;
int word[50];
int learn = 0;

int dfs(int idx, int learning){
    int cnt = 0;

    if(learning == K){
        for(int i = 0; i < N; i++){
            if((word[i] & learn) == word[i])
                cnt++;
        }
        return cnt;
    }

    for(int i = idx; i < 26; i++){
        if((learn & (1 << i)) == 0){
            learn |= (1 << i);
            cnt = max(cnt, dfs(i+1,learning+1));
            learn &= ~(1 << i);
        }
    }
    return cnt;
}

void init(){
    cin >> N >> K;
    for(int i = 0; i < N; i++){
        string str;
        cin >> str;
        for(int j = 0; j < str.length(); j++){
            word[i] |= (1 << (str[j] - 'a'));
        }
    }

    char c[5] = {'a', 'c', 't', 'i', 'n'};
    for(int i = 0; i < 5; i++){
        learn |= (1 << (c[i] - 'a'));
    }
}

void solve(){
    if(K < 5){
        cout << 0;
    }
    else if(K == 26){
        cout << N;
    }
    else{
        cout << dfs(0, 5);
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

