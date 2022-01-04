#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, K;
    cin >> N >> K;

    queue<pair<int, int>> q;
    bool visited[100002] = {false,};
    visited[N] = true;
    q.push({N, 0});

    while(!q.empty()) {
        int curr = q.front().first;
        int time = q.front().second;
        if(curr == K) break;
        q.pop();

        if(curr > 0 && !visited[curr-1]) {
            visited[curr-1] = true;
            q.push({curr-1, time+1});
        }
        if(curr < 100001 && !visited[curr+1]) {
            visited[curr+1] = true;
            q.push({curr+1, time+1});
        }
        if(curr*2 < 100001 && !visited[curr*2]) {
            visited[curr*2] = true;
            q.push({curr*2, time+1});
        }
    }
    cout << q.front().second;
}