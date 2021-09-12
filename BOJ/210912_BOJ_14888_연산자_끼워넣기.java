// BOJ_14888_연산자 끼워넣기
// 모든 경우의 수를 탐색하며 최대값, 최소값 찾기
// 순열로 연산자(N-1개)를 순서에 상관있게 섞은 뒤에 피연산자(N개)를 계산한 모든 결과값 탐색
// dfs+재귀 방식으로 더 빠르게 풀 수 있는 문제.

import java.io.*;
import java.util.*;
public class Main{
    static int N,maxval=Integer.MIN_VALUE,minval=Integer.MAX_VALUE;
    static int[] nums;
    static char[] selected;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		nums = new int[N];
		char[] op = new char[N-1];
		selected = new char[N-1];

		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i=0; i<N; i++){
		    nums[i] = Integer.parseInt(st.nextToken());
		}
		st = new StringTokenizer(br.readLine());
		int cnt=0;
		char[] map = {'+','-','*','/'};
		for(int i=0; i<4; i++){
		    int n = Integer.parseInt(st.nextToken());
		    for(int j=0; j<n; j++){
		        op[cnt++]=map[i];
		    }
		}
		boolean[] visited = new boolean[N-1];
		makePermutation(op, visited, 0);
		System.out.printf("%d\n%d",maxval,minval);
	}
	private static void makePermutation(char[] op, boolean[] visited, int cnt){
	    if(cnt==N-1){
	        getAnswer();
	        return;
	    }
	    for(int i=0; i<N-1; i++){
	        if(!visited[i]){
	            visited[i]=true;
	            selected[cnt]=op[i];
	            makePermutation(op,visited,cnt+1);
	            visited[i]=false;
	        }
	    }
	}
	private static void getAnswer(){
	    int tmp=nums[0];
	    for(int i=0; i<N-1; i++){
	        switch(selected[i]){
	            case '+':
	                tmp += nums[i+1];
	                break;
	            case '-':
	                tmp -= nums[i+1];
	                break;
	            case '*':
	                tmp *= nums[i+1];
	                break;
	            case '/':
	                if(tmp<0) tmp = -(-tmp/nums[i+1]);
	                else tmp /= nums[i+1];
	                break;
	        }
	    }
	    if(tmp>maxval) maxval = tmp;
	    if(tmp<minval) minval = tmp;
	}
}
