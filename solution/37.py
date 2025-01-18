# 크루스칼 알고리즘 사용
# - 가중치 무방향 그래프에서
# 최소 가중치 누적값으로 + 가장 많이 탐색 = 최소신장트리
# 사이클 안만들면서

# 유니온파인드로 루트 다르면 연결해서 사이클 만들기 방지하기




def find(parent, i):
    # 최적화 1: 경로 압축을 통한 find 연산
    if parent[i] == i:
        return i
    parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    # 최적화 2: Union by Rank를 통한 트리 높이 최소화
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1


"""
Input:
- n: int (노드의 개수)
- costs: List[List[int]] (간선 정보)
  - costs[i] = [node1, node2, cost]
  - node1, node2: 연결할 노드 번호 (0 to n-1)
  - cost: 연결 비용

Output:
- min_cost: int (최소 신장 트리의 총 비용)
"""
"""
[Kruskal MST Algorithm]
Data Structures:
- parent[]: Disjoint Set for cycle detection
- rank[]: Tree height optimization
- edges[]: Sorted edge list by weight

Algorithm:
1. Initialize DisjointSet(n)
2. Sort edges by weight
3. For each edge in sorted edges:
    If not creates_cycle(edge):
        Add edge to MST
        Union nodes
    If edge_count == n-1:
        break
4. Return total_cost

Time: O(E log E)
Space: O(V)
"""
def solution(n, costs):
    # 최적화 3: key 함수를 사용한 정렬로 성능 향상
    costs.sort(key=lambda x: x[2])
    
    parent = [i for i in range(n)]
    rank = [0] * n
    
    min_cost = 0
    edges = 0

    # 최적화 4: early return으로 불필요한 반복 방지
    for u, v, cost in costs:
        if edges == n - 1:
            break
            
        x = find(parent, u)
        y = find(parent, v)
        
        if x != y:
            union(parent, rank, x, y)
            min_cost += cost
            edges += 1

    return min_cost

# TEST 코드입니다
# print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))  # 4
