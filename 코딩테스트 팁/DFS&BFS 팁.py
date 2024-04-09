# 스택(선입후출)은 리스트 그냥 사용
# DFS시에 사용됨
# stack = []
# stack.append()
# stack.pop()

# But!!!!! DFS에서는 stack 보다는 재귀함수를 사용해서 구현하는 게 일반적이고 직관적
# 단, return 처리를 잘 해줘야 함
# 재귀함수를 여러번 호출하면 컴퓨터 내부의 스택에 함수가 쌓이므로 스택을 이용하는 것과 같음


# 미로탈출과 같은 상하좌우 문제는 BFS문제!!!! deque을 이용한 queue문제!!!!! 꼭 기억!!!!!

# 큐(선입선출)은 deque 라이브러리 사용
# 주로 BFS에서 queue에 bfs 순서대로 append하고 popleft로 꺼내서 사용함.
# from collections import deque
# queue = deque()
# 오른쪽으로 들어가서 왼쪽으로 나간다고 생각해야함(선입선출)
# queue.append()
# queue.popleft()
# queue.reverse() 가능
