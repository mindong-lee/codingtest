// 2749 피보나치 수 3
// 풀이 방법 1: 행렬의 거듭제곱 이용 2: 피사노 주기
// 행렬의 거듭제곱을 이용해서 풀었는데 나는 3x3 행렬을 이용했고 개선하면 2x2 행렬로도 구할 수 있다.
// 내가 푼 방식은 배열 없이 피보나치 수를 구하는 방법에서 영감을 얻었는데
// 세 변수만 이용해서 f1=f2, f2=f3, f3=f1+f2; 하는 방식을 행렬로 표현하면
// {{0,1,0},{0,0,1},{0,1,1}} @ {f1,f2,f3} 이다.
// 따라서 위 행렬의 거듭제곱을 이용하면 답을 빠르게 구할 수 있다.
// 좀 더 연산양을 줄이려면 피보나치 점화식을 보고 {{1,1},{1,0}} 라는 배열을 떠올렸어야 했다.
// an+2 = an+1 + an               |an+2|   |1 1| |an+1|
// an+1 = an+1 + 0       =>       |an+1| = |1 0| | an |

import java.util.Scanner;
public class Main{
    static long[][] base = {{0,1,0},{0,0,1},{0,1,1}};
    static final int MOD = 1000000;
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
		long N = sc.nextLong();
		long answer = 1;
		if(N>2){
    		long[][] ret = solve(base,N-2);
    		answer = (ret[2][1]+ret[2][2])%MOD;
		}
		System.out.println(answer%MOD);
	}
	private static long[][] solve(long[][] arr, long N){
	    if(N==1)
	        return arr;
	    if(N==2){
	        long[][] ret = new long[3][3];
	        for(int i=0; i<3; i++){
	            for(int j=0; j<3; j++){
	                for(int k=0; k<3; k++){
	                    ret[i][j] += arr[i][k]*arr[k][j];
	                }
	                ret[i][j] %= MOD;
	            }
	        }
	        return ret;
	    }
	    
	    long[][] ret = solve(solve(arr, N/2),2);
	    if(N%2==0){
	        return ret;
	    } else {
	        long[][] nret = new long[3][3];
	        for(int i=0; i<3; i++){
	            for(int j=0; j<3; j++){
	                for(int k=0; k<3; k++){
	                    nret[i][j] += ret[i][k]*base[k][j];
	                }
	                nret[i][j] %= MOD;
	            }
	        }
	        return nret;
	    }
	}
}
