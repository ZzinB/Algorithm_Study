class Solution {
    public int characterReplacement(String s, int k) {
        //현재 윈도우 내의 문자 빈도
        int[] cnt = new int[26];
        int left = 0, right = 0;
        int maxCnt = 0;
        int maxLength = 0;

        //윈도우 확장
        while (right < s.length()){
            //현재 문자빈도수 ++
            char current = s.charAt(right);
            cnt[current - 'A']++;
            //현재 윈도우에서 빈도가 가장 높은 문자의 빈도 업데이트
            maxCnt = Math.max(maxCnt, cnt[current - 'A']);

            //현재 윈도우가 유효하지 않다면?
            if (right - left + 1 - maxCnt > k){
                char leftChar = s.charAt(left);
                cnt[leftChar - 'A']--;
                //왼쪽으로 윈도우 줄이기
                left++;
            }
        //윈도우 최대 길이 업데이트
        maxLength = Math.max(maxLength, right - left + 1);
        //오른쪽으로 윈도우 확장
        right++;
        }
        return maxLength;
    }
}