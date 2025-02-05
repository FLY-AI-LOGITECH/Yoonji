def solution(array, commands):
    answer = [] #빈 리스트 생성
    for i in range(len(commands)):
        arr = array[commands[i][0]-1 : commands[i][1]]
        arr.sort() #오름차순 정렬
        answer.append(arr[commands[i][2]-1]) 
    return answer