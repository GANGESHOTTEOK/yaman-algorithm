#include <bits/stdc++.h>
using namespace std;

int solution(int cacheSize, vector<string> cities) {
    deque<string> cache(cacheSize);
    int answer = 0;

    // 캐시 크기가 0이면 cities크기에 5를 곱한 값 반환
    if (cacheSize == 0) {
        return cities.size() * 5;
    }

    for (auto it = cities.begin(); it != cities.end(); it++) {
        // 대소문자 구분하지 않으니까 모두 소문자로 변경
        transform(it->begin(), it->end(), it->begin(), ::tolower);

        // 캐시 크기가 cacheSize보다 작으면 cache miss
        if (cache.size() < cacheSize) {
            cache.push_back(*it);
            answer += 5;
        }
        // 캐시 크기가 cacheSize와 같다면
        else {
            auto pos = find(cache.begin(), cache.end(), *it);
            // 도시가 캐시에 존재하면 cache hit
            if (pos != cache.end()) {
                cache.erase(pos);
                cache.push_back(*it);
                answer += 1;
            }
            // 도시가 캐시에 존재하지 않으면 cache miss
            else {
                cache.pop_front();
                cache.push_back(*it);
                answer += 5;
            }
        }
    }
    return answer;
}