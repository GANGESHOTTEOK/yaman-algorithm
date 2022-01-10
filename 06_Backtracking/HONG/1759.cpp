#include <bits/stdc++.h>
using namespace std;
const string VOWELS = "aeiuo";
string result;
vector<char> chr;
int L, C;

bool check() {
    int vowel = 0;
    for(auto &w : result)
        if(VOWELS.find(w) != string::npos) vowel++;
    
    if(vowel >= 1 && L-vowel >= 2) return true;
    return false;
}

void genPW(int idx) {
    if(result.length() == L) {
        if(check()) cout << result << '\n';
        return;
    };

    for(int i=idx;i<C;i++) {
        result.push_back(chr[i]);
        genPW(i+1);
        result.pop_back();
    }
}

int main() {
    cin >> L >> C;
    char c;
    while(cin >> c) chr.push_back(c);
    sort(chr.begin(), chr.end());
    genPW(0);
}