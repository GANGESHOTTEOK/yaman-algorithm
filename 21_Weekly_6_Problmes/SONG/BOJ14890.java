import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ14890 {
	static int n, l, road;
	static int[][] arr;
	static Queue<Integer> q = new LinkedList<>();

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());
		n = Integer.parseInt(st.nextToken());
		l = Integer.parseInt(st.nextToken());
		arr = new int[n][n];
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(bf.readLine());
			for (int j = 0; j < n; j++)
				arr[i][j] = Integer.parseInt(st.nextToken());
		}

		for (int i = 0; i < n; i++) {
			q.clear();
			// 행
			for (int j = 0; j < n; j++) {
				int current = arr[i][j];
				if (q.isEmpty() || q.peek() == current) {
					q.offer(current);
				} else if(Math.abs(q.peek() - current) > 1) { // 안 되는 경우
					break;
				} else if (q.peek() < current) { // 올라갈 때
					if (q.size() >= l) {
						q.clear();
						q.offer(current);
					} else
						break;
				} else { // 내려갈때
					boolean flag = true;
					for (int k = 0; k < l; k++) {
						if (j + k >= n || arr[i][j + k] != current) {
							flag = false;
							break;
						}
					}
					if (!flag) {
						break;
					}
					else {
						j = j + l - 1;
						if(j+1<n && current < arr[i][j+1]) break;
						q.clear();
						if(j+1<n && current > arr[i][j+1])
							q.offer(arr[i][j]);
					}
				}
				if (j == n - 1){
					road++;
				}
			}

			q.clear();
			// 열
			for (int j = 0; j < n; j++) {
				int current = arr[j][i];
				if (q.isEmpty() || q.peek() == current) {
					q.offer(current);
				} else if(Math.abs(q.peek() - current) > 1) {
					break;
				} else if (q.peek() < current) { // 더 높은 곳으로 올라갈 때
					if (q.size() >= l) {
						q.clear();
						q.offer(current);
					} else 
						break;
				} else { // 더 낮은 곳으로 내려갈때
					boolean flag = true;
					for (int k = 0; k < l; k++) {
						if (j + k >= n || arr[j+k][i] != current) {
							flag = false;
							break;
						}
					}
					if (!flag) {
						break;
					} else {
						j = j + l - 1;
						if(j+1<n && current < arr[j+1][i]) break;
						q.clear();
						if(j+1<n && current > arr[j+1][i])
							q.offer(arr[j][i]);
					}
				}
				if (j == n - 1){
					road++;
				}
			}
		}

		System.out.println(road);
	}

}