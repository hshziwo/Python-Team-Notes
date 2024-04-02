def solution(arr):
    array = [arr[0]]
    for i in range(1, len(arr)):
        if array[-1] == arr[i]:
            continue
        else:
            array.append(arr[i])
    return array
