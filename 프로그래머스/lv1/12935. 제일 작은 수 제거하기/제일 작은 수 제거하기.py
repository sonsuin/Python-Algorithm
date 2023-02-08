def solution(arr):    
    a = []
    if len(arr) <= 1:
        a.append(-1)
    else:
        min_ = min(arr)
        arr.remove(min_)
        a = arr
    return a