from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()

        count = 0
        for i in prices:
            count += 1
            if c > i:
                break

        answer.append(count)

    return answer