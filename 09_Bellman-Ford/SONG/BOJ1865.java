package bellman_ford;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ1865 {
	static class Edge {
		int start, end, cost;

		public Edge(int start, int end, int cost) {
			this.start = start;
			this.end = end;
			this.cost = cost;
		}
	}
	
	static int N, M, W;
	static int[] dist;
	static List<Edge> edgeList;
	
	static final int INF = 1000000000;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int TC = Integer.parseInt(br.readLine());
		
		StringTokenizer st;
		while(TC-->0) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			W = Integer.parseInt(st.nextToken());

			edgeList = new ArrayList<>();
			for(int i=0; i<M; i++) { // 도로의 정보
				st = new StringTokenizer(br.readLine());
				int S = Integer.parseInt(st.nextToken());
				int E = Integer.parseInt(st.nextToken());
				int T = Integer.parseInt(st.nextToken());
				edgeList.add(new Edge(S, E, T));
				edgeList.add(new Edge(E, S, T)); // 방향이 없는 그래프이므로 양방향 추가
			}
			
			for(int i=0; i<W; i++) { // 웜홀의 정보
				st = new StringTokenizer(br.readLine());
				int S = Integer.parseInt(st.nextToken());
				int E = Integer.parseInt(st.nextToken());
				int T = Integer.parseInt(st.nextToken());
				edgeList.add(new Edge(S, E, T*(-1))); // 웜홀은 방향이 있고, 시간이 거꾸로 간다
			}
			
			if(BellmanFord()) sb.append("YES\n");
			else sb.append("NO\n");
		}
		System.out.println(sb.toString());
	}
	
	static boolean BellmanFord() {
		dist = new int[N+1];
		Arrays.fill(dist, INF);
		dist[1] = 0;
		
		boolean isUpdated = false;
		for(int i = 1; i <= N; i++) {
			isUpdated = false;
			for (Edge now : edgeList) {
				if(dist[now.end] > dist[now.start] + now.cost) {
					dist[now.end] = dist[now.start] + now.cost;
					isUpdated = true;
					if(i == N) return true;
				}
			}
			if(!isUpdated) break;
		}
		
		return false;
	}
}
