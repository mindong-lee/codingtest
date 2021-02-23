# 코딩 테스트 준비할 때 알아두면 유용한, 자주 사용되는 내장 함수, 라이브러리 
# 1. SUM, MIN, MAX, EVAL

eval("(3+5)*9") # 수식 계산

# 2. sorted

# 3. permutation(순열), combination(조합)
from itertools import permutations

data= ['A','B','C']

result = list(permutations(data,3))
print(result)
result = list(permutations(data,2))
print(result)
result = list(permutations(data,1))
print(result)

from itertools import combinations

result = list(combinations(data,3))
print(result)
result = list(combinations(data,2))
print(result)
result = list(combinations(data,1))
print(result)

# 4. product(중복 순열), combinations with replacement(중복 조합)
from itertools import product

result=list(product(data,repeat=3))
print(result)
result=list(product(data,repeat=2))
print(result)
result=list(product(data,repeat=1))
print(result)

from itertools import combinations_with_replacement

result=list(combinations_with_replacement(data,3))
print(result)
result=list(combinations_with_replacement(data,2))
print(result)
result=list(combinations_with_replacement(data,1))
print(result)

#5. Counter, 반복 가능한 객체 안에서 등장 횟수를 세는 기능

from collections import Counter

counter = Counter([1,2,3,4,1,2,3,1,2,3,1,2,3,1,21,2,3,1,2,3,1,3,2,1])
print(counter)
print(counter[1])

import math
def lcm(a,b):
    return a*b //math.gcd(a,b)
a=21
b=14
print(math.gcd(21,14)) #최대 공약수
print(lcm(21,14)) #최소 공배수 