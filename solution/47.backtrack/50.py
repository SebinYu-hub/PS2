"""
[Input]
1. n: int
   - 체스판의 크기 (n x n)
   - 제약: 1 <= n <= 12

[Output]
- result: int
  - 퀸을 서로 공격할 수 없게 놓는 방법의 수
  - 제약: result >= 0
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 모든 가능한 퀸 배치를 고려해야 함 : 백트래킹으로 모든 경우 탐색
2. 이전 퀸의 위치가 다음 퀸 배치에 영향 : 상태 체크 배열로 유효성 검사
3. 대각선 방향 체크 필요 : 비트마스킹으로 효율적인 상태 관리
4. 행/열/대각선 충돌 검사 필요 : 체크 배열로 O(1) 시간 검증
5. 모든 해를 찾아야 함 : 완전탐색으로 모든 유효한 배치 카운트
"""
"""
[자료구조]
1. width: Boolean Array
   - 목적: 열 사용 여부 체크
   - 특징: O(1) 접근

2. diagonal1, diagonal2: Boolean Array
   - 목적: 대각선 방향 체크
   - 특징: 비트마스킹으로 상태 관리

[알고리즘: Backtracking]
procedure solve_n_queens(n):
    initialize check arrays (width, diagonal1, diagonal2)
    
    procedure place_queen(row):
        if row == n:
            return 1
        
        count = 0
        for col in range(n):
            if can_place_queen(row, col):
                1. 현재 위치에 퀸 배치
                2. 체크 배열 업데이트
                3. 다음 행으로 재귀 호출
                4. 체크 배열 복구
                
        return count
    
    return place_queen(0)
"""

def solution(n):
    # 최적화 1: 비트마스킹으로 체크 배열 관리
    def getAns(n, y, width, diagonal1, diagonal2):
        # 최적화 2: 지역 변수로 결과값 관리
        ans = 0
        
        # 최적화 3: 모든 행에 퀸 배치 완료 시 1 반환
        if y == n:
            return 1
            
        # 최적화 4: 현재 행에서 가능한 열 위치 탐색
        for i in range(n):
            # 최적화 5: 비트 연산으로 체크 조건 검사
            if width[i] or diagonal1[i + y] or diagonal2[i - y + n]:
                continue
                
            # 최적화 6: 비트 플래그 설정
            width[i] = diagonal1[i + y] = diagonal2[i - y + n] = True
            ans += getAns(n, y + 1, width, diagonal1, diagonal2)
            width[i] = diagonal1[i + y] = diagonal2[i - y + n] = False
            
        return ans
    
    # 최적화 7: list comprehension으로 체크 배열 초기화
    # @reference/list_comprehension.py 참조
    width = [False] * n
    diagonal1 = [False] * (n * 2)
    diagonal2 = [False] * (n * 2)
    
    return getAns(n, 0, width, diagonal1, diagonal2)

# 예시 실행
# print(solution(4))  # 2
# print(solution(8))  # 92
