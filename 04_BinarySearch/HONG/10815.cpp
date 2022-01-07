#include <bits/stdc++.h>
using namespace std;
int N, M, num;
set<int> cards;

void input();
void solve1();
void solve2();
int binarySearch(vector<int> &cards, int target);

int main() {
    input();
    // solve1();
    solve2();
}

void input() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL); cout.tie(NULL);
    cin >> N;
    while(N-- && cin >> num) cards.emplace(num);
    cin >> M;
}

void solve1() {
    while(M-- && cin >> num) {
        auto itr = cards.find(num);
        if(itr != cards.end()) cout << 1 << ' ';
        else cout << 0 << ' ';
    }
}

void solve2() {
    vector<int> cards_vec(cards.begin(), cards.end());
    while(M-- && cin >> num) cout << binarySearch(cards_vec, num) << ' ';
}

int binarySearch(vector<int> &cards, int target) {
    int st = 0, ed = cards.size() - 1;

    while(st <= ed) {
        int mid = (st+ed) / 2;
        if(cards[mid] < target) st = mid+1;
        else if(cards[mid] > target) ed = mid-1;
        else return 1;
    }
    return 0;
}