def solution(participant, completion):
    # 내림차순이냐 오름차순이냐는 운빨일꺼 같음ㅠㅠ
    # participant.sort(reverse = True)
    # completion.sort(reverse = True)
    participant.sort()
    completion.sort()
    for i in range(len(participant) - 1):
        if participant[i] != completion[i]:
            return participant[i]

    # 못 찾았으면 맨 마지막 사람이다. 이러면 최악일듯...
    return participant[-1]


# Counter를 이용한 풀이
import collections


def solution(participant, completion):
    # 카운터 객체는 빼기가 되네... 대박
    # 이거 알았으면 아까 Set으로 차집합하려고 했던 거 그냥 바로 하면 됨
    answer = collections.Counter(participant) - collections.Counter(completion)
    # Counter 객체인 answer의 keys들만 뽑아서 list로 만들고
    # 어짜피 문제에서는 하나만 남을 것이므로 0번째 원소를 뽑으면 정답
    return list(answer.keys())[0]
