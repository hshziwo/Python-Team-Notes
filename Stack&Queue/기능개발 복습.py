# 큐의 개념을 이용하는데
# 파이썬 원소 합을 위해 그냥 리스트 이용
def solution(progresses, speeds):
    answer = []
    while progresses:
        if progresses[0] < 100:
            progresses = [i + j for i, j in zip(progresses, speeds)]
            continue

        count = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1

        if count != 0:
            answer.append(count)

    return answer
