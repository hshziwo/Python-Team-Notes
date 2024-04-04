# 이거는 진짜 한줄 컴프리헨션으로
def solution(array, commands):
    return [sorted(array[a[0] - 1 : a[1]])[a[2] - 1] for a in commands]


# 다른 사람이 완전 깔끔하게 푼거
def solution(array, commands):
    answer = []
    for i, j, k in commands:
        answer.append(sorted(array[i - 1 : j])[k - 1])
    return answer


# 이거는 내가 푼거
def solution(array, commands):
    answer = []
    for command in commands:
        tmp_array = array[command[0] - 1 : command[1]]
        tmp_array.sort()
        answer.append(tmp_array[command[2] - 1])

    return answer
