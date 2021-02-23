# 계수 정렬
# 저장된 데이터가 양의 정수이고, 범위가 제한된다면 빠르게 동작하는 알고리즘.
# 음의 정수도 표현할 순 있음

def CountingSort(array):
    arrlen = max(array)+1 # 0과 최대값 사이 정수 개수
    CountArr = [0]*(arrlen)
    for i in array:
        CountArr[i] += 1
    for idx,count in enumerate(CountArr):
        for j in range(count):
            print(idx, end= " ")

CountingSort([1,2,3,1,0,2,2,3,9,3,2,0,3,2,5,7,0])