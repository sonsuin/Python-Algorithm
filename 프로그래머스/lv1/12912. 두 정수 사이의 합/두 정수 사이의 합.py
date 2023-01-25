def solution(a, b):
    list = []
    if a <= b:
        for i in range(a, b+1):
            list.append(i)
        return sum(list)
    else:
        for i in range(b, a+1):
            list.append(i)
        return sum(list)