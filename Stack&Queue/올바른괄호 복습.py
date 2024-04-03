# 완전 제대로? 푼 거
def solution(s):
    count = 0
    for char in s:
        # 최소한 0보다 크거나 같아야 제대로 된 괄호 성립
        # 0보다 작으면 )가 많은 거라 바로return False 시킴
        if count < 0:
            return False
        
        if char == "(":
            count += 1
        if char == ")":
            count -= 1
            
    answer = False
    if count == 0:
        answer = True

    return answer




# 아래에 제대로 더 좋게 푼거 확인
def solution(s):
    # 문자열이므로 선형시간으로만 해도 될듯
    answer = False

    start = s[0]
    if start == ")":
        return False

    count = 1
    for i in range(1, len(s)):
        if s[i] == "(":
            count += 1
        if s[i] == ")":
            count -= 1

        # 여기서 중요한게 count가 -1인건 )가 더 많다는 말이라
        # 아예 무조건 False임
        if count < 0:
            return False

    if count == 0:
        answer = True

    return answer


# 이미 더 좋게 풀었던 거 같은데
# count를 -1부터 세게 해서 시작부터 셀 수 있게 해서
# count == 0 일때만 True로 해서 정답 판정 받은 듯
def solution(s):
    answer = False

    count = 0
    for i in s:
        if count > -1:
            if i == "(":
                count += 1
            elif i == ")":
                count -= 1

    if count == 0:
        answer = True

    return answer
