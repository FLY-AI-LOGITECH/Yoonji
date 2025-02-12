def solution(num):
    new = []
    for i in range(len(num)-1):
        for k in range(i+1, len(num)):
            result = num[i] + num[k]
            new.append(result)
 
    answer = list(set(new))
    answer.sort()
    return answer