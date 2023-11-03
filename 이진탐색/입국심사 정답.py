# https://school.programmers.co.kr/questions/49151

# 특정 시간 내에 몇명이 통과 가능한지 카운트해보세요.
# 이분탐색으로 시간을 탐색한다고 생각해보시면 됩니다.

# 접근 방법 자체를 다시 생각해보세요
# 이분 탐색으로 답을 찾는 작업은 작업 시간들을 비교해서 최적의 스케쥴을 찾는것이 아닙니다.

# 작업과정을 간략하게 말하자면 아래와 같으니 참고해보세요

# 처음에 middle 값을 대충 정함
# middle 시간안에 처리할 수 있는 총 사람수를 구함(done_num=sum(mid//time for time in times))
# [해당시간에 처리할수 있는 사람수]와 [목표 사람수]를 비교함
# * [처리할수 있는 사람수]가 [처리해야되는 사람수]보다 많으면 시간을 너무 여유있게 잡았음 -> 시간을 줄여봄
# * [처리할수 있는 사람수]가 [처리해야되는 사람수]보다 적으면 시간을 너무 빡빡하게 잡았음 -> 시간을 늘려봄

# [처리할수 있는 사람수]와 [처리해야되는 사람수]가 같으면
# * 스케쥴은 모르겠지만 아무튼 시간은 구했다! 끝!

def solution(n, times):
    start, end = 0, 10**13
    while start < end :
        mid = (start + end) // 2
        value = sum([mid // x for x in times])
        
        if n <= value :
            # 만족하면 == 모두 성공 이상일때
            # 좌측으로 가야함
            end = mid
        else :
            # 우측으로 가야함
            start = mid + 1
            
    answer = start
    return answer

# 더 좋은 정답
def solution(n, times):
    a,b = 0,1
    while not is_ok(n, times, b):
        a,b = b, 2*b        
    while a<b:
        m = (a+b)//2
        a,b = (a,m) if is_ok(n, times, m) else (m+1,b)
    return a

def is_ok(n, times, x):
    return n <= sum(x//i for i in times)

