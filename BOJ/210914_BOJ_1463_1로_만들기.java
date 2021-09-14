// 210914 BOJ 1463 1로 만들기
// bfs+backtracking 으로 풀 수 있는데
// dp로 더 빠르게 풀 수 있는 문제
// 이 풀이가 짧고 효율적인 것 같다.
// 작은 값부터 구하면서 올라오는 상향식 풀이.
import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n+1];
        for(int i=2; i<=n; i++){
            int min=arr[i-1];
            if(i%3==0)
                min = (min < arr[i/3]) ? min : arr[i/3]; 
            
            if(i%2==0)
                min = (min < arr[i/2]) ? min : arr[i/2]; 
            
            arr[i]=min+1;
        }
        System.out.println(arr[n]);
    }    
}
