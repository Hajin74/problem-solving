from itertools import permutations

def solution(dots):
    perms = list(permutations(dots, 4))
   
    for perm in perms:
        # print(perm)
        a, b, c, d = perm
        if ((a[0]-b[0]) / (a[1]-b[1])) == ((c[0]-d[0] )/(c[1]-d[1])):
            return 1  
        
    return 0

# 기울기가 같으면 평행하다
# 모든 점들 2개씩 묶어, 기울기가 평행한지 탐색한다