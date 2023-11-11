# deepcopy가 시간 다 잡아 먹었음....ㅠㅠ
import copy
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
        tmp_array = copy.deepcopy(array)
        
        min_count = 9999999
        x1,y1,x2,y2 = query
        # 왼쪽 세로
        for i in range(x1-1, x2 - 1) :
            value = array[i+1][y1-1]
            tmp_array[i][y1-1] = value
            min_count = min(value, min_count)
        # 오른쪽 세로
        for i in range(x1, x2) :
            value = array[i-1][y2-1]
            tmp_array[i][y2-1] = value
            min_count = min(value, min_count)
        # 위쪽 가로
        for i in range(y1, y2) :
            value = array[x1-1][i-1]
            tmp_array[x1-1][i] = value
            min_count = min(value, min_count)
        # 아래쪽 가로
        for i in range(y1-1, y2 - 1) :
            value = array[x2-1][i+1]
            tmp_array[x2-1][i] = value
            min_count = min(value, min_count)
        
        answer.append(min_count)
        array = tmp_array
            
    return answer