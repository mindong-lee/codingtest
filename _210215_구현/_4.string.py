# <문제> 문자열 재정렬: 문제 설명
# 알파벳 대문자와 숫자(0 ~ 9)로만 구성된 문자열이 입력으로 주어진다. 이때 모든 알파벳을 오름차순으로
# 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력한다
# 예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력한다

# 배울 점이 있는 코드
# 반복 가능한 객체를 for문으로 iterate할 때, 해당 객체가 변경되면, 오류는 발생시키지 않으나, 잘못된 결과가 나올 수 있다.

s=list(input())
s.sort()
count=0
for i in s:
    if not i.isalpha():
        count += int(i)
        s.pop(0)
s += str(count)

print(s)

# 답안
s=list(input())
s.sort()
count=0
result=""
for i in s:
    if i.isalpha():
        result+=i
    else:
        count+=int(i)
print(result+str(count))