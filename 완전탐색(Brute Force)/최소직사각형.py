# 팁
# 사실상 문제를 보면 가로x세로 길이를 명시해서 더 헷갈리게 만들었다.
# 사실 어떤 모서리는 가로가 될 수도 있고 세로도 될 수가 있다.
# 그치만 한 모서리를 가로라고 지정하면 다른 모서리는 세로가 되어야 옳다.

# 두 개의 모서리를 비교하여 큰 값을 전부 가로 작은 값을 전부 세로로 두면
# 각 모서리의 길이의 최댓값이 답이 되지않을까?


def solution(sizes):
    answer = 0
    x = []
    y = []
    for i in sizes :
        a, b = i[0],i[1]
        if a > b :
            x.append(a)
            y.append(b)
        else :
            x.append(b)
            y.append(a)
        
    answer = max(x) * max(y)
    return answer