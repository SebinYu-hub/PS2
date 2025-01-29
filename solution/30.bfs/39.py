"""
[Input]
1. graph: List[List[str]]
   - 무방향 그래프의 간선 정보
   - [(노드1, 노드2), ...] 형태
   - 튜플로 표현된 노드들의 연결 관계

2. start: int
   - 탐색을 시작할 노드 번호
   - 1부터 시작하는 노드 번호

[Output]
- result: List[int]
  - BFS 순회 결과를 담은 노드 리스트
  - 너비 우선 탐색 순서대로 방문한 노드들
"""

"""
[문제 특징] : [알고리즘 선택 이유]
1. 그래프 순회 필요 : BFS 알고리즘 선택
2. 레벨 단위 탐색 : deque로 큐 구현
3. 방문 순서 중요 : 정렬된 순서로 방문
4. 무방향 그래프 : 양방향 연결 처리
5. 방문 관리 필요 : set으로 방문 체크
"""

"""
[자료구조]
1. adj_list: DefaultDict[int, List[int]]
   - 인접 리스트로 구현된 그래프
   - key: 노드 번호
   - value: 인접 노드 리스트

2. visited: Set[int]
   - 방문한 노드들의 집합
   - O(1) 탐색을 위한 set 사용

[알고리즘: Level-order BFS]
procedure breadth_first_search(graph, start):
    1. Initialize:
       - 인접 리스트 구성
       - 방문 집합과 결과 리스트 생성
       - 큐에 시작 노드 추가
    
    2. While queue not empty:
       - 현재 레벨 노드 처리
       - 미방문 이웃 노드들을 큐에 추가
       - 방문 순서 기록
    
    3. Return 방문 순서 리스트
"""

from collections import defaultdict, deque

def solution(graph, start):
    # defaultdict 사용 - KeyError 방지 및 코드 간소화
    adj_list = defaultdict(list)
    for u, v in graph:
        adj_list[u].append(v)
    
    def bfs(start_node):
        visited = set()  # set 사용 - O(1) 시간복잡도로 방문 체크
        result = []
        queue = deque([start_node])  # deque 사용 - 큐 연산 O(1) 시간복잡도
        visited.add(start_node)  # 시작 노드 방문 처리
        result.append(start_node)
        
        while queue:  # BFS 구현 - 레벨 단위 탐색
            node = queue.popleft()  # popleft() - O(1) 시간복잡도
            # sorted 사용 - 방문 순서 보장
            for neighbor in sorted(adj_list.get(node, [])):
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    result.append(neighbor)
        
        return result

    return bfs(start)

# TEST 코드
# print(solution([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (5, 8), (6, 9), (7, 9)], 1))
# print(solution([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)], 1))