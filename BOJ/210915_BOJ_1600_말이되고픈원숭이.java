// BOJ 1600 말이 되고픈 원숭이
// 1. 입력이 열,행 순으로 들어옴.(하..)
// 2. 행==1, 열==1 인 경계값 처리해야 함.
// 3. 기존의 BFS 최단 경로 문제와 다른 점은 이미 방문한 지점을 재방문 할 수 있다. k를 사용한 횟수가 다르기 때문.
// 4. 핵심은 3차원 visit 배열로 k의 횟수에 따라 방문 기록을 남길 수 있게 해야함.

import java.io.*;
import java.util.*;
public class Main{
    static int[][] dir = {{-1,0},{1,0},{0,1},{0,-1}};
    static int[][] hdir = {{-2,-1},{-1,-2},{-2,1},{-1,2},{1,-2},{2,-1},{1,2},{2,1}};
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int k = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		int col = Integer.parseInt(st.nextToken());
		int row = Integer.parseInt(st.nextToken());
		if(row==1 && col==1){
		    System.out.print(0);
		    return;
		}
		int[][] arr = new int[row][col];
	    boolean[][][] visit = new boolean[row][col][k+1];
	    
		for(int i=0; i<row; i++){
		    st = new StringTokenizer(br.readLine());
		    for(int j=0; j<col; j++){
		        arr[i][j] = -Integer.parseInt(st.nextToken());
		    }
		}
		
		Queue<Info> queue = new LinkedList<>();
		queue.offer(new Info(0,0,k));
		
    	while(!queue.isEmpty()){
		    Info v = queue.poll();
		    if(v.r==row-1 && v.c==col-1) break;
		    if(v.k>0){
		        for(int i=0; i<8; i++){
		            int nr = v.r+hdir[i][0];
		            int nc = v.c+hdir[i][1];
		            if(0<=nr && nr<row && 0<=nc && nc<col && arr[nr][nc]!=-1 && !visit[nr][nc][v.k-1]){
		                arr[nr][nc]=arr[v.r][v.c]+1;
		                visit[nr][nc][v.k-1]=true;
		                queue.offer(new Info(nr,nc,v.k-1));
		            }
		        }
		    }
		    for(int i=0; i<4; i++){
		        int nr = v.r+dir[i][0];
		        int nc = v.c+dir[i][1];
                if(0<=nr && nr<row && 0<=nc && nc<col && arr[nr][nc]!=-1 && !visit[nr][nc][v.k]){
                    arr[nr][nc]=arr[v.r][v.c]+1;
                    visit[nr][nc][v.k]=true;
                    queue.offer(new Info(nr,nc,v.k));
		        }
		    }
		}
		System.out.print((arr[row-1][col-1]==0) ? -1 : arr[row-1][col-1]);
	}
}
class Info{
    int r;
    int c;
    int k;
    public Info(int r, int c, int k){
        this.r=r;
        this.c=c;
        this.k=k;
    }
}
