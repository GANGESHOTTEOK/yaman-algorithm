package algorithmWeek2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ2529 {
	static int N;
	static boolean[] arr;
	static boolean[] checked;
	static int[] answer;
	static long max = Long.MIN_VALUE;
	static long min = Long.MAX_VALUE;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		arr = new boolean[N]; // 부등호
		checked = new boolean[10]; // 0~9
		answer = new int[N+1]; // 부등호 개수+1
			
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		for(int i=0; i<N; i++) {
			if(st.nextToken().equals(">")) arr[i] = true;
			else arr[i] = false;
		}
		
		permutation(0);
		
		/* output */
		String maxNum = Long.toString(max);
		String minNum = Long.toString(min);
		if(maxNum.length() == N) maxNum = "0" + maxNum;
		if(minNum.length() == N) minNum = "0" + minNum;
		
		System.out.println(maxNum);
		System.out.println(minNum);
	}
	
	static void permutation(int count) {
		if(count > 1) { 
			if(arr[count-2] == true) { // >
				if(answer[count-2] < answer[count-1]) return;
			}
			else {
				if(answer[count-2] > answer[count-1]) return;
			}
		}
			
        if(count == N+1) { //부등호보다 숫자가 1개 더 많음
        	long num = 0;
        	for(int n : answer) { // 숫자만들기
        		num += n;
        		num *= 10;
        	}
        	num /= 10; // 마지막에 곱해진거 원위치
        	
        	if(num > max) max = num;
        	if(num < min) min = num;
        	
        	return;
        }

        for (int i = 0; i < 10; i++) {
            if(checked[i]) continue;
            answer[count] = i;
            checked[i] = true;
            permutation(count + 1);
            checked[i] = false;
        }
    }
}
