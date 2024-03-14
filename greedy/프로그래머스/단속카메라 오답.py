def solution(routes):
    answer = 0
    routes.sort(key= lambda x : abs(x[0] - x[1]))
    camera = [False for _ in range(len(routes))]
    for x in range(len(routes)) :
        all_case = {}
        for i in range(routes[x][0], routes[x][1] + 1) :
            all_case[i] = 1
        keys = all_case.keys()
        for y in range(len(routes)) :
            if x == y :
                continue
            for z in keys :
                if routes[y][0] <= z <= routes[y][1] :
                    all_case[z] += 1
        tmp = sorted(all_case.items(), key = lambda x:x[1], reverse=True)
        value = False
        for w in tmp :
            if w[0] in camera : 
                camera[x] = w[0]
                value = True
                break
        if value == False :
            camera[x] = tmp[0][0]
        
    return len(set(camera))