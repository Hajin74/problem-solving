def solution(answers):
    # 찍는 방식
    way1 = [1, 2, 3, 4, 5]
    way2 = [2, 1, 2, 3, 2, 4, 2, 5]
    way3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 정답을 모두 탐색하면서 찍은 번호와 맞는지 확인
    correct = [0, 0, 0]
    for i in range(len(answers)):
        if way1[i % 5] == answers[i]:
            correct[0] += 1
        if way2[i % 8] == answers[i]:
            correct[1] += 1
        if way3[i % 10] == answers[i]:
            correct[2] += 1
            
    return [index + 1 for index, value in enumerate(correct) if value == max(correct)]