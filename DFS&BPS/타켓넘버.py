def solution(numbers, target):
    answer = 0
    def dfs(idx, x) :
        nonlocal answer
        if idx == len(numbers) :
            if target == x :
                answer += 1
            return False
        y = numbers[idx]
        dfs(idx+1, x+y)
        dfs(idx+1, x-y)
    dfs(0, 0)    
    return answer