def solution(numbers):
    result = []
    a = [i for i in range(1, 10)]
    for i in a:
        if i not in numbers:
            result.append(i) 
    return sum(result)