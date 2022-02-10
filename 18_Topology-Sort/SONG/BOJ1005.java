import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ1005 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());
        while(T-->0) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken()); // 건물 개수
            int K = Integer.parseInt(st.nextToken()); // 규칙 개수
        
            st = new StringTokenizer(br.readLine());
            int[] time = new int[N+1];
            for(int i=1; i<=N; i++) {
                time[i] = Integer.parseInt(st.nextToken());
            }

            int[] dp = time.clone();
            int[] indeg = new int[1001];

            ArrayList<Integer>[] list = new ArrayList[1001];
            for(int i=1; i<=N; i++) {
                list[i] = new ArrayList<Integer>();
            }

            for(int i=0; i<K; i++) {
                st = new StringTokenizer(br.readLine());
                int in = Integer.parseInt(st.nextToken());
                int out = Integer.parseInt(st.nextToken());

                indeg[out]++;
                list[in].add(out);
            }

            int W = Integer.parseInt(br.readLine());
            Queue<Integer> q = new LinkedList<Integer>();

            for(int i=1; i<=N; i++) {
                if(indeg[i] == 0) q.add(i);
            }

            while(!q.isEmpty()) {
                int curr = q.poll();

                for(int i=0; i<list[curr].size(); i++) {
                    int next = list[curr].get(i);
                    indeg[next]--;
                    if(indeg[next] == 0) q.add(next);
                    dp[next] = Math.max(dp[next], dp[curr]+time[next]);
                }
            }

            System.out.println(dp[W]);
        }
    }
}
