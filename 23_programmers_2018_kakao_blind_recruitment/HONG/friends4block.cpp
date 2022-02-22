#include <bits/stdc++.h>
using namespace std;
int M, N, answer;

bool canErase(vector<string> &board, int y, int x) {
    char shape = board[y][x];
    if(shape == ' ') return false;
    for(int i=y;i<=y+1;i++) for(int j=x;j<=x+1;j++)
        if(shape != board[i][j]) return false;
    return true;
}   

void moveDown(vector<string> &board, int x, int y) {
    for(int i=y;i>0;i--) board[i][x] = board[i-1][x];
    board[0][x] = ' ';
}

int solution(int m, int n, vector<string> board) {
    bool flag = true;

    while(flag) { 
        set<pair<int, int>> targets;
        flag = false;

        for(int i=0;i<m-1;i++) for(int j=0;j<n-1;j++) {
            if(!canErase(board, i, j)) continue;
            for(int k=i;k<=i+1;k++) for(int l=j;l<=j+1;l++)
                targets.emplace(l, k);
            flag = true;
        }

        for(auto &p : targets) moveDown(board, p.first, p.second);
        answer += targets.size();
    }    
    return answer;
}