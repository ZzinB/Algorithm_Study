class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        int left = 0;
        int right = rows * cols - 1;

        //이진탐색
        while(left <= right){
            //중간 인덱스 계산
            int mid = left + (right - left) / 2;
            //2차원 인덱스로 변환 -> 중간값
            int midValue = matrix[mid / cols][mid % cols];

            //중간값 비교
            if (midValue == target){
                return true;
            } else if (midValue < target){
                left = mid + 1;
            } else{
                right = mid - 1;
            }
        }
        return false;
    }
}