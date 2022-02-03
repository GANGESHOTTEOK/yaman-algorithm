import java.util.*;

class Solution {
    public int[] solution(String s) {
        Set<String> set = new HashSet<>(); // 중복 안 되게 검사

        String[] strs = s.replace("{", " ").replace("}", " ").trim().split(" , "); // 공백,공백으로 바꿔서 집합별로만 뗀다.
        Arrays.sort(strs, (a,b)->{return a.length() - b.length();}); // 길이로 정렬함
        
        int[] answer = new int[strs.length];
        int idx = 0;
        
        for(String s1 : strs) { // 집합별로
            for(String s2 : s1.split(",")) { // 각 원소별로
                if(set.add(s2)) { // 셋에 넣으려하면 자동으로 중복이 걸러진다. 변화가 있는 경우 true 반환
                    answer[idx++] = Integer.parseInt(s2); // 변화가 있다 ==> 새 값이다
                    // 이때 위에서 정렬했으므로 자동으로 순서가 맞춰짐
                }
            }
        }
        return answer;
    }
}