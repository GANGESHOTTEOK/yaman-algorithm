#include <bits/stdc++.h>
using namespace std;

void printStar(vector<vector<bool>> &msg, int level, int x, int y) {
    if(level == 1) {
        msg[x][y] = true;
        return;
    }
    int div = level / 3;
    printStar(msg, div, x, y);
    printStar(msg, div, x, y+div);
    printStar(msg, div, x, y+2*div);

    printStar(msg, div, x+div, y);
    printStar(msg, div, x+div, y+2*div);

    printStar(msg, div, x+2*div, y);
    printStar(msg, div, x+2*div, y+div);
    printStar(msg, div, x+2*div, y+2*div);
}

int main() {
    int N;
    cin >> N;
    vector<vector<bool>> msg(N, vector<bool>(N, false));

    printStar(msg, N, 0, 0);

    for(auto &str : msg) {
        for(auto c : str) 
            if(c) cout << '*'; 
            else cout << ' ';
        cout << endl;
    }
}