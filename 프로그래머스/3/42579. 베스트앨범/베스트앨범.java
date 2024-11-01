import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        // 반례 = [4, 3]
        // genres = new String[]{"classic", "classic", "classic", "classic", "classic"};
        // plays = new int[]{500, 600, 150, 800, 2500};
        
        
        // 키: 장르, 값: 장르에 속한 곡의 재생수의 합
        HashMap<String, Integer> genresMap = new HashMap();
        for (int i = 0; i < genres.length; i++) {
            if (genresMap.containsKey(genres[i])) {
                genresMap.put(genres[i], genresMap.get(genres[i]) + plays[i]);
            } else {
                genresMap.put(genres[i], plays[i]);
            }
        }
        // printMap(genresMap);
        
        
        // 값으로 장르 순서 내림차순하기
        List<String> genresList = new ArrayList<>(genresMap.keySet());
        genresList.sort((key1, key2) -> 
                        genresMap.get(key2).compareTo(genresMap.get(key1)));
        // System.out.println(genresList);
        
        
        List<Integer> answerList = new ArrayList<>(); // 정답 인덱스 저장
        
        for (int i = 0; i < genresList.size(); i++) {
            // 키: 곡 인덱스, 값: 곡 재생 수
            HashMap<Integer, Integer> playsMap = new HashMap<>();
            for (int j = 0; j < genres.length; j++) {
                if (genres[j].equals(genresList.get(i))) {
                    playsMap.put(j, plays[j]);
                }
            }
            // printMap(playsMap);
            
            // 재생 수 대로 내림차순 하기
            List<Integer> playsList = new ArrayList<>(playsMap.keySet());
            playsList.sort((key1, key2) ->
                          playsMap.get(key2).compareTo(playsMap.get(key1)));
            // System.out.println(playsList);
            
            
            // 2개씩 재생 수 많은 곡의 인덱스 출력하기
            answerList.add(playsList.get(0));
            if (playsList.size() > 1) {
                answerList.add(playsList.get(1));
            }
        }
        
        System.out.println(answerList);
        return answerList.stream().mapToInt(i -> i).toArray(); // List -> array 변환
    }
    
    public static <K, V> void printMap(HashMap<K, V> map) {
        for (K key : map.keySet()) {
            System.out.println("Genre: " + key + ", Count: " + map.get(key));
        }
    }
    
}