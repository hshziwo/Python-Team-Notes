array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# array 중 max값 + 1 만큼 크기를 해줘야함
# 왜냐하면 인덱스는 0부터 시작하기 때문에 3이 제일 크면 [0]*4를 해줘야 3인덱스에 들어감
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        # 이때 count[i] 범위인 이유는 3번 출력하려면 3+1까지 범위를 줘야하기 떄문
        print(i, end=" ")
