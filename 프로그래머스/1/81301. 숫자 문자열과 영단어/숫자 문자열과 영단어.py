def solution(s):
    english = ['zero', 'one', 'two', 'three', 'four',
               'five', 'six', 'seven', 'eight', 'nine']
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(len(english)):
        s = s.replace(english[i], number[i])
        #answer = int(s)
    answer = int(s)
    return answer

