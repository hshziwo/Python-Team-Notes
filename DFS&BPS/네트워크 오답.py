def solution(n, computers):
    def find_parent(parent, x) :
        if parent[x] != x :
            parent[x] = find_parent(parent, parent[x])
        return parent[x]
    
    def union_parent(parent, a, b) :
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b :
            parent[b] = a
        else :
            parent[a] = b
            
    parents = [i for i in range(n)]
    for i in range(len(computers)) :
        for j in range(len(computers[i])) :
            if computers[i][j] == 1 :
                if find_parent(parents, i) != find_parent(parents, j) :
                    union_parent(parents, i, j)
                    
    return len(set(parents))