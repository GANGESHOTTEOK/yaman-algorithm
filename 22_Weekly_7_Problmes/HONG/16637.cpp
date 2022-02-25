#include <bits/stdc++.h>
using namespace std;
int N, maxVal = INT_MIN; 
string inp;

int calc(int a, int b, char op) {
    switch (op) {
        case '+' : return a+b;
        case '-' : return a-b;
        case '*' : return a*b;
    }
    return 0;
}

void fx(int idx, int val) {

    if(idx >= N) {
        maxVal = max(maxVal, val);
        return;
    }

    char op = idx ? inp[idx-1] : '+';
    int next_val = calc(val, inp[idx] - '0', op);
    
    // 그냥 연산 하기
    fx(idx+2, next_val);

    // 괄호 묶어서 연산
    if(idx >= N-2) return;

    int temp = calc(inp[idx] - '0', inp[idx+2] - '0', inp[idx+1]);
        temp = calc(val, temp, op);
    
    fx(idx+4, temp);
}

int main() {
    cin >> N >> inp;
    fx(0, 0);
    cout << maxVal;
}