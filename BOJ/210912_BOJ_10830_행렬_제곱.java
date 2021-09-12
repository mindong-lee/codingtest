// BOJ 10830 행렬 제곱

// 정수 또는 행렬의 거듭제곱은 일반적인 방법으로 O(N)의 시간복잡도를 갖는다. (행렬 곱 연산은 고려하지 않았을 때)
// 만약 시간 제한 1초, 1e9 이상의 거듭제곱을 구하는 문제가 나온다면 TLE가 발생한다.
// 이를 분할정복 기법으로 효율적으로 개선하는 방법이 있다.
// A^8의 연산은 A*A*A*A*A*A*A*A = A^2*A^2*A^2*A^2 = A^4*A^4 = A^8 의 과정을 거쳐 연산이 진행된다.
// 만약 우리가 A^2의 연산을 미리 구한다면 A^2을 4번 연산하면 A^8이 되고
// 만약 우리가 A^4의 연산을 미리 구한다면 A^4을 2번 연산하면 A^8이 된다.
// 그럼 만약 A^9의 연산을 구한다면? A^8을 분할정복으로 빠르게 구한 후에 A만 곱해주면 된다.
// 위와 같은 방법으로 O(logN)의 시간복잡도로 문제를 해결할 수 있다.

import java.io.*;
import java.util.*;
public class Main{
    static int[][] base;
    static int N;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		long B = Long.parseLong(st.nextToken());
		
		base = new int[N][N];
		for(int i=0; i<N; i++){
		    st = new StringTokenizer(br.readLine());
		    for(int j=0; j<N; j++){
		        base[i][j]=Integer.parseInt(st.nextToken());
		    }
		}
		int[][] ret;
		ret = solve(base,B);
		for(int i=0; i<N; i++){
		    for(int j=0; j<N; j++){
		        bw.write(ret[i][j]+" ");
		    }
		    bw.newLine();
		}
		bw.flush();
	}
	private static int[][] solve(int[][] arr, long B){
	    int[][] ret;
	    if(B==1){
	        ret = new int[N][N];
	        for(int i=0; i<N; i++){
	            for(int j=0; j<N; j++){
	                ret[i][j]=arr[i][j]%1000;
	            }
	        }
	        return ret;
	    };
	    if(B==2){
	        ret = new int[N][N];
	        for(int i=0; i<N; i++){
	            for(int j=0; j<N; j++){
	                for(int k=0; k<N; k++){
	                    ret[i][j]+=arr[i][k]*arr[k][j];
	                }
	                ret[i][j]%=1000;
	            }
	        }
	        return ret;
	    }
	    ret = solve(solve(arr, B/2),2);
	    if(B%2==0){
	        return ret;
	    } else {
	        int[][] nret = new int[N][N];
	        for(int i=0; i<N; i++){
	            for(int j=0; j<N; j++){
	                for(int k=0; k<N; k++){
	                    nret[i][j]+=ret[i][k]*base[k][j];
	                }
	                nret[i][j]%=1000;
	            }
	        }
	        return nret;
	    }
	}
}
