import java.io.*;
import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        ArrayList<Integer> arr = new ArrayList<>();
        Arrays.sort(tangerine);
        int cnt = 0;
        
        for(int i = 0 ; i< tangerine.length ; i++){
            cnt++;
            if((i<tangerine.length-1 && tangerine[i] != tangerine[i+1]) || ( i == tangerine.length-1 && cnt > 0)){
                arr.add(cnt);
                cnt = 0;
            }
        }
        Collections.sort(arr, Collections.reverseOrder());
        
        for(int i : arr){
            answer ++;
            k -= i;
            if(k <= 0){
                break;
            }
        }
        return answer;
    }
}