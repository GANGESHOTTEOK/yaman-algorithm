#include <bits/stdc++.h>
using namespace std;

int solution(int cacheSize, vector<string> cities) {
    int time = 0;
    list<string> cache; 
    
    for(auto &city : cities) {
        auto it=cache.begin();
        transform(city.begin(), city.end(), city.begin(), ::tolower);
        while(true) {
            if(it == cache.end()) {
                cache.push_back(city);
                if(cache.size() > cacheSize) cache.pop_front();
                time+=5;
                break;
            }
            
            if(*it == city) {
                cache.splice(cache.end(), cache, it);
                time++;
                break;
            }
            it++;
            continue;
        }
    }
    
    return time;
}