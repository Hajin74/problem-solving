class Solution :
    N = int(input())
    scores = list(map(int, input().split()))
    
    new_scores = []
    for i, s in enumerate(scores):
        new_scores.append(s / max(scores) * 100)

    print(sum(new_scores)/len(new_scores))