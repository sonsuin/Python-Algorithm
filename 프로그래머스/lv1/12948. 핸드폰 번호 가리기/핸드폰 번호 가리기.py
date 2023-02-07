def solution(phone_number):
    back = phone_number[-4:]
    l = len(phone_number)
    return '*'*(l-4) + back