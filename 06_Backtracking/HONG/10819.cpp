#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, x;
    cin >> N;
    vector<int> arr(N);
    for(int i=0;i<N;i++) cin >> arr[i];
    sort(arr.begin(), arr.end());

    int max_sum = 0;
    do {
        int sum = 0;
        for(int i=0;i<N-1;i++) sum += abs(arr[i] - arr[i+1]);
        max_sum = max(sum, max_sum);
    } while(next_permutation(arr.begin(), arr.end()));

    cout << max_sum;
}