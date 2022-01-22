
#include <bits/stdc++.h>
#define INF 100000
using namespace std;

int N, S;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> N >> S;
	queue<int> sub;
	int ans = INF, num;
	int sum = 0;
	for(int i = 0; i < N; i++){
        cin >> num;
        sub.push(num);
        sum+=num;
        while(sum >= S){
            ans = min(ans,(int)sub.size());
            sum -= sub.front();
            sub.pop();
        }
	}
	ans != INF ? cout << ans : cout << 0;
	return 0;
}
