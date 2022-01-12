#include <bits/stdc++.h>
using namespace std;
int N;

int main() {
    cin >> N;
    vector<int> arr(N);
    iota(arr.begin(), arr.end(), 1);
    do {
        for(auto &w : arr) cout << w << ' ';
        cout << '\n';
    } while(next_permutation(arr.begin(), arr.end()));
}