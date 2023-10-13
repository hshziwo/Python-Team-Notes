from itertools import permutations
def solution(k, dungeons):
    answer = 0
    n = len(dungeons)
    for order in permutations(range(n)):
        #print(t)
        cur = k
        local_ans = 0
        for t in order:
            require, consum = dungeons[t]
            if cur >= require:
                cur -= consum
                local_ans += 1
        answer = max(answer, local_ans)


    return answer