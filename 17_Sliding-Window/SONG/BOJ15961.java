import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ15961 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()); // 초밥 개수
        int d = Integer.parseInt(st.nextToken()); // 종류
        int k = Integer.parseInt(st.nextToken()); // 연속으로 먹는 수
        int c = Integer.parseInt(st.nextToken()); // 쿠폰

        int sushiBelt[] = new int[N];
        for(int i=0; i<N; i++) {
            sushiBelt[i] = Integer.parseInt(br.readLine());
        }

        int eat[] = new int[d+1]; // 지금 먹은 스시 종류별 몇 개인지 표시
        int max = 0;
        int cnt = 0;
        for(int i=0; i<k; i++) {
            eat[sushiBelt[i]]++; // 먹음
            if( eat[sushiBelt[i]] == 1 ) { // 처음 먹었으면
                cnt++;
            }
        }
        
        for(int i=1; i<N; i++) {
            if(max <= cnt) {
                if(eat[c] == 0) {
                    max = cnt + 1;
                } else {
                    max = cnt;
                }
            }

            // 맨 앞에 먹은거 제외
            eat[sushiBelt[i-1]]--;
            if( eat[sushiBelt[i-1]] == 0) { // 종류 줄어드니까
                cnt--;
            }

            // 그 뒤에거 먹기
            if( eat[sushiBelt[(i+k-1) % N]] == 0) cnt++;
            eat[sushiBelt[(i+k-1) % N]]++;
        }

        System.out.println(max);
    }
}
