// BOJ 9370 미확인 도착지
// 기존 나의 풀이: queue에 저장하는 Info에 bool 변수를 하나 추가해서
// g-h 경로를 지나면 bool변수를 바꿔서 경로를 지났는지 안 지났는지 알 수 있다.
// 문제점 : 만약 g-h를 지나지 않은 경로와 g-h를 지났을 때 경로의 가중치가 같아서
// g-h를 지나지 않은 경로가 먼저 갱신됐다면?!
// 가중치를 홀,짝으로 구분해 경로를 지났는지 안 지났는지를 구분할 수 있는 아이디어를 배웠다.
import java.io.*;
import java.util.*;
public class Main{
    private static class Node{
        int v;
        int w;
        Node next;
        
        public Node(int v, int w, Node n){
            this.v=v;
            this.w=w;
            this.next=n;
        }
    }
    private static class Info implements Comparable<Info>{
        int v;
        int w;
        public Info(int v, int w){
            this.v=v;
            this.w=w;
        }
        public int compareTo(Info o){
            return this.w-o.w;
        }
    }
	public static void main(String[] args) throws IOException{
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		  int T = Integer.parseInt(br.readLine());
		  for(int tt=0; tt<T; tt++){
		    StringTokenizer st = new StringTokenizer(br.readLine());
		    int n = Integer.parseInt(st.nextToken());
		    int m = Integer.parseInt(st.nextToken());
		    int t = Integer.parseInt(st.nextToken());
		    st = new StringTokenizer(br.readLine());
		    int s = Integer.parseInt(st.nextToken());
		    int g = Integer.parseInt(st.nextToken());
		    int h = Integer.parseInt(st.nextToken());
		    
		    Node[] edgeList = new Node[n+1];
		    for(int i=0; i<m; i++){
		        st = new StringTokenizer(br.readLine());
		        int from = Integer.parseInt(st.nextToken());
		        int to = Integer.parseInt(st.nextToken());
		        int w = Integer.parseInt(st.nextToken());
		        if( (from==g&&to==h) || (from==h&&to==g) ){
		            edgeList[from] = new Node(to, 2*w-1, edgeList[from]);
		            edgeList[to] = new Node(from, 2*w-1, edgeList[to]);
		        } else {
		            edgeList[from] = new Node(to, 2*w, edgeList[from]);
		            edgeList[to] = new Node(from, 2*w, edgeList[to]);
		        }
		    }
		    int[] cand = new int[t];
		    for(int i=0; i<t; i++){
		        cand[i] = Integer.parseInt(br.readLine());
		    }
		    Arrays.sort(cand);
		    
		    int[] dist = new int[n+1];
		    Arrays.fill(dist,Integer.MAX_VALUE-1);
		    boolean[] visit = new boolean[n+1];
		    PriorityQueue<Info> queue = new PriorityQueue<>();
		    queue.offer(new Info(s,0));
		    dist[s]=0;
    	    while(!queue.isEmpty()){
		        Info i = queue.poll();
		        if(visit[i.v]) continue;
		        visit[i.v]=true;
		        for(Node tmp=edgeList[i.v]; tmp!=null; tmp=tmp.next){
		            if(!visit[tmp.v] && dist[i.v]+tmp.w<dist[tmp.v]){
		                dist[tmp.v] = dist[i.v]+tmp.w;
		                queue.offer(new Info(tmp.v,dist[tmp.v]));
		            }
		        }
		    }
            for(int i=0; i<t; i++){
                if(dist[cand[i]]%2==1) bw.write(cand[i]+" ");
            }
		    bw.newLine();
		}
		bw.flush();
	}
}
