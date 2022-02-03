#include <bits/stdc++.h>

using namespace std;

string P,S;
vector<int> pi;

void init(){
    cin >> P >> S;

    pi.resize(S.length());

    int k = 0;
    for(int i = 1; i < S.length(); i++){
        while(k > 0 && S[k] != S[i]){
            k = pi[k-1];
        }
        if(S[k] == S[i]){
            pi[i] = ++k;
        }
    }
}

void solve(){
    int k = 0;
    for(int i = 0; i < P.length(); i++){
        while(k > 0 && S[k] != P[i]){
            k = pi[k-1];
        }
        if(S[k] == P[i]){
            ++k;
            if(S.length() == k){
                cout << 1;
                return;
            }
        }
    }
    cout << 0;
    return;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    init();
    solve();

    return 0;
}

