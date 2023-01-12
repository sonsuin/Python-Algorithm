def solution(n):
    answer = -1
    s = n ** 0.5
    if n // s == s :
        answer = (s + 1) ** 2
    return answer