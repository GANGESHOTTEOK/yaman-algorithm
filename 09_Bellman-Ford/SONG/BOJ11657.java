package bellman_ford;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ11657 {

	static class Edge {
		int start, end, cost;

		public Edge(int start, int end, int cost) {
			this.start = start;
			this.end = end;
			this.cost = cost;
		}
	}

	static int N, M;
	static long[] dist;
	static Edge[] edgeList;
	static int ans;
	static boolean infFlag;

	static final int INF = 100000000;

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		edgeList = new Edge[M + 1];

		int a, b, c;
		for (int i = 1; i <= M; i++) {
			st = new StringTokenizer(br.readLine());
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			c = Integer.parseInt(st.nextToken());

			edgeList[i] = new Edge(a, b, c);
		}
		dist = new long [N+1];
		for (int i = 2; i <= N; i++) {
			dist[i] = INF;
		}
		BellmanFord();

		if (infFlag) {
			System.out.print(-1);
		}
		else {
			StringBuilder sb = new StringBuilder();
			for (int i = 2; i<=N; i++) {
				if (dist[i]==INF) {
					sb.append("-1\n");
				}
				else {
					sb.append(dist[i]+"\n");
				}
			}
			System.out.print(sb);
		}
	}

	static void BellmanFord() {
		for (int i = 1; i < N; i++) {
			for (int j = 1; j <= M; j++) {
				Edge now = edgeList[j];

				if (dist[now.start] == INF)
					continue;
				
				dist[now.end] = Math.min(dist[now.end], dist[now.start] + now.cost);
			}
		}

		for (int j = 1; j <= M; j++) {
			Edge now = edgeList[j];

			if (dist[now.start] == INF)
				continue;

			if (dist[now.start] + now.cost < dist[now.end]) {
				infFlag = true;
				return;
			}
		}
	}

}
