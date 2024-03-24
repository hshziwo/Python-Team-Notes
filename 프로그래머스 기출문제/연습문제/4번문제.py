# 문자열에서 반복되는 패턴 중 가장 짧은 문자열의 길이
# [Python] 백준 1305번: 광고
# https://www.acmicpc.net/problem/1305
# 해설
# https://rccode.tistory.com/137
# https://rccode.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-1893%EB%B2%88-%EC%8B%9C%EC%A0%80-%EC%95%94%ED%98%B8


def solution4(string):
    length = len(string)
    pi = [0] * length
    j = 0

    for i in range(1, length):
        # j는 0부터 i는 1부터
        while j > 0 and string[i] != string[j]:
            # 현재 i번째 문자와 j의 문자가 맞지 않으면 계속 j인덱스를 내려줌
            j = pi[j - 1]

        if string[i] == string[j]:
            # j인덱스의 문자와 i인덱스의 문자가 맞다면 현재까지의 맞은 length(= j+1)를 pi에 저장함.
            j += 1
            pi[i] = j

    # 전체 길이에서 suffix(pi[-1]) 길이를 제거하면 반복되는 패턴 중 가장 짧은 문자열의 길이이다
    return length - pi[-1]


print(solution4("abcabc"))
