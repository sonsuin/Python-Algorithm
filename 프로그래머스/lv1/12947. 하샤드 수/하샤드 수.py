def solution(x):
    x1 = list(str(x))
    x1 = map(int, x1)
    s = sum(x1)
    
    if x % s == 0:
        return True
    else:
        return False
