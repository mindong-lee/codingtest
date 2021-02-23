# 정렬
# 특정 기준에 따라 데이터를 순서대로 나열하는 것
# 선택 정렬, 삽입 정렬 => O(N^2)

# assignment => 복사가 아닌 포인터로 연결. 수정하면 다른 포인터에도 영향.
# shallow copy => new 포인터에 메모리 할당 후 복사
# deep copy => 이중 포인터도 메모리 할당 후 복사

# copy test
import copy

list_a=[[1,2,3],[4,5,6],[7,8,9]]

#copy case test
list_b=list_a #assignmnet just binds two list.
list_c=list_a.copy() # list에 copy 내장돼있음.
list_d=copy.deepcopy(list_a)

list_a[1]=[100,101,102]

print("Shallow Copy Test!")
print(list_a)
print(list_b)
print(list_c)
print(list_d)

list_a[1][1]=200

print("\nDeep Copy Test!")
print(list_a)
print(list_b)
print(list_c)
print(list_d)

