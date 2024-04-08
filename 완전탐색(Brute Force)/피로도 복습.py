from itertools import permutations


def solution(k, dungeons):
    answer = -1
    # 일단 던전을 돌 순서에 대한 순열을 모두 구함
    for list_item in list(permutations(dungeons, len(dungeons))):
        count = 0
        init_k = k
        for item in list_item:
            if init_k >= item[0]:
                init_k -= item[1]
                count += 1
            else:
                # k를 더 쓸 수 없을 경우 그 순서는 종료
                break

        answer = max(answer, count)
    return answer
