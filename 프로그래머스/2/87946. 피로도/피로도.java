class Solution {
    static boolean[] visited;
    static int cnt = 0;
    
    public int solution(int k, int[][] dungeons) {
        visited = new boolean[dungeons.length];
        dfs(0, k, dungeons);
        return cnt;
    }
    
    private void dfs(int depth, int k, int[][] dungeons){
        //종료조건 X : 던전 길이 만큼 반복!!!
        for(int i=0 ; i<dungeons.length ; i++){
        //1. 던전 방문 체크 
            // 방문했다면? 다음 노드로
            if (visited[i] || k < dungeons[i][0]){
                continue;
            }
        //2. 현재 피로도와 필요 피로도를 비교하여 탐험가능한 던전인지 판단
            // 방문한 적이 없고, 현재 피로도 < 필요 피로도이면? 점화식
                //2-1. 방문 처리
            visited[i] = true;
                //2-2. depth +1, 현재 피로도 - 해당 던전 피로도 -> 다음 던전
            dfs(depth+1, k - dungeons[i][1], dungeons);
                //2-3. 방문 처리 취소 
            visited[i] = false;
        }
        cnt = Math.max(cnt, depth);
    }
}