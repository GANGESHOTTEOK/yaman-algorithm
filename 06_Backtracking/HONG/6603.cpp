#include <bits/stdc++.h>
using namespace std;
int k, result[6];

void selectSix(vector<int> arr, vector<bool> visited, int level, int idx) {
    if(level == 6) {
        for(int i=0;i<6;i++) cout << result[i] << ' ';
        cout << endl;
        return;
    }

    for(int i=idx;i<k;i++) {
        if(visited[i]) continue;
        visited[i] = true;
        result[level] = arr[i];
        selectSix(arr, visited, level+1, i+1);
        visited[i] = false;
    }
}

int main() {
    while(cin >> k && k != 0) {
        vector<int> arr(k, 0);
        vector<bool> visited(k, false);

        sort(arr.begin(), arr.end());
        for(int i=0;i<k;i++) cin >> arr[i];

        selectSix(arr, visited, 0, 0);
        cout << '\n';
    }
}
