class Solution {
    public String largestNumber(int[] nums) {
        // 숫자 배열을 문자열 배열로 변환
        String[] strNums = new String[nums.length];
        for (int i = 0; i < nums.length; i++) {
            strNums[i] = String.valueOf(nums[i]);
        }

        Arrays.sort(strNums, new Comparator<String>() {
            @Override
            public int compare(String a, String b) {
                // a + b와 b + a를 비교하여 내림차순 정렬
                return (b + a).compareTo(a + b);
            }
        });

        // 모든 숫자가 0일 경우 0을 반환
        if (strNums[0].equals("0")) {
            return "0";
        }
        
        String answer = "";
        for(String str : strNums){
            answer += str;
        }
        return answer;

    }
}