"""
[Input]
1. n: int
   - 컴퓨터의 개수
   - 1 ≤ n ≤ 200

2. computers: List[List[int]]
   - n x n 크기의 연결 정보 행렬
   - computers[i][j] = 1: i와 j가 연결됨
   - computers[i][j] = 0: 연결 안됨
   - computers[i][i]는 항상 1

[Output]
- result: int
  - 네트워크의 개수
  - 연결된 컴퓨터들의 집합 개수
"""

"""
[문제 특징] : [알고리즘 선택 이유]
1. 연결 요소 탐색 필요 : DFS로 연결된 컴퓨터 탐색
2. 방문 관리 필요 : 방문 배열로 중복 방문 방지
3. 인접 행렬 구조 : 직접 연결 정보 접근 가능
4. 무방향 그래프 : 양방향 연결 고려
5. 전체 탐색 필요 : 모든 노드에서 DFS 시도
"""

"""
[자료구조]
1. visited: List[bool]
   - 각 컴퓨터의 방문 여부 저장
   - False: 미방문, True: 방문

2. computers: List[List[int]]
   - 인접 행렬로 구현된 그래프
   - 직접 연결 정보 저장

[알고리즘: Connected Components with DFS]
procedure count_networks(n, computers):
    1. Initialize:
       - 방문 배열 초기화
       - 네트워크 카운트 = 0
    
    2. For each computer:
       - 미방문이면 DFS 시작
       - DFS로 연결된 모든 컴퓨터 방문
       - 네트워크 카운트 증가
    
    3. Return 네트워크 개수
"""


def solution(n, computers):
    # 최적화 1: list comprehension으로 방문 배열 초기화
    # @reference/list_comprehension.py 참조
    visited = [False] * n
    answer = 0
    
    # 최적화 5: 모든 노드에 대해 연결 요소 확인
    for node in range(n):
        if not visited[node]:  # 아직 방문하지 않은 노드라면
            # DFS 시작: 스택을 사용하여 반복적으로 구현
            stack = [node]
            
            while stack:
                current = stack.pop()
                visited[current] = True  # 현재 노드 방문 처리
                
                # 최적화 3: enumerate 사용으로 인덱스와 값을 함께 처리
                # n = 3
                # computers = [
                #     [1, 1, 0],  # 컴퓨터 0
                #     [1, 1, 0],  # 컴퓨터 1
                #     [0, 0, 1]   # 컴퓨터 2
                # ]
                # # computers[0] = [1, 1, 0]일 때 enumerate 실행 결과:
                # for next_node, connected in enumerate(computers[0]):
                #     print(f"next_node: {next_node}, connected: {connected}")

                # # 출력:
                # # next_node: 0, connected: 1  # 자기 자신과의 연결
                # # next_node: 1, connected: 1  # 컴퓨터 1과 연결됨
                # # next_node: 2, connected: 0  # 컴퓨터 2와 연결되지 않음
                for next_node, connected in enumerate(computers[current]):
                    print(f"next_node: {next_node}, connected: {connected}")
                    # 최적화 4: 조건 검사를 한번에 처리
                    if connected and not visited[next_node]:
                        stack.append(next_node)  # 스택에 추가하여 나중에 방문
            
            answer += 1  # 새로운 네트워크 발견
            
    return answer

# 예시 실행
# print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))  # 2
# print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))  # 1
