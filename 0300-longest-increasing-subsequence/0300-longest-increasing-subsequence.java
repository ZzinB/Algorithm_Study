class Solution {
    public int lengthOfLIS(int[] nums) {
        //dp 생성
        int[] dp = new int[nums.length];
        Arrays.fill(dp, 1);
        int result = 1;

        //현재 요소
        for (int i=1 ; i<nums.length ; i++){
            for (int j=0 ; j<i ; j++){
                //num[i]가 num[j]보다 크면, dp[i] 갱신
                if (nums[i] > nums[j]){
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
            result = Math.max(result, dp[i]);
        }
        return result;
    }
}