# 그리디 2번
#
# <문제> 1이 될 때까지:
# 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다
# 단, 두번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다

# N에서 1을 뺀다
# N을 K로 나눈다
# 예를 들어 N이 17, K가 4라고 가정하면. 이때 1번의 과정을 한 번 수행하면 N은 16이 된다.
# 이 후에 2번의 과정을 두 번 수행하면 N은 1이 된다. 결과적으로 이 경우 전체 과정을 실행한 횟수는 3이 된다
# 이는 N을 1로 만드는 최소 횟수이다.

# N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는
# 프로그램을 작성하라
#
# <문제> 1이 될 때까지: 정당성 분석
#
# 가능하면 최대한 많이 나누는 작업이 최적의 해를 항상 보장할 수 있을까?
# N이 아무리 큰 수여도 K로 계속 나눈다면 기하급수적으로 빠르게 줄일 수 있다
# 다시 말해 K가 2이상이기만 하면 K로 나누는 것이 1을 빼는 것 보다 항상 빠르게 N을 줄일 수 있다
# 또한 N은 항상 1에 도달하게 된다 (최적의 해 성립)

n, k = map(int,input().split())
count=0
while n != 1:
    if n%k==0:
        n //= k
    else:
        n -= 1
    count+=1
print(count)