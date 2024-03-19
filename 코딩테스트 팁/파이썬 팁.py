# 시간제한 1초일때
# N <= 500 O(N3) 알고리즘 가능
# N <= 2000 O(N2) 알고리즘 가능
# N <= 100000 O(NlogN) 알고리즘 가능
# N <= 10000000 O(N) 알고리즘 가능

# ord() = 문자 -> 숫자
# chr() = 숫자 -> 문자

# array 문자열로 조인
# '구분자'.join(리스트)
# ex) ''.join(['a', 'b', 'c']) -> abc

# 알파벳인지 확인 .isalpha()
# "z".isalpha()

# array 또는 스택 뒤집기
# 1. 슬라이싱방법
# a[start : end : step]
# >>> a = ['a', 'b', 'c', 'd', 'e']
# # 전체를 거꾸로 가져옵니다.
# >>> a[ : : -1 ]
# ['e', 'd', 'c', 'b', 'a']

# 2. num_list.reverse() 메모리사용량이 더 작음
