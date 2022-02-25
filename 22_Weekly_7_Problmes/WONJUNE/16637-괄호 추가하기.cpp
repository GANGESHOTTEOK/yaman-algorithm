#include <bits/stdc++.h>

using namespace std;

int N;
string equation;
vector<int> operand;
vector<char> op;
bool brace[11] = {false, };
int ans = -2'147'483'648;

int calc(int x, int y, char o){
    switch(o){
        case '+':
            x += y;
            break;
        case '-':
            x -= y;
            break;
        case '*':
            x *= y;
            break;
    }
    return x;
}

void check(vector<int> num, vector<char> o){
    for(int i = 1; i <= o.size(); i++){
        if(brace[i]){
            num[i-1] = calc(num[i-1], num[i], o[i-1]);
        }
    }
    int temp = num[0];
    for(int i = 1; i <= o.size(); i++){
        if(brace[i]) continue;
        temp = calc(temp, num[i], o[i-1]);
    }
    ans = max(ans, temp);
}

void backTracking(int idx){
    check(operand, op);

    for(int i = idx; i <= op.size(); i++){
        if(!brace[i-1]){
            brace[i] = true;
            backTracking(i+1);
            brace[i] = false;
        }
    }
}

void init(){
    cin >> N >> equation;
    for(int i = 0; i < N; i++){
        if(i%2){
            op.emplace_back(equation[i]);
        }
        else{
            operand.emplace_back(equation[i] - '0');
        }
    }
}

void solve(){
    backTracking(1);
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

