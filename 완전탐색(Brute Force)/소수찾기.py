import itertools
def solution(numbers):
    set_array = set([])
    numbers_array = [x for x in numbers]
    
    for i in range(1, len(numbers_array) + 1) :
        permu = list(itertools.permutations(numbers_array, i))
        for x in permu :
            value = int(''.join(x))
            if value == 0 or value == 1 :
                continue
            boolean = True
            for y in range(2,value) :
                if value % y == 0 :
                    boolean = False
                    break
            if boolean == True :
                set_array.add(value)
    
    return len(set_array)