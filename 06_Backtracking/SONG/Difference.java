package algorithmWeek2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Difference {
    static int N;
    static int[] array, numbers;
    static boolean[] checked;
    static int max = Integer.MIN_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        array = new int[N];
        numbers = new int[N];
        checked = new boolean[N];
        for (int i = 0; i < N; i++) {
            array[i] = Integer.parseInt(st.nextToken());
        }

        permutation(0);
        System.out.println(max);
    }

    static void permutation(int count) {
        if(count == N) {
            max = Math.max(max, cal());
            return;
        }

        for (int i = 0; i < N; i++) {
            if(checked[i]) continue;
            numbers[count] = array[i];
            checked[i] = true;
            permutation(count + 1);
            checked[i] = false;
        }
    }

    private static int cal() {
        int sum = 0;
        for (int i = 0; i < N - 1; i++) {
            sum += Math.abs(numbers[i] - numbers[i + 1]);
        }
        return sum;
    }
}