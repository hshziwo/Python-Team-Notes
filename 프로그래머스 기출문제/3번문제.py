# 과일을 5개들이, 3개 들이 상자에 담는데 상자 갯수를 최소로 해서 담는 방법, 단 모든 상자가 꽉 차야 하고 못 나누어 담으면 0을 반환

# 비슷한 문제 백준 14916번 - 거스름돈
# https://www.acmicpc.net/problem/14916
# 해설
# https://devjeong.com/algorithm/algorithm-4/
# 춘향이는 편의점 카운터에서 일한다.

# 손님이 2원짜리와 5원짜리로만 거스름돈을 달라고 한다. 2원짜리 동전과 5원짜리 동전은 무한정 많이 가지고 있다. 동전의 개수가 최소가 되도록 거슬러 주어야 한다. 거스름돈이 n인 경우, 최소 동전의 개수가 몇 개인지 알려주는 프로그램을 작성하시오.

# 예를 들어, 거스름돈이 15원이면 5원짜리 3개를, 거스름돈이 14원이면 5원짜리 2개와 2원짜리 2개로 총 4개를, 거스름돈이 13원이면 5원짜리 1개와 2원짜리 4개로 총 5개를 주어야 동전의 개수가 최소가 된다.

# 입력
# 첫째 줄에 거스름돈 액수 n(1 ≤ n ≤ 100,000)이 주어진다.

# 출력
# 거스름돈 동전의 최소 개수를 출력한다. 만약 거슬러 줄 수 없으면 -1을 출력한다.


def solution3(fruits):
    answer = 0

    while fruits > 0:
        # 5로 나눠질때까지 -3을 빼주면서 카운팅하고 5로 나눠지는 순간 나눌 수 있는 몫을 카운트에 더하고 멈추면 정답
        if fruits % 5 == 0:
            answer += fruits // 5
            break
        else:
            fruits -= 3
            answer += 1

    if fruits < 0:
        return 0
    else:
        return answer


print(solution3(7))
