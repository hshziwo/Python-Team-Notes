# 못 풀어서 정답보고 복습함
# 양쪽 끝 투포인터를 설정하는 게 핵심
def solution(people, limit):
    # 먼저 오름차순 정렬
    people.sort()
    cnt = 0
    # 제일 가벼운 왼쪽과 가장 무거운 오른쪽을 동시에 체크하기 위한
    # 양쪽 끝 투포인터를 이용하기 위해 두 인덱스 설정
    light = 0
    heavy = len(people) - 1
    # 두 포인터가 만날때까지 while
    while light <= heavy:
        # 지금 가장 가벼운 사람과 지금 가장 무거운 사람의 합이 limit 괜찮을 때만
        # light값을 한칸 오른쪽으로 이동시킴
        # 문제에서 보트에 최대 2명을 태울 수 있다는 조건을 만족시킴
        if people[light] + people[heavy] <= limit:
            light += 1
        # 항상 무거운 사람은 한번씩 태워서 한칸씩 당겨져야 하므로 조건 필요없이 한칸 왼쪽으로 이동
        heavy -= 1
        # 위의 과정이 한번 돌았으면 보트 한번을 태운 것으로 생각해서 cnt + 1
        cnt += 1
    return cnt
