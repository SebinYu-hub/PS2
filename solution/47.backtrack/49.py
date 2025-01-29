"""
[Input]
1. k: int
   - 초기 체력/에너지
   - 제약: k > 0

2. dungeons: List[List[int]]
   - 던전 정보 배열
   - 각 던전 [필요 에너지, 소모 에너지]
   - 제약: len(dungeons) > 0

[Output]
- result: int
  - 탐험 가능한 최대 던전 수
  - 제약: 0 <= result <= len(dungeons)
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 모든 던전 방문 순서 고려 필요 : DFS로 모든 경우의 수 탐색
2. 이전 선택이 이후 선택에 영향 : 백트래킹으로 상태 관리
3. 방문 여부 추적 필요 : visited 배열로 상태 체크
4. 최적해 보장 필요 : 완전탐색으로 모든 경우 확인
5. 선택 취소 필요 : 백트래킹의 상태 복구(visited[i] = 0)
"""
"""
[자료구조]
- visited: Boolean Array
  - 목적: 던전 방문 상태 추적
  - 특징: O(1) 접근, 상태 토글 용이

[알고리즘: Backtracking DFS]
procedure explore_dungeons(energy, dungeons):
    initialize visited array
    
    procedure dfs(current_energy, visited_count):
        1. 현재까지의 최대 방문 수 기록
        2. 모든 던전에 대해:
            if (방문 가능 && 미방문):
                a. 방문 표시
                b. 에너지 소모하여 다음 탐색
                c. 방문 표시 제거
        3. 최대 방문 수 반환
    
    return dfs(initial_energy, 0)
"""
def solution(k, dungeons):
    # 최적화 1: 방문 배열을 list comprehension으로 초기화
    # @reference/list_comprehension.py 참조
    visited = [0] * len(dungeons)
    
    # 최적화 2: DFS 함수를 내부에 정의하여 변수 접근 최적화
    # @mistake/variable_scope_tutorial.py 참조
    def dfs(curr_k, count):
        max_count = count  # 현재까지의 최대 탐험 횟수
        
        # 최적화 3: enumerate 사용으로 인덱스와 값을 함께 처리
        for i, (min_k, use_k) in enumerate(dungeons):
            # 최적화 4: 조건 검사를 한번에 처리
            if curr_k >= min_k and not visited[i]:
                visited[i] = 1  # 던전 방문 처리
                # 최적화 5: 재귀 호출 결과와 현재 최대값 비교
                max_count = max(
                    max_count,
                    dfs(curr_k - use_k, count + 1)
                )
                visited[i] = 0  # 방문 상태 복구
                
        return max_count
    
    # 최적화 6: 초기 호출 시 현재 피로도와 카운트 0으로 시작
    return dfs(k, 0)

# 예시 실행
# print(solution(80, [[80,20],[50,40],[30,10]]))  # 3
# print(solution(40, [[40,20],[10,10],[10,10],[10,10],[10,10]]))  # 4
