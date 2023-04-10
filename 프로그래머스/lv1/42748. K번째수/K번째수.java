import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int [commands.length];
        int[] tmp;
        for(int a = 0 ; a<commands.length ; a++){
            int i = commands[a][0];
            int j = commands[a][1];
            int k = commands[a][2];
            tmp = new int [(j-i)+1];
        
            int s = i;
            for(int f = 0 ; f<tmp.length ; f++){
                tmp[f] = array[s-1];
                s++;
            }
            Arrays.sort(tmp);
            answer[a] = tmp[k-1];
        }
        return answer;
    }
}