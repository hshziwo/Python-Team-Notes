import datetime

# 완전탐색 브루트포싱 문제인데 틀렸음..ㅠㅠ
# n+1까지로 변경해야 정답임
n = int(input())
#a = n * 60 * 60 # 이부분이 틀렸음
a = (n+1) * 60 * 60
count = 0

for i in range(a) :
    txt = str(datetime.timedelta(seconds = i))

    if "3" in txt :
        count += 1

print(count)

