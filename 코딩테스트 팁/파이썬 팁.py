# 시간제한 1초일때
# N <= 500 O(N3) 알고리즘 가능
# N <= 2000 O(N2) 알고리즘 가능
# N <= 100000 O(NlogN) 알고리즘 가능
# N <= 10000000 O(N) 알고리즘 가능


# 리스트 컴프리헨션 좋은 예
# 이차원 배열 선언
# array = [[0] * m for _ in range(n)] #여기서 _는 단순 반복을 위해 사용
# 조건문 포함 선언
# array = [i for i in tmp if i not in remove_set]

# 이차원 배열 잘된 예!!!!!!
# n = 3
# m = 4
# arr = [[0] * m for _ in range(n)]

# 이차원 배열 잘못된 예!!!!!!
# * n 에서 얕은 복사가 된다. 이렇게 쓰면 절대 안됨 위에꺼 대로 써야함.
# n = 3
# m = 4
# arr = [[0] * m] * n

# list 주요함수
# array.reverse() -> 정렬과 상관없이 현재값들을 그냥 뒤집기만 함.
# array.count(특정값) : 특정값 갯수
# array.remove(특정값) : 특정값 여러개 중 하나만 지움
# array.insert(삽입할 위치 인덱스, 삽입할 값) -> array.insert(0, 100)
# array.append(값)

# 두 리스트 요소 간 합하기
# 두 리스트를 동시에 해서 뭘 하고 싶을때는 zip함수를 쓰면 엄청 유용하다!!
# a=[1,2,3]
# b=[4,5,6]
# c= [i+j for i,j in zip(a,b)]
# print(c) #[5, 7, 9]


# find indexAll 에 대한 람다함수 filter 이용
# a = [1, 2, 3, 4, 1, 1, 2]
# print(a.index(1)) # 0
# all_a_index = list(filter(lambda x: a[x] == 1, range(len(a))))
# print(all_a_index) # [0, 4, 5]


# 무한을 의미하는 값으로 10억을 설정
# INF = int(1e9)
# ex)
# 1e9 = 1*109 = 1000000000,
# 2e9 = 2*109 = 2000000000


# 유용한 표준 라이브러리
# itertools : 순열 조합
# data = ['A', 'B', 'C']
# from itertools import permutations #순열
# list(permutations(data, 뽑을 수))
# from itertools import combinations #조합
# list(combinations(data, 뽑을 수))
# from itertools import product #중복 순열
# list(product(data, repeat=뽑을 수))
# from itertools import combinations_with_replacement #중복 조합
# list(combinations_with_replacement(data, 뽑을 수))

# heapq : 힙, 우선순위 큐
# import heapq

# bisect : 이진 탐색
# from bisect import bisect_left, bisect_right

# 스택(선입후출)은 리스트 그냥 사용
# stack = []
# stack.append()
# stack.pop()

# collections : 덱(deque), 스텍, 카운터(Counter)
# from collections import deque

# 큐(선입선출)은 deque 라이브러리 사용
# from collections import deque
# queue = deque()
# 오른쪽으로 들어가서 왼쪽으로 나간다고 생각해야함(선입선출)
# queue.append()
# queue.popleft()
# queue.reverse() 가능

# 카운터(Counter) 사용법
# from collections import Counter
# counter = Counter(['a', 'a', 'b', 'c', 'c'])
# counter['a'] -> 2 #카운터 객체에 값에 해당하는 게 몇 개 있는 지 수를 세줌
# counter['b'] -> 1
# dict(counter) -> {'a': 2. 'b': 1, 'c':2} #dict로 변환하면 사전형태로 정보를 변환해줌
# dict같이 편하게 변환할 수 있기 때문에 Counter라이브러리 써서
# 워드클라우드 같은 기능을 만들 때 유용하게 사용할 수 있음
# 카운터 객체는 set처럼 빼기가 가능하다
# 따라서 차집합 문제에 오히려 set보다 편하게 적용 가능 set은 중복을 제거해버려서 문제
# 완주하지못한선수 복습.py 파일으로 확인할 것

# math: 팩토리얼, 최대공약수(GCD), 삼각함수, 파이 제곱근
# import math
# math.gcd(21, 14) 21과 14의 최대공약수 구하기


# lambda함수 사용법
# 형태: lambda 파라미터들: 함수내용
# 즉시 실행 방법
# (lambda 파라미터들: 함수내용)(인자)
# ex) (lambda a, b: a+b)(3,7)
# -> 10
# ex) print( (lambda a, b: a+b)(3,7) )

# lambda함수를 map함수를 사용해서 효과적으로 사용하는 방법
# list1 = [1,2,3,4,5]
# list2 = [6,7,8,9,10]

# map(람다함수, 리스트1, 리스트2)
# result = map(lambda a, b: a + b, list1, list2)
# list(result) #패킹된 상태기 떄문에 list로 변환해줘야함
# 결과 : [7,9,11,13,15]


# sort 함수 사용법
# list형태의 변수
# reverse 내림차순
# array.sort(reverse = True) #단 array변수 자체가 정렬되어 바뀜

