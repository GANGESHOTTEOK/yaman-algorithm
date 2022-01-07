#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, num, budget, low = 0, high = 0;
    cin >> N;
    vector<int> nums;
    while(N-- && cin >> num) {
        nums.push_back(num);
        high = max(high, num);
    }
    cin >> budget;

    int result;

    while(low <= high) {
        int mid = (low + high) / 2, sum = 0;
        for(auto &num : nums) sum += min(num, mid);
        if(sum <= budget) {
            result = mid;
            low = mid + 1;
        }
        else high = mid-1;
    }
    cout << result;
}