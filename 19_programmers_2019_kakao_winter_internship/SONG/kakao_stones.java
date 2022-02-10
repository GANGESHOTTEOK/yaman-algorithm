class Solution {
    public int solution(int[] stones, int k) {
        int left = 0;
        int right = Integer.MAX_VALUE;
        int mid = 0;
        int count = 0; 
        boolean flag = false;             
        int answer = 0;

        // 가능한 count를 탐색하는 것으로
        while(left <= right) {
            int[] stoneA = stones.clone();
            mid = (left+right)/2;
            count= 0; // 0이 몇 개나 연속으로 나오는지
            flag = false;        
            
            for(int i = 0 ; i < stoneA.length;i++) {
                if(stoneA[i] <= mid) { // 현재 돌을 밟을 수 있는 수가 mid(건너간 수)보다 작거나 같으면
                    stoneA[i] = 0; // 그 돌의 남은 수는 0이 된다
                    count++; // 연속되는 0의 개수를 증가시킴
                    if(count == k) {
                        flag = true; // 최대 개수가 되면 flag를 세운다(못 건너감)
                        break;
                    }
                }else {
                    count = 0; // 이때 아직 밟을 수 있는 돌이 나오면 연속카운트를 0으로 되돌림
                }
            }
            if(flag) {
                right = mid -1; // 일단 불가능 했으므로 앞쪽 배열 탐색
                answer = mid;
            }else {
                left = mid +1; // 더 큰 수가 될 가능성이 있으므로 뒷쪽 배열 탐색
            }
        }
        return answer;
    }

}