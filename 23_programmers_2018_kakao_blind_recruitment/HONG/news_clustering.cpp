#include <string>
#include <iostream>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

int isCapital(char c) {
    if('A' <= c && c <= 'Z') return 1;
    else if('a' <= c && c <= 'z') return 0;
    else return -1;
}

multiset<string> splitTwo(string inp) {
    string str;

    for(int i=0;i<inp.size();i++) {
        int result = isCapital(inp[i]);
        if(result == 1) str.push_back(inp[i]-'A'+'a');
        else if(!result || i) str.push_back(inp[i]);
    }
    cout << str << endl;

    multiset<string> rtn;
    for(int i=0;i<(int)str.size()-1;i++) {
        if(isCapital(str[i+1]) == -1 || isCapital(str[i]) == -1) continue;
        string tmp;
        tmp.push_back(str[i]);
        tmp.push_back(str[i+1]);
        rtn.insert(tmp);

    }
    return rtn;
}

int solution(string str1, string str2) {
    int answer = 0;

    multiset<string> set1 = splitTwo(str1);
    multiset<string> set2 = splitTwo(str2);

    vector<string> inter, uni;

    set_intersection(set1.begin(), set1.end(), set2.begin(), set2.end(), back_inserter(inter));
    set_union(set1.begin(), set1.end(), set2.begin(), set2.end(), back_inserter(uni));

    cout << inter.size() << ' ' << uni.size() << endl;

    for(auto &w : inter) cout << w << ' '; cout << endl;
    for(auto &w : uni) cout << w << ' '; cout << endl;

    if(uni.size() == 0) return 65536;
    return (int) ((double)inter.size() / (double)uni.size()  * 65536);
}