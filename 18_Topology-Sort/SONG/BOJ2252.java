import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ2252 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] indeg = new int[32001];

        ArrayList<Integer>[] list = new ArrayList[32001];
        for(int i=1; i<=N; i++) {
            list[i] = new ArrayList<Integer>();
        }

        for(int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            int in = Integer.parseInt(st.nextToken());
            int out = Integer.parseInt(st.nextToken());

            indeg[out]++;
            list[in].add(out);
        }

        Queue<Integer> q = new LinkedList<Integer>();
        for(int i=1; i<=N; i++) {
            if(indeg[i] == 0) q.add(i);
        }

        StringBuilder sb = new StringBuilder();
        while(!q.isEmpty()) {
            int curr = q.poll();
            sb.append(curr + " ");

            for(int i=0; i<list[curr].size(); i++) {
                int next = list[curr].get(i);
                indeg[next]--;
                if(indeg[next] == 0) q.add(next);
            }
        }

        System.out.println(sb.toString());
    }
    
}