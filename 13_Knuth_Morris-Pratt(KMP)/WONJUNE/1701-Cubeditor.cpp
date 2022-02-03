#include <bits/stdc++.h>

using namespace std;

string str;
vector<int> pi;

void init(){
    cin >> str;
}

void solve(){
    int ans = 0;
    if(str.length() == 1){
        cout << 0;
        return;
    }

    int subNum = str.length();
    for(int i = 0; i < subNum-1; i++){
        pi = vector<int>(str.length());
        int k = 0;
        for(int j = 1; j < str.length(); j++){
            while(k > 0 && str[k] != str[j]){
                k = pi[k-1];
            }
            if(str[k] == str[j]){
                pi[j] = ++k;
                ans = max(pi[j], ans);
            }
        }
        str = str.substr(1, str.length());
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

