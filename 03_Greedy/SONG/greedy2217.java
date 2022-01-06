package algorithmStudy;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;

public class greedy2217 {

	private static int N;
	private static ArrayList<Integer> rope = new ArrayList<Integer>();
	private static ArrayList<Integer> w = new ArrayList<Integer>();
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		N = Integer.parseInt(br.readLine());
		
		for(int i=0; i<N; i++) {
			rope.add(Integer.parseInt(br.readLine()));
		}
		Collections.sort(rope);
		
		for(int i=0; i<N; i++) {
			w.add(rope.get(i) * (N-i));
		}
		bw.write(""+Collections.max(w));
		bw.flush();
		bw.close();
	}

}
