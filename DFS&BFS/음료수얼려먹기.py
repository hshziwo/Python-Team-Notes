a, b = map(int, input().split())

visited = [[False for j in range(b)] for i in range(a)]

count = 0
for i in range(a) :
    tmp = input()
    for j in range(len(tmp)) :
        if int(tmp[j]) == 0 :
            visited[i][j] = True
        try :
            if visited[i][j] and visited[i-1][j] == False and visited[i][j-1] == False :
                count += 1
        except :
            continue

print(count)