# DFS

## 코드 스니펫
```
def dfs(graph, v, visited):
	visited[v] = True

	for i in graph[v]:
		if not visited[i]:
			dfs(graph, i, visited)

```

</br>

## 흐름
1. 현재 노드 방문 처리
2. 현재 노드와 인접한 노드들 탐색
	2-1. 인접 노드가 방문하지 않았다면, 재귀적 방문

</br>

## 사용 예시
- 모든 경로 탐색
- 최장 경로
- 재귀적 구조