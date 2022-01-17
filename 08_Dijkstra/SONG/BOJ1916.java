package dijkstra;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class BOJ1916 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	
	static class Node implements Comparable<Node> {
		int to, weight;
		Node next;
		
		public Node(int to, int weight, Node next) {
			this.to = to;
			this.weight = weight;
			this.next = next;
		}

		@Override
		public int compareTo(Node o) {
			return this.weight - o.weight;
		}
	}
	
	static Node[] list;
	static int[] dist;
	static boolean[] visit;
	static int N, M;
	
	public static void main(String[] args) throws IOException {
		N = Integer.parseInt(br.readLine());
		M = Integer.parseInt(br.readLine());
		
		list = new Node[N+1];
		dist = new int[N+1];
		visit = new boolean[N+1];
		
		Arrays.fill(dist, Integer.MAX_VALUE >> 1);
		
		for (int i=0; i<M; i++) {
			st = new StringTokenizer(br.readLine());
			int from = Integer.parseInt(st.nextToken());
			int to = Integer.parseInt(st.nextToken());
			int weight = Integer.parseInt(st.nextToken());
			
			list[from] = new Node(to, weight, list[from]);
		}
		
		st = new StringTokenizer(br.readLine());
		int start = Integer.parseInt(st.nextToken());
		int end = Integer.parseInt(st.nextToken());
		
		System.out.println(dijkstra(start, end));
	}
	
	static int dijkstra(int start, int end) {
		PriorityQueue<Node> queue = new PriorityQueue<>();
		queue.offer(new Node(start, 0, list[start]));
		dist[start] = 0;
		
		while (!queue.isEmpty()) {
			Node node = queue.poll();
			
			if (node.to == end) return node.weight;
			
			if (visit[node.to]) continue;
			visit[node.to] = true;
			
			for (Node temp = node.next; temp != null; temp = temp.next) {
				if (dist[temp.to] > dist[node.to] + temp.weight) {
					dist[temp.to] = dist[node.to] + temp.weight;
					queue.offer(new Node(temp.to, dist[temp.to], list[temp.to]));
				}
			}
		}
		return -1;
	}
}