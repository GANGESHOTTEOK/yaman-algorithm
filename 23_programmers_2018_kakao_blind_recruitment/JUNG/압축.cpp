#include <bits/stdc++.h>
using namespace std;

map<string, int> dict;

void init_dict() {
    for (int i = 0; i < 26; i++) {
        string str;
        str.push_back(char(i + 'A'));
        dict.insert({str, i + 1});
    }
}

vector<int> solution(string msg) {
    vector<int> answer;
    init_dict();

    string target = "";
    int prev_idx = 0;

    int now = 0;
    while (true) {
        if (now >= msg.size()) break;

        char w = msg[now];
        target += w;

        auto it = dict.find(target);
        // 없음
        if (it == dict.end()) {
            cout << target << endl;
            dict.insert({target, dict.size() + 1});
            answer.push_back(prev_idx);
            target = "";
        }
        // 있음
        else {
            prev_idx = it->second;
            now++;
        }
    }
    // 마지막 글자 처리
    answer.push_back(prev_idx);

    return answer;
}