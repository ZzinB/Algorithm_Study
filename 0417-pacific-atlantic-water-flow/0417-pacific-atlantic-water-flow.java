class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        List<List<Integer>> result = new ArrayList<>();
        //예외 처리
        if (heights == null || heights.length == 0 || heights[0].length == 0) {
            return result;
        }
        
        int m = heights.length;
        int n = heights[0].length;
        boolean[][] pacific = new boolean[m][n];
        boolean[][] atlantic = new boolean[m][n];
        
        // 태평양과 대서양에서 각각 DFS를 수행하여 접근 가능한 셀
        for (int i = 0; i < m; i++) {
            dfs(heights, pacific, i, 0); // 왼쪽 열에서 시작하는 태평양 DFS
            dfs(heights, atlantic, i, n - 1); // 오른쪽 열에서 시작하는 대서양 DFS
        }
        
        for (int j = 0; j < n; j++) {
            dfs(heights, pacific, 0, j); // 위쪽 행에서 시작하는 태평양 DFS
            dfs(heights, atlantic, m - 1, j); // 아래쪽 행에서 시작하는 대서양 DFS
        }
        
        // 두 바다로 모두 흐를 수 있는 셀
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (pacific[i][j] && atlantic[i][j]) {
                    List<Integer> cell = new ArrayList<>();
                    cell.add(i);
                    cell.add(j);
                    result.add(cell);
                }
            }
        }
        
        return result;
    }

    private void dfs(int[][] heights, boolean[][] reachable, int r, int c) {
        reachable[r][c] = true;
        int m = heights.length;
        int n = heights[0].length;
        
        // 상하좌우
        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};
        
        for (int i = 0; i < 4; i++) {
            int nr = r + dr[i];
            int nc = c + dc[i];
            
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && !reachable[nr][nc] && heights[nr][nc] >= heights[r][c]) {
                dfs(heights, reachable, nr, nc);
            }
        }
    }
}