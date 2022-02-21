#include <bits/stdc++.h>
using namespace std;
vector<vector<int>> board(10, vector<int>(10, 0));
vector<int> papers{0, 5, 5, 5, 5, 5};
int minCount = INT_MAX;

bool isPossible(int x, int y, int size) {
    for(int i=x;i<x+size;i++)
        for(int j=y;j<y+size;j++)
            if (i>=10 || j>=10 || !board[i][j]) return false;
    return true;
}

pair<int, int> getNextPos() {
    for(int i=0;i<10;i++)
        for(int j=0;j<10;j++)
            if(board[i][j]) return {i, j};
    return {-1, -1};
}

void fillPaper(int x, int y, int size, bool color){
    for(int i=x;i<x+size;i++)
        for(int j=y;j<y+size;j++)
            board[i][j] = color;
}

void dfs(int count) {
    int x, y;
    tie(x, y) = getNextPos();

    if(x<0 && y<0) {
        minCount = min(minCount, count);
        return;
    }

    for(int k=5;k>0;k--) { // 5개의 색종이를 대어본다
        if(!isPossible(x, y, k) || !papers[k]) continue;

        fillPaper(x, y, k, 0);
        papers[k]--;
        dfs(count+1);
        papers[k]++;
        fillPaper(x, y, k, 1);
    }
}

int main() {
    ios::sync_with_stdio(0); cin.tie(NULL);

    for(int i=0;i<10;i++)
        for(int j=0;j<10;j++) cin >> board[i][j];

    dfs(0);

    if(minCount == INT_MAX) cout << "-1";
    else cout << minCount;
}