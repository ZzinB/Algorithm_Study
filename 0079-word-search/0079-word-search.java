class Solution {
    int[][] dir = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    private boolean dfs(char[][] board, int y, int x, String word, int idx, boolean[][] visited){
        // 단어를 모두 찾았다면 true 반환
        if (idx == word.length()){
            return true;
        }

        // 방문 확인, 좌표 내 확인
        if (y < 0 || y >= board.length || x < 0 || x >= board[0].length || visited[y][x]){
            return false;
        }

        // 현재 위치의 문자가 단어와 일치하는지 확인
        if(board[y][x] == word.charAt(idx)){
            // 방문 처리
            visited[y][x] = true;
            // 상하좌우로 문자 찾기
            for (int[] d : dir){
                int newY = y + d[0];
                int newX = x + d[1];
                if (dfs(board, newY, newX, word, idx + 1, visited)) {
                    return true;
                }
            }
            // 방문 처리 초기화
            visited[y][x] = false;
        }
        return false;
    }

    public boolean exist(char[][] board, String word) {
        // 문자 그리드 탐색
        for (int i = 0; i < board.length; i++){
            for (int j = 0; j < board[0].length; j++){
                // DFS
                if (dfs(board, i, j, word, 0, new boolean[board.length][board[0].length])){
                    return true;
                }
            }
        }
        return false;
    }
}
