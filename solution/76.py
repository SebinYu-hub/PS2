"""
[Input]
1. land: List[List[int]]
   - N x 4 크기의 2차원 정수 배열
   - 제약: len(land) >= 1
   - 제약: len(land[i]) == 4
   - 제약: 각 원소는 정수

[Output]
- result: int
  - 최대 점수 합
  - 제약: result는 정수
  - 제약: 연속된 열 선택 불가
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 상태 전이 제한 : DP로 상태 관리
2. 열 선택 제약 : 이전 열 정보 활용
3. 최적 부분 구조 : DP 접근 가능
4. 중복 계산 발생 : 메모이제이션 필요
5. 행 단위 처리 : 상태 압축 가능
"""
"""
[자료구조]
- dp: List[int]
  - 목적: 각 열까지의 최대 점수 저장
  - 특징: 4개 열에 대한 상태만 유지
  - 갱신: 이전 행의 다른 열 값 활용

[알고리즘: Column-restricted DP]
procedure find_max_score(land):
    1. Initialize:
       - 첫 행으로 DP 배열 초기화
    
    2. For each row:
       - 각 열에 대해 이전 행의 다른 열 중 최대값 선택
       - 현재 값과 더하여 DP 갱신
    
    3. Return max(DP) (마지막 행의 최대값)
"""

def solution(land):
    # 최적화 1: 첫 번째 행을 복사하여 DP 배열 초기화
    # @reference/list_comprehension.py 참조
    dp = land[0][:]
    
    # 최적화 2: 각 행에 대해 최대값 계산
    for i in range(1, len(land)):
        # 최적화 3: 현재 행의 값을 임시 저장
        curr = [0] * 4
        
        # 최적화 4: 각 열에 대해 이전 행의 다른 열 중 최대값 선택
        for j in range(4):
            # 최적화 5: 리스트 슬라이싱으로 현재 열 제외한 최대값 계산
            prev_max = max(dp[:j] + dp[j+1:])
            curr[j] = land[i][j] + prev_max
        
        dp = curr  # 다음 행 계산을 위해 현재 값 저장
    
    return max(dp)  # 마지막 행에서의 최대값 반환

# 예시 실행
# print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))  # 16
