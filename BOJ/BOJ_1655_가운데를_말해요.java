// BOJ 1655 가운데를 말해요.
// 못생긴 사람 중에 가장 잘생긴 사람과 잘생긴 사람 중에 가장 못생긴 사람은 같은 사람일 확률이 높다!
// 우선순위 큐 2개를 이용한다.
// minQueue는 최솟값을 뽑는(작을수록 우선순위가 높은 것)이 아니라, 작은 수들 중에 가장 큰 값을 나타낸다.
// maxQueue는 최댓값을 뽑는(클수록 우선순위가 높은 것)이 아니라, 큰 수들 중에 가장 작은 값을 나타낸다.
// 두 그룹을 확실하게 분류하기 위해서 minQueue의 root(작은 그룹의 가장 큰 값)과 maxQueue의 root(큰 그룹의 가장 작은 값)을
// 값을 삽입할 때마다 비교하고 교환해준다.

import java.io.*;
import java.util.*;
public class Main{
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N = Integer.parseInt(br.readLine());
		PriorityQueue<Integer> minQueue = new PriorityQueue<>();
		PriorityQueue<Integer> maxQueue = new PriorityQueue<>();
		
		for(int i=0; i<N; i++){
		    if(i%2==0) minQueue.offer(-Integer.parseInt(br.readLine()));
		    else maxQueue.offer(Integer.parseInt(br.readLine()));
		    
		    if(!maxQueue.isEmpty() && -minQueue.peek()>maxQueue.peek()){
		        int a = minQueue.poll();
		        int b = maxQueue.poll();
		        minQueue.offer(-b);
		        maxQueue.offer(-a);
		    }
		    
		    bw.write(-minQueue.peek()+"\n");
		}
		
		bw.flush();
	}
}
