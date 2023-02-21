def solution(arr1, arr2):
    row = len(arr1)
    col = len(arr1[0])
    
    result = []
    for i in range(row):
        temp = []
        for j in range(col):
            temp.append(arr1[i][j] + arr2[i][j])
        result.append(temp)
    
    return result
            