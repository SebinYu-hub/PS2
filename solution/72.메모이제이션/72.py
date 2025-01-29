"""
[Input]
1. arr: List[List[int]]
   - 3xN 크기의 2차원 정수 배열
   - 제약: len(arr) == 3
   - 제약: len(arr[0]) >= 1
   - 제약: 각 원소는 정수

[Output]
- result: int
  - 최대 가중치 경로의 합
  - 제약: result >= 0
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 상태 전이 필요 : DP 테이블 활용
2. 패턴 기반 선택 : 4가지 패턴 정의
3. 최적 부분 구조 : DP로 해결 가능
4. 중복 계산 발생 : 메모이제이션 필요
5. 열 단위 처리 : 상태 압축 가능
"""
"""
[자료구조]
- dp: List[int]
  - 목적: 각 패턴별 최대값 저장
  - 특징: 4가지 상태만 유지
  - 패턴: [상단만, 중단만, 하단만, 상하단]

[알고리즘: Pattern-based DP]
procedure find_max_path(arr):
    1. Initialize:
       - 첫 열에 대한 DP 상태 초기화
       - 4가지 패턴별 초기값 설정
    
    2. For each column:
       - 각 패턴에 대해 이전 상태 활용
       - 현재 열에서 가능한 최대값 계산
       - 상태 전이 규칙 적용
    
    3. Return 마지막 열의 최대값
"""

def solution(arr):
    # 최적화 1: 상수로 패턴 정의
    PATTERN_TOP = 0      # 상단만 선택
    PATTERN_MID = 1      # 중단만 선택
    PATTERN_BOT = 2      # 하단만 선택
    PATTERN_BOTH = 3     # 상단과 하단 선택
    
    # 최적화 2: 열의 개수 저장
    n = len(arr[0])
    
    # 최적화 3: DP 배열 초기화 (첫 번째 열)
    dp = [0] * 4
    dp[PATTERN_TOP] = arr[0][0]
    dp[PATTERN_MID] = arr[1][0]
    dp[PATTERN_BOT] = arr[2][0]
    dp[PATTERN_BOTH] = arr[0][0] + arr[2][0]
    
    # 최적화 4: 각 열에 대해 최적의 선택 계산
    for i in range(1, n):
        curr = [0] * 4
        
        # 패턴 0: 상단만 선택 가능한 경우
        curr[PATTERN_TOP] = arr[0][i] + max(dp[PATTERN_MID], dp[PATTERN_BOT])
        
        # 패턴 1: 중단만 선택 가능한 경우
        curr[PATTERN_MID] = arr[1][i] + max(dp[PATTERN_TOP], dp[PATTERN_BOT], dp[PATTERN_BOTH])
        
        # 패턴 2: 하단만 선택 가능한 경우
        curr[PATTERN_BOT] = arr[2][i] + max(dp[PATTERN_TOP], dp[PATTERN_MID])
        
        # 패턴 3: 상단과 하단 선택 가능한 경우
        curr[PATTERN_BOTH] = arr[0][i] + arr[2][i] + dp[PATTERN_MID]
        
        dp = curr  # 다음 열 계산을 위해 현재 상태 저장
    
    # 최적화 5: 마지막 열에서 최대 가중치 반환
    return max(dp)

# 예시 실행
# print(solution([[1, 3, 3, 2], [2, 1, 4, 1], [1, 5, 2, 3]]))  # 19
# print(solution([[1, 7, 13, 2, 6], [2, -4, 2, 5, 4], [5, 3, 5, -3, 1]]))  # 32