# sorted함수 # 정렬된 새로운 값을 return 기존 array는 정렬 바뀌지 않음
# array = [('a',1), ('b',2), ('c',3)]
# new_array = sorted(array, key = lambda: x: x[1], reverse = True)
# key 옵션에서 lambda함수는 위의 튜플에서 두번째값인 1인덱스 값을 기준으로 정렬을 한다는 뜻
# reverse 내림차순 옵션도 사용가능


# 전역변수를 사용하는 방법
# 위에서 선언한 전역변수명을 지역 scope에서 global로 지정해줘야함
# a = 0
# def func():
#     global a
#     a += 1

# 중첩함수(nested function) 내에서 비지역변수(=전역변수)를 사용하는 방법
# 프로그래머스에서 유용하게 쓰일 듯 왜냐면 solution함수 안에서 작성해야 하기 때문
# def solution():
#     num = 0

#     def change_num():
#         nonlocal num
#         num = 100
#         print(num)

#     change_num() #이때 비지역변수 num이 100이 됨

#     print(num)

# solution() 결과
# 100
# 100


# 여러개의 변수가 한번에 반환되는 걸 패킹이라고 하고
# 그 return 값을 각 변수로 받는 것을 언패킹이라고 함
# def func()
#     a += 1
#     b += 1
#     c += 1
#     d += 1
#     return a, b, c, d #패킹
# e, r, t, t = func() # 언패킹


# 주의사항 continue는 아래꺼는 수행 안하고 다음 for문으로 넘어가는 거임
# for i in array:
#     if i == 0:
#         continue
#     print(i)
# 이때 i가 0이면 print하지 않고 다음 i=1일때의 for문으로 넘어가는 거(주의해야함)
# break는 for문이 끝나는 거고 continue는 for문 다음 for문 계속 진행


# if else 한줄 쓰기(삼항연산자 같은 거)
# 참일때 값 if 참인조건 else 거짓일때 값
# "asdf" if 300 > 200 else "Fail"


# python에서 부정(! 아님)
# not X


# 리스트에 있는 지 없는 지 조건
# if x not in (문자열 or array)
# if x in (문자열 or array)


# 조건에 그냥 아무것도 넣고 싶지 않을때(pass)
# if a > 200:
#     pass
# else:
#     print('a')


# print문 활용법
# print()는 기본적으로 한번쓰고 다음엔 enter가 들어감
# print('a')
# print('b')
# 결과:
# a
# b


# 공백 기준으로 연달아 출력하고 싶을때
# print(a, b) -> a b
# or
# print(a, end = " ")
# print(b, end = " ")
# print("안녕하세요")
# 결과: a b 안녕하세요
# 이 때 마지막에 end 옵션을 안해야 뒤에 공백이 안생김


# 자바스크립트에 백틱(``) 문법과 비슷한 방법
# f string 방법
# 형태 : f"글자들 {변수값} 형태"
# answer = 7
# print( f"정답은 {answer}입니다.")
# 결과: 정답은 7입니다.


# \ 사용 시 큰따옴표 작은따옴표 상관없이 사용 가능
# ex) "don't you know \"python\"?"
# 문자열 더하기 곱하기('a' * 3), 슬라이싱(a[2:4])은 가능하나 인덱스의 값을 바꿀수는 없음 text[2] = 'a'


# 튜플 괄호형
# tuple = (1,2,3,4,5)


# 사전 자료형 선언
# a = dict() or a = {key:value,}


# 집합(set) 자료형 초기화 방법
# data = {1,2,3,4}
# or
# data = set([])
# or
# data = set([1,1,2,2,3,4]) 중복있는 array를 넣으면 중복 제거된 {1,2,3,4}만 남음
# 기본 구조는 {1,2,3,4} 같은 json에서 key value가 아닌 value값만 있는 형태
# data = set([1,1,2,2,3,4]) -> {1,2,3,4} # 안에 array를 넣으면 중복제거 된 set 자료형
# data = {1,1,2,2,3,4} -> {1,2,3,4} # 값을 중복해서 넣어도 결과는 중복제거
# set 자료형
# 합집합: a | b
# 교집합: a & b
# 차집합: a - b
# 원소 추가: a.add(4)
# 여러개 추가: a.update([5,6])
# 특정 값 제거: a.remove(값)


# ord() = 문자 -> 숫자
# chr() = 숫자 -> 문자


# array 문자열로 조인
# '구분자'.join(리스트)
# ex) ''.join(['a', 'b', 'c']) -> abc


# 알파벳인지 확인 .isalpha()
# "z".isalpha()


# !!! 단순 reverse == 뒤집기임!! sort 정렬 아님!!!
# array 또는 스택 뒤집기
# 1. 슬라이싱방법
# a[start : end : step]
# >>> a = ['a', 'b', 'c', 'd', 'e']
# # 전체를 거꾸로 가져옵니다.
# >>> a[::-1]
# ['e', 'd', 'c', 'b', 'a']

# 2. num_list.reverse() 메모리사용량이 더 작음 <--- 추천


# 파이썬 빠른 input함수 선언
# import sys
# input = lambda: sys.stdin.readline().rstrip()
# 공백있는 input값을 받아서 int로 바꾸고 패킹 후 언패킹
# input() -> 이때는 문자열 형태
# input().split() -> 이때는 list형태
# 즉, map은 list형태를 받아서 함수 적용 후 언패킹함
# a, b, c = map(int, input().split())
# 리스트로 바로 받기
# array = list(map(변환함수 , list형태))
