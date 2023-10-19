def solution(people, limit):
    people.sort()
    cnt = 0
    light = 0
    heavy = len(people)-1;
    while light <= heavy:
        if(people[light]+people[heavy]<=limit):
            light+=1
        heavy-=1
        cnt+=1
    return cnt