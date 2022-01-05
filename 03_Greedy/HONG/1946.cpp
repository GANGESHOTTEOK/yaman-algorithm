#include <bits/stdc++.h>
using namespace std;
int T, N, doc, itv;

int getEmploees(set<pair<int, int>> &eval) {
    int count=0, max_num=0;
    for(auto &p : eval) 
        if(max_num < p.second) {
            max_num = p.second;
            count++;
        }
    return count++;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);cout.tie(NULL);
    
    cin >> T;
    while(T--) {
        cin >> N;
        set<pair<int, int>> eval;
        int n = N;
        while(n-- && cin >> doc >> itv) eval.emplace(doc, N - itv + 1);
        cout << getEmploees(eval) << '\n';
    }
}