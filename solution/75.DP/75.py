"""
[Input]
1. triangle: List[List[int]]
   - 삼각형 모양의 2차원 정수 배열
   - 제약: len(triangle) >= 1
   - 제약: len(triangle[i]) == i+1
   - 제약: 각 원소는 정수

[Output]
- result: int
  - 최대 경로 합
  - 제약: result는 정수
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 최적 부분 구조 : DP 접근 가능
2. 상향식 계산 유리 : 아래에서 위로 DP
3. 공간 최적화 가능 : 한 줄만 저장
4. 인접 원소만 이동 : 이전 행 활용
5. 누적 합 계산 : 경로 합 갱신
"""
"""
[자료구조]
- dp: List[int]
  - 목적: 각 위치까지의 최대 경로 합 저장
  - 특징: 한 줄만 유지하여 공간 최적화
  - 갱신: 아래에서 위로 계산

[알고리즘: Bottom-up Triangle DP]
procedure find_max_path(triangle):
    1. Initialize:
       - 마지막 행으로 DP 배열 초기화
    
    2. For each row from bottom to top:
       - 현재 위치에서 아래 두 값 중 최대값 선택
       - 현재 위치 값과 더하여 DP 갱신
    
    3. Return DP[0] (최상단 값)
"""

def solution(triangle):
  # 최적화 1: 마지막 행을 복사하여 DP 배열 초기화
  # @reference/list_comprehension.py 참조
  dp = triangle[-1][:]
  
  # 최적화 2: 아래에서 위로 올라가며 최대값 계산
  for i in range(len(triangle)-2, -1, -1):
    # 최적화 3: 현재 행의 각 위치에서 최대값 계산
    for j in range(len(triangle[i])):
      # 최적화 4: 아래 두 값 중 큰 값을 선택하여 현재 값과 더함
      dp[j] = triangle[i][j] + max(dp[j], dp[j+1])
  
  # 최적화 5: 최상단 값이 최대 경로 합
  return dp[0]

# 예시 실행
# print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))  # 30
