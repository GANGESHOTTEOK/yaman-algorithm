#include<bits/stdc++.h>
using namespace std;
vector<string> board;
string result, path;
int R, C;

void solve(int y, int x) {
    bool flag = false;

    if(x!=0 && path.find(board[y][x-1])==string::npos) {
        path.push_back(board[y][x-1]);
        solve(y, x-1);
        flag = true;
    }
    if(y!=0 && path.find(board[y-1][x])==string::npos) {
        path.push_back(board[y-1][x]);
        solve(y-1, x);
        flag = true;
    }
    if(x!=C-1 && path.find(board[y][x+1])==string::npos) {
        path.push_back(board[y][x+1]);
        solve(y, x+1);
        flag = true;
    }
    if(y!=R-1 && path.find(board[y+1][x])==string::npos) {
        path.push_back(board[y+1][x]);
        solve(y+1, x);
        flag = true;
    }

    if(!flag) result = result.length() < path.length() ? path : result;
    path.pop_back();
}

int main() {
    cin >> R >> C;

    char c;
    for(int i=0;i<R;i++) {
        string tmp;
        for(int i=0;i<C && cin>>c;i++) tmp.push_back(c);
        board.push_back(tmp);
    }

    path.push_back(board[0][0]);
    solve(0, 0);
    
    cout << result.length();
}   