def solution(n):
    answer = 0
    list = []    
    for i in range(1, n+1, 1):
        if n % i == 0:
            list.append(i)          
    for i in list:
        answer += i 
    return answer

