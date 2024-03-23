# 순차탐색: 앞에서부터 하나씩 확인

# 이진탐색: 이미 정렬되어 있는 상황의 리스트에서 <--- 중요
# 탐색범위를 반씩 좁혀 탐색하는 방법
# 시작점, 끝점, 중간점을 이용해서 탐색 범위를 설정
# 중간점은 n/2 에서 소수점 버림 ex) 9 /2 = 4
# 찾고자하는 값이 중간점 보다 작으면 중간점 및 오른쪽은 버림(탐색 안함) == 범위를 좁힌다 -> 시작점과 중간점 왼쪽 사이에 새로운 중간점을 만든다.
# 반대로 찾는 값이 중간점 보다 크면 중간점 및 왼쪽을 버리고 중간점 오른쪽~ 끝점 사이에 새로운 중간점을 만듬
# 계속 반복
# 중간점이 찾는 값이 되면 탐색 멈춤

# !!! 중요한 점!!! 이진탐색을 했을 때 값을 비교해서 다음 스텝으로 왼쪽에 둘꺼나 오른쪽에 둘꺼냐 일때
# 해당 인덱스 -1 +1 로 해도 되지만
# 문제에 따라서는 값에서 +1 -1 로 해서 조건을 만족시켜 이진탐색을 진행해도 됨
# ex) 떡볶이만들기 문제

# 파이썬 이진 탐색 라이브러리
# bisect_left(a, x) : 찾은 모든 x 중에 왼쪽 index를 반환
# bisect_right(a, x) : 찾은 모든 x 중에 오른쪽 index를 반환
# ex)
# from bisect import bisect_left, bisect_right
# a = [1, 2, 4, 4, 8]
# x = 4
# bisect_left(a,x) -> 2 인덱스
# bisect_right(a,x) -> 4 인덱스
# bisect 라이브러리 사용하면 x값들의 count도 구할 수 있음 -> 예제 확인
