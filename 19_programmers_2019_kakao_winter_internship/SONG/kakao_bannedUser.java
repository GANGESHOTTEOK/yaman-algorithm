import java.util.ArrayList;
import java.util.HashSet;
import java.util.regex.Pattern;

class Solution {
    HashSet<HashSet<String>> result;
    ArrayList<ArrayList<String>> banList;
    public int solution(String[] user_id, String[] banned_id) {
        result = new HashSet<HashSet<String>>(); // 불량 사용자들. 중복X니까 셋으로
        banList = new ArrayList<ArrayList<String>>(); // 불량 사용자 아이디 목록
        
        for(String id : banned_id) { // 각각의 불량 목록이랑 매치되는 아이디 모두 찾기
            banList.add(check(id, user_id));
        }
        
        dfs(new HashSet<String>(), 0);
        int answer = result.size(); // 경우의 수의 개수 반환
        return answer;
    }
    
    ArrayList<String> check(String id, String[] user_id) { // 정규표현식으로 체크
        String pattern = id.replace('*', '.'); // 문자 하나라는 의미의 .으로 바꿈
        
        ArrayList<String> list = new ArrayList<>(); // 매치 되는 아이디를 모아서 넘길 배열
        
        for(String user : user_id) {
            boolean isMatch = Pattern.matches(pattern, user); // 자바 메소드! 유용!
            if(isMatch) list.add(user);
        }
        return list;
    }
    
    void dfs(HashSet<String> add, int d) { // dfs로 모든 경우의 수를 탐색
        if(d == banList.size()) { // 깊이가 불량 목록이랑 같아지면 사용자 조합 한 가지 완성
            result.add(new HashSet<>(add)); // 조합을 결과리스트에 추가함
            return;
        }
        
        for(String user : banList.get(d)) {
            if(!add.contains(user)) { // user 셋에 포함이 안 되어 있으면
                add.add(user);
                dfs(add, d+1);
                add.remove(user);
            }
        }
    }
    
}