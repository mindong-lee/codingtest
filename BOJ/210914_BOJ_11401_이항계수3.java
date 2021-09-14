// n이 10000을 넘어가면, 동적계획법을 이용해서 이항 계수 구하기(시간복잡도 O(nk))가 힘들다.
// 왜냐하면 2차원 memoization table을 만드는데 메모리를 많이 사용하기 때문이다.
// 그렇다면 n 범위가 400만인 이 문제는 어떻게 접근해야할까?
// 문제를 푸는 데 필요한 키워드는 1. 모듈러 연산 성질 2. 페르마의 소정리 3. 분할정복을 이용한 행렬의 거듭제곱이다.
// 1. A*B mod C = ((A mod C) * (B mod C)) mod C 의 분배법칙이 성립한다.
//    A+B mod C = ((A mod C) + (B mod C)) mod C 의 분배법칙이 성립한다.
//    A*B mod C = ((A mod C) - (B mod C)) mod C 의 분배법칙이 성립한다.
// 2. 페르마 소정리에 의해 소수 p에 대해서 a^p ≡ a (mod p) 가 성립한다.
//    a^(p-1)≡1 (mod p)
//    a*a^(p-2)≡1 (mod p)
//    따라서 a^(p-2)는 모듈로 연산에 대한 a의 역원이 된다.
// 3. 만약 C가 p라면, nCk mod C = n!/((n-k)!*k!) mod C = n!*((n-k)!)^(C-2)*(k!)^(C-2) 가 성립한다.
//    문제에서 1000000007은 소수이므로 위의 식을 이용해서 풀 수 있다.

import java.util.Scanner;
public class Main{
    static final int MOD = (int)1e9+7;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int k = sc.nextInt();
		long[] facto = new long[n+1];
		facto[0]=1;
		facto[1]=1;
		for(int i=2; i<=n; i++) facto[i]=(facto[i-1]*i)%MOD;
		long inv = pow((facto[k]*facto[n-k])%MOD,MOD-2);
		long answer = (facto[n]*inv)%MOD;
		System.out.println(answer);
	}
	private static long pow(long a, int b){
	    if(b==1) return a;
	    if(b==2) return (a*a)%MOD;
	    
	    long ret = pow(a, b/2);
	    if(b%2==0) return (ret*ret)%MOD;
	    else return ((ret*ret)%MOD*a)%MOD;
	}
}
