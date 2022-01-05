#include <bits/stdc++.h>
using namespace std;

int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

bool bfs(auto& graph, int m, int n, int x, int y) {
    if (graph[x][y] == 0)
        return false;

    queue<pair<int, int>> que;
    graph[x][y] = 0;
    que.push(pair<int, int>(x, y));

    while (!que.empty()) {
        auto front = que.front();
        que.pop();
        for (int i = 0; i < 4; i++) {
            int nx = front.first + dx[i];
            int ny = front.second + dy[i];
            if (nx <= -1 || ny <= -1 || nx >= m || ny >= n) continue;
            if (graph[nx][ny] == 1) {
                graph[nx][ny] = 0;
                que.push(pair<int, int>(nx, ny));
            }
        }
    }
    return true;
}

int main(void) {
    int T;
    cin >> T;

    while (T--) {
        int m, n, k, x, y, count = 0;
        cin >> m >> n >> k;
        vector<vector<int>> graph(m, vector<int>(n));

        for (int i = 0; i < k; i++) {
            cin >> x >> y;
            graph[x][y] = 1;
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (bfs(graph, m, n, i, j) == true) count++;
            }
        }
        cout << count << "\n";
    }
    return 0;
}