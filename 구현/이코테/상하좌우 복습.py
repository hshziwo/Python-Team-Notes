n = int(input())
plans = input().split()

move_types = ["L", "R", "U", "D"]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

x, y = 1, 1
for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)


# n = int(input())
# plan = list(input().split())

# plan_map= {
#     "L": -1,
#     "R": 1,
#     "U": -1,
#     "D": 1
# }
# x = 1
# y = 1
# for i in plan:
#     if i == "U" or i == "D":
#         tmp = x + plan_map[i]
#         if 1 <= tmp <= n :
#             x = tmp
#     else:
#         tmp = y + plan_map[i]
#         if 1 <= tmp <= n:
#             y = tmp

# print(x, y)
