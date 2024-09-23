from collections import deque

t = int(input()) # 테스트케이스 개수

def print_doc(n, m, importance_queue):
    doc_queue = deque(range(n)) # 문서의 인덱스 큐

    order = 0
    while True:
        curr_doc_index = doc_queue.popleft()
        curr_doc_importance = importance_queue[curr_doc_index]

        if any(other_doc_importance > curr_doc_importance for other_doc_importance in importance_queue):
            doc_queue.append(curr_doc_index)
        else:
            importance_queue[curr_doc_index] = 0
            order += 1

            if curr_doc_index == m:
                return order

   
for _ in range(t):
    n, m =  map(int, input().split()) # 문서의 개수, 궁금한 문서의 순서
    importance_queue = deque(map(int, input().split())) # 문서의 중요도
    print(print_doc(n, m, importance_queue))