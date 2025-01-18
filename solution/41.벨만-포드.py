"""
[Input]
1. graph: list[list[tuple[int, int]]]
   - 그래프의 인접 리스트 표현
   - 제약: 1 ≤ len(graph) ≤ 100
   - 제약: 각 튜플은 (목적지, 가중치)

2. source: int
   - 시작 노드 번호
   - 제약: 0 ≤ source < len(graph)

[Output]
- result: list[Any]
  - [distances, predecessors] 형태의 리스트
  - distances: 각 노드까지의 최단 거리
  - predecessors: 각 노드의 이전 노드
  - 음의 순환 발견 시 [-1] 반환
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 음수 가중치 처리 필요 : 벨만-포드 알고리즘 활용
2. 순환 감지 필요 : 음의 순환 체크
3. 경로 추적 필요 : 이전 노드 기록
4. 메모리 효율성 필요 : defaultdict 사용
5. 최적화 필요 : 변경된 노드만 처리
"""
"""
[자료구조]
1. distance: defaultdict
   - 목적: 최단 거리 저장
   - 특징: 무한대로 초기화
   - 연산: 거리 갱신

2. predecessor: defaultdict
   - 목적: 이전 노드 저장
   - 특징: None으로 초기화
   - 연산: 이전 노드 갱신

[알고리즘: Bellman-Ford]
procedure solution(graph, source):
    1. Initialize:
       - 거리와 이전 노드 배열 초기화
       - 시작점 설정
    
    2. Relax edges:
       - V-1번 반복하여 모든 간선 처리
       - 더 짧은 경로 발견 시 갱신
    
    3. Check negative cycle:
       - 음의 순환 존재 여부 확인
       - 발견 시 [-1] 반환
"""
from collections import defaultdict

def solution(graph, source):
    # 그래프의 노드 수
    num_vertices = len(graph)
    
    # 거리 배열 초기화 - defaultdict 사용으로 KeyError 방지
    distance = defaultdict(lambda: float("inf"))  # O(1) 시간복잡도로 초기화
    distance[source] = 0
    
    # 직전 경로 배열 초기화 - defaultdict 사용으로 KeyError 방지
    predecessor = defaultdict(lambda: None)  # O(1) 시간복잡도로 초기화

    # 최적화: 변경된 노드만 다음 반복에서 검사하기 위한 set
    changed = {source}  # 초기에는 시작 노드만 포함

    # 간선 수 만큼 반복하여 최단 경로 갱신 - O(VE) 시간복잡도
    for i in range(num_vertices - 1):  # V-1번 반복
        if not changed:  # 최적화: 변경된 노드가 없으면 조기 종료
            break
            
        current_changed = set()  # 현재 반복에서 변경된 노드들
        
        for u in changed:  # 최적화: 변경된 노드에 대해서만 검사
            for v, weight in graph[u]:
                # 더 짧은 경로를 찾은 경우 갱신
                if distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight
                    predecessor[v] = u
                    current_changed.add(v)  # 변경된 노드 추가
                    
        changed = current_changed  # 다음 반복에서 검사할 노드들 업데이트

    # 음의 가중치 순환 체크 - O(E) 시간복잡도
    for u in range(num_vertices):
        for v, weight in graph[u]:
            if distance[u] + weight < distance[v]:
                return [-1]  # 음의 순환 발견 시 [-1] 반환

    # 결과를 리스트로 변환하여 반환
    dist_list = [distance[i] for i in range(num_vertices)]
    pred_list = [predecessor[i] for i in range(num_vertices)]
    return [dist_list, pred_list]

# TEST 코드
# print(solution([[(1, 4), (2, 3), (4, -6 )], [(3, 5)], [(1, 2)], [(0, 7), (2, 4)],[(2, 2)]],0))
# print(solution([[(1, 5), (2, -1)], [(2, 2)], [(3, -2)], [(0, 2), (1, 6)]],0))

