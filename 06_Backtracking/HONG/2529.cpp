#include <bits/stdc++.h>
using namespace std;
string max_num="0", min_num="987654321";
int k;

void getMinMaxNum(vector<int> &arr, vector<bool> &op) {
    do {
        bool flag = false;
        for(int i=0;i<k;i++)
            if(!op[i] && arr[i] < arr[i+1] || 
                op[i] && arr[i] > arr[i+1]) {
                flag = true;
                break;
            }
        if(flag) continue;

        string num_str;
        for(auto &w : arr) num_str.push_back(w+'0');
        max_num = max(max_num, num_str);
        min_num = min(min_num, num_str);

    } while(next_permutation(arr.begin(), arr.end()));
}

int main() {
    cin >> k;
    vector<bool> op, selector(10, true);
    char c;
    int K = k;
    while(K-- && cin >> c) op.push_back(c=='<');

    for(int i=0;i<=k;i++) selector[i] = false;

    do {
        vector<int> selected;
        for(int i=0;i<10;i++)
            if(!selector[i]) selected.push_back(i);
        getMinMaxNum(selected, op);
    } while(next_permutation(selector.begin(), selector.end()));

    cout << max_num << '\n' << min_num;
}