import heapq
def solution(genres, plays):
    dic_genres = {}
    for i in range(len(genres)) :
        genre = genres[i]
        if genre not in dic_genres :
            dic_genres[genre] = []
            
        heapq.heappush(dic_genres[genre], (-plays[i], i))
            
    def sum_func_genres(genre) :
        sum = 0
        for i in genre :
            sum += plays[i[1]]
            
        return sum
    
    sorted_genres = sorted(dic_genres.items(), key= lambda x: sum_func_genres(x[1]), reverse=True)
    
    answer = []        
    for i in sorted_genres :
        count = 0
        genre_heap = i[1]
        while genre_heap :
            answer.append(heapq.heappop(genre_heap)[1])
            count += 1
            
            if count == 2 :
                break
        
    return answer