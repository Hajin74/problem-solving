import itertools

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))   

# 치킨 집 하나당 모든 집의 치킨 거리를 리스트에 저장한다.
# 리스트에서 오름차순으로 정렬하여 최소의 치킨 거리로 만들고
# m만큼 리스트의 요소를 더한게 모든 치킨집의 최소 거리다.

def get_chicken_distance(home_spot, chicken_spot):
    return abs(chicken_spot[0] - home_spot[0]) + abs(chicken_spot[1] - home_spot[1])
    
home_spots = []
chicken_spots = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home_spots.append((i, j))
        elif graph[i][j] == 2:
            chicken_spots.append((i, j))
# print(chicken_spots)

comb = list(itertools.combinations(chicken_spots, m))
all_chicken_distances = []
for i in range(len(comb)):
    all_chicken_distance = 0
    for home_spot in home_spots:
        distance = []
        for chicken_spot in comb[i]:
            distance.append(get_chicken_distance(home_spot, chicken_spot))
        all_chicken_distance += min(distance)
    all_chicken_distances.append(all_chicken_distance)

print(min(all_chicken_distances))