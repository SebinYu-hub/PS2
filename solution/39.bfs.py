"""
[BFS가 실생활에서 어떻게 쓰이는지 예시]

1. 최단 경로 찾기
실생활: 네비게이션에서 최단 거리 경로 탐색
알고리즘 본질: 레벨 단위 탐색으로 최단 경로 보장

2. 주변 시설 검색
실생활: 현재 위치에서 가까운 편의점 찾기
알고리즘 본질: 거리순으로 확장하며 가까운 곳부터 탐색

3. 소셜 네트워크 추천
실생활: LinkedIn의 1촌, 2촌 관계 표시
알고리즘 본질: 레벨별로 확장하며 관계의 깊이 측정

[자주 사용되는 파이썬 문법]
1. 큐 구현
   from collections import deque
   queue = deque()  # 큐 생성
   queue.append(item)  # O(1) 인큐
   item = queue.popleft()  # O(1) 디큐

2. 레벨 관리
   level = 0
   size = len(queue)  # 현재 레벨의 노드 수

[핵심 알고리즘 패턴 수도코드]

# BFS 구현
def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        process(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
"""

# 기존 코드는 유지... 