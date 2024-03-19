# ord = 문자 -> 숫자
# chr = 숫자 -> 문자

import sys

input = lambda: sys.stdin.readline().rstrip()

string = input()
x = int(string[1])
y = int(ord(string[0])) - 96
# 팁 string[0]에서 받은 거에 a값을 빼주면 0이고 거기에 1이 초기값이니까 +1 해주면 96 상수를 빼주지 않아도 됨.
# y = int(ord(string[0])) - int(ord('a')) + 1


n = [-1, 1, 2, 2, 1, -1, -2, -2]
m = [-2, -2, -1, 1, 2, 2, -1, 1]

count = 0
for i in range(len(n)):
    nx = x + n[i]
    ny = y + m[i]

    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue

    count += 1

print(count)
