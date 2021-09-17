// DFS+BackTracking을 이용하는 접근 방법은 빠르게 알았는데
// 구현하는 데 있어서 어려운 점이 많았다.
// 1. 전선이 겹치는 구간을 체크하려면 배열에 기록을 해야하는데 dfs를 마치고나서 다시 배열을 초기화하는 과정.
// 2. 재귀의 기저조건 설정

import java.io.*;
import java.util.*;
public class Solution{
    static int[][] dir = { {1,0},{-1,0},{0,1},{0,-1} };
    static int N,ans,anslen;
    static int[][] arr;
    static List<Pos> core;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T = Integer.parseInt(br.readLine());
        arr = new int[12][12];
        for(int t=1; t<=T; t++){
            N = Integer.parseInt(br.readLine());
            core = new ArrayList<>();
            for(int i=0; i<N; i++){
                StringTokenizer st = new StringTokenizer(br.readLine());
                for(int j=0; j<N; j++){
                    arr[i][j] = Integer.parseInt(st.nextToken());
                    if(arr[i][j]==1 && i!=0 && i!=N-1 && j!=0 && j!=N-1) core.add(new Pos(i,j));
                }
            }
            ans=0;
            anslen=123456789;
            dfs(0,0,0);
            System.out.printf("#%d %d\n", t, anslen);
        }
    }
 
    private static void dfs(int cnt, int selected, int len){
        if(cnt == core.size()){
            if(selected > ans){
                ans = selected;
                anslen = len;
            } else if( selected == ans ){
                anslen = Math.min(anslen, len);
            }
            return;
        }
         
        for(int i=0; i<4; i++){
            List<Pos> tmp = new ArrayList<>();
             
            boolean flag = false;
            int nr = core.get(cnt).r;
            int nc = core.get(cnt).c;
             
            while(true){
                if(nr==0 || nc==0 || nr==N-1 || nc==N-1){
                    flag=true;
                    break;
                }
                nr += dir[i][0];
                nc += dir[i][1];
                if(arr[nr][nc]==0){
                    tmp.add(new Pos(nr,nc));
                } else {
                    break;
                }
            }
            if(flag){
                for(int j=0; j<tmp.size(); j++){
                    arr[tmp.get(j).r][tmp.get(j).c] = 2;
                }
                dfs(cnt+1, selected+1, len+tmp.size());
                for(int j=0; j<tmp.size(); j++){
                    arr[tmp.get(j).r][tmp.get(j).c] = 0;
                }
            }
        }
        dfs(cnt+1, selected, len);
    }
}
class Pos{
    int r;
    int c;
    public Pos(int r, int c){
        this.r=r;
        this.c=c;
    }
}
