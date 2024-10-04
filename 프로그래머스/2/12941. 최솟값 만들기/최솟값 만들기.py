def solution(A,B):
    # 곱이 최소가 되게 배열을 정렬
    A.sort()
    B.sort(reverse=True)
    
    sum = 0
    for i in range(len(A)):
        sum += A[i] * B[i]
    
    return sum