# 수학문제라 못 풀었음
# 결국에 정답의 팁을 보고 조합 공식을 떠올려 품


def solution(clothes):
    hash_map = {}
    for item in clothes:
        if item[1] not in hash_map:
            hash_map[item[1]] = [item[0]]
        else:
            hash_map[item[1]].append(item[0])

    count = 1
    for item in hash_map.values():
        # 조합의 수 : nC1 + nC0
        count *= len(item) + 1

    # 전체 모두를 안 입는 경우의수 한가지는 제외
    answer = count - 1
    return answer


# 오답
# def solution(clothes):
#     answer = 0
#     hash_map = {}
#     for item in clothes:
#         if item[1] not in hash_map:
#             hash_map[item[1]] = [item[0]]
#         else :
#             hash_map[item[1]].append(item[0])

#     count = 0
#     if len(hash_map.values()) > 1 :
#         count = 1
#         for value in hash_map.values():
#             if len(value) > 0:
#                 count *= len(value)

#     answer = len(clothes) + count
#     return answer
