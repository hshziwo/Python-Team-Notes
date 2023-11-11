# deepcopy 안쓴 버전이긴 한데... 통과는 됐으나 코드가 넘 복잡..
def solution(rows, columns, queries):
    count = 1
    array = []
    for i in range(rows) :
        tmp = []
        for j in range(columns) :
            tmp.append(count)
            count += 1
        array.append(tmp)
        
    if len(queries) == 1 :
        return [array[queries[0][0] - 1][queries[0][1] - 1]]    
    
    answer = []
    for query in queries :
        tmp_array = [[0]*columns for _ in range(rows)]
        
        min_count = 9999999
        x1,y1,x2,y2 = query
        # 왼쪽 세로
        for i in range(x1-1, x2 - 1) :
            tmp_array[i][y1-1] = array[i][y1-1]
            value = array[i+1][y1-1]
            if tmp_array[i+1][y1-1] != 0 :
                value = tmp_array[i+1][y1-1]
            array[i][y1-1] = value
            min_count = min(value, min_count)
        # 오른쪽 세로
        for i in range(x1, x2) :
            tmp_array[i][y2-1] = array[i][y2-1]
            value = array[i-1][y2-1]
            if tmp_array[i-1][y2-1] != 0 :
                value = tmp_array[i-1][y2-1]
            array[i][y2-1] = value
            min_count = min(value, min_count)
        # 위쪽 가로
        for i in range(y1, y2) :
            tmp_array[x1-1][i] = array[x1-1][i]
            value = array[x1-1][i-1]
            if tmp_array[x1-1][i-1] != 0 :
                value = tmp_array[x1-1][i-1]
            array[x1-1][i] = value
            min_count = min(value, min_count)
        # 아래쪽 가로
        for i in range(y1-1, y2 - 1) :
            tmp_array[x2-1][i] = array[x2-1][i]
            value = array[x2-1][i+1]
            if tmp_array[x2-1][i+1] != 0 :
                value = tmp_array[x2-1][i+1]
            array[x2-1][i] = value
            min_count = min(value, min_count)
        
        answer.append(min_count)
            
    return answer