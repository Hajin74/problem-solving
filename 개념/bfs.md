# BFS

## 코드 스니펫
```
from collection import deque

def dfs(graph, start, visited):
	queue = deque([start])
	visited[start] = True

	while queue:
		v = queue.popleft()

		for i in graph[v]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True
```

</br>

## 흐름
1. 시작 노드 큐 삽입 및 방문 처리
2. 큐가 빌 때까지 반복
2-1. 큐 꺼내서 현재 노드로 저장
2-2. 현재 노드와 인접한 노드 탐색
2-2-1. 인접 노드가 방문하지 않았다면 큐 삽입 및 방문처리

</br>

## 사용 예시
- 가중치 없는 최단 경로
- 레벨 순서대로 탐색
- 최소 비용, 최단 이동
- 방문 표시를 통해서 depth를 표시할 수 있다 -> 전에 있던 경로에 +1

</br>

## 문제
|플랫폼|문제 이름|문제 레벨|문제 링크|
|---|---|---|---|
|프로그래머스|네트워크|level3|https://school.programmers.co.kr/learn/courses/30/lessons/43162|
백준|숨바꼭질4|Gold IV|https://www.acmicpc.net/problem/13913|
