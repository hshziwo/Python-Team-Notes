# def solution(numbers):
#     answer = ''
#     numbers.sort(reverse=True, key = lambda x : str(x)*3) # 사전식 정렬 - 파이썬 특징
#     numbers=''.join(str(s) for s in numbers)
#     return "0" if numbers[0]=="0" else numbers

import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer


# 숫자를 놓을 수 있는 모든 배치를 구하면 시간 초과이다.
# 처음에 DFS로 놓일 수 있는 모든 조합을 구했는데,
# 생각해보니, N이 100,000이므로 시간 초과

# 원소의 길이와 원소의 수
# 원소는 1,000이하, 100,000개 이하이다.
# 최악의 경우 1000*100000 자리의 수가 된다.(이어 붙이는 것이므로)
# 즉 숫자를 위한 자료형으로 풀이할 수 없다.
# 문자열로 가지고 놀아야함.

# 정렬 알고리즘 사용
# 3, 34, 30이 있다고 가정해보자
# 가능한 조합은 33430, 33034, 34330,34303, 30334, 30343 이다.
# 이걸 좀 더 작은 문제로 분할하고, 두 수를 조합해 나올 수 있는 경우는?
# 334, 330, 343, 3430, 303, 3034
# 여기서 얻을 수 있는 인사이트는 두 수를 붙였을 때 큰 방향으로 붙이면 된다는 것

# 3번까지 다 구현했는데, 통과가 안된다면, numbers가 [0,0,0] 일 때의 결과를 살펴보자
# 답은 0이다. 000이 아니라
# 큰 수 방향으로 정렬을 했는데 첫 번째 원소가 0이라면 뒤에 원소들은 어떤 값을 갖게 될까
# 참고로 원소는 0이상 1,000 이하의 값을 가진다.

# 이동규
# 2. 자리수의 경우는 1000은 자리수가 아니라 숫자 최대치이므로 4 * 100,000 이 되겠네요. 애초에 원소가 100,000 개 까지니깐 숫자 자료형은 안되는거죠.

# 이동규―2023.08.24 21:48