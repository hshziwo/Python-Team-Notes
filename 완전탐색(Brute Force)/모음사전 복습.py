# 중복 순열(product)로 풀긴했는데 이게 맞나ㅋㅋㅋ
# N이 5까지니까 가능한 문제
from itertools import product


def solution(word):
    alpabet = ["A", "E", "I", "O", "U"]
    word_list = []
    # 모든 중복 순열에 대해 word_list에 더해줌
    for i in range(1, 6):
        word_list += list(map(lambda x: "".join(x), product(alpabet, repeat=i)))

    # 사전식으로 오름차순 정렬
    word_list.sort()
    # 현재 단어의 인덱스는 0부터 시작하니까 1을 더해줌
    return word_list.index(word) + 1


# list 컴프리헨션으로 한줄로 푼거
# (한줄로 푼거인데 black 때문에 여러줄 됐네...)
def solution(word):
    a = [
        "".join(list(j))
        for i in range(1, 6)
        for j in product(["A", "E", "I", "O", "U"], repeat=i)
    ]
    a.sort()
    return a.index(word) + 1


# 딴 사람이 푼 거 중에
# 아래와 같이 itertools의 product를 안쓰고 직접 만드는 방법도 있음
# N이 5까지니까 가능한 문제
def solution(word):
    answer = 0
    alpha = ["A", "E", "I", "O", "U", ""]
    ans = []
    for i in alpha:
        for j in alpha:
            for k in alpha:
                for l in alpha:
                    for m in alpha:
                        # 문자열 합이라서 공백을 처리해줬다 미친
                        w = i + j + k + l + m
                        if w not in ans:
                            ans.append(w)
    ans.sort()
    answer = ans.index(word)
    return answer
