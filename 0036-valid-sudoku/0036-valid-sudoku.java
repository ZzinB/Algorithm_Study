class Solution {
    public boolean isValidSudoku(char[][] board) {
        // 각 위치 정보를 저장하기 위한 HashSet
        Set<String> set = new HashSet<>();

        // 보드의 각 칸을 순회하면서 체크
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                char num = board[i][j];
                // 현재 칸이 비어있지 않을 경우에만
                if (num != '.') {
                    // 각 행, 열, 3x3 블록에 중복된 숫자가 있는지 확인
                    // 만약 중복된 숫자가 있으면 false 
                    if (!set.add(num + "row:" + i) || !set.add(num + "col:" + j) || !set.add(num + "block:" + i/3 + "-" + j/3)) {
                        return false;
                    }
                }
            }
        }
        // 중복된 숫자가 없으면 true 
        return true;
    }
}