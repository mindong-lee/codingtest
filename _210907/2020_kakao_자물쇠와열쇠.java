import java.util.*;
class Solution {
    static int N,M,zeroCnt;
    public boolean solution(int[][] key, int[][] lock) {
        boolean answer = false;
        N = lock.length;
        M = key.length;
        //0. 이미 홈이 없는 경우 체크
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                if(lock[i][j]==0) zeroCnt++;
            }
        }
        if(zeroCnt==0) return true;
        int[][] tmp;
        int[][] arr = new int[3*M][3*M];
        for(int i=M; i<2*M; i++){
            for(int j=M; j<2*M; j++){
                arr[i][j] = key[i-M][j-M];
            }
        }
        //1.열쇠를 만든다.
outer:  for(int i=0; i<2*M; i++){
            for(int j=0; j<2*M; j++){
                tmp = makeKey(arr,i,j);
                //2.열쇠를 회전시키면서 자물쇠와 맞춰본다.
                for(int k=0; k<4; k++){
                    tmp = rotateKey(tmp);
                    //3. true를 return 하면 멈춘다.
                    if(isFilled(tmp, lock)){
                        answer=true;
                        break outer;
                    }
                }
            }
        }
        return answer;
    }
    private static int[][] makeKey(int[][] key, int r, int c){
        int[][] ret = new int[M][M];
        for(int i=r; i<r+M; i++){
            for(int j=c; j<c+M; j++){
                ret[i-r][j-c]=key[i][j];
            }
        }
        return ret;
    }
    private static boolean isFilled(int[][] key, int[][] lock){
        for(int i=0; i<=N-M; i++){
            for(int j=0; j<=N-M; j++){
                int cnt = 0;
outer:          for(int k=0; k<M; k++){
                    for(int l=0; l<M; l++){
                        if((key[k][l]==1) && (lock[i+k][j+l]==1)) break outer;
                        if((key[k][l]==1) && (lock[i+k][j+l]==0)) cnt++;
                    }
                }
                if(cnt==zeroCnt) return true;
            }
        }
        return false;
    }
    private static int[][] rotateKey(int[][] key){
        int[][] ret = new int[M][M];
        for(int i=0; i<M; i++){
            for(int j=0; j<M; j++){
                ret[i][j] = key[M-1-j][i];
            }
        }
        return ret;
    }
}
