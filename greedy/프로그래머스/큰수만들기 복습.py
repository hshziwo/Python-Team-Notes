# 정답 찾아보고 스택으로 다시 품
def solution(number, k):

    stack = []

    # 모든 원소를 stack에 넣어가면서
    # 현재 넣는 원소보다 stack의 맨 위 원소(==stack[-1])가 작을 경우
    # stack의 맨 위 원소 제거
    for num in number:

        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1

        stack.append(num)

    # k가 남을 수도 있음
    # 뒷 원소 k만큼 짜르기
    stack = stack[: len(number) - k]

    # 최종적으로 큰 순서대로 0인덱스부터 쌓임
    # 문자열로 반환
    return "".join(stack)


# 내가 combinations으로 푼 효율성 안 좋은 실패 코드
from itertools import combinations


def solution(number, k):
    return str(
        max(list(map(lambda x: int("".join(x)), combinations(number, len(number) - k))))
    )
