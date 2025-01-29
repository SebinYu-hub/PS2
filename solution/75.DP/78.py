"""
[Input]
1. board: List[List[int]]
   - 0과 1로 이루어진 2차원 배열
   - 제약: len(board) >= 1
   - 제약: len(board[0]) >= 1
   - 제약: 각 원소는 0 또는 1

[Output]
- result: int
  - 1로 이루어진 가장 큰 정사각형의 넓이
  - 제약: result >= 0
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 정사각형 판별 : DP로 크기 누적
2. 최적 부분 구조 : 이전 상태 활용
3. 공간 최적화 가능 : 입력 배열 재활용
4. 2차원 DP 필요 : 행렬 형태로 처리
5. 누적 값 계산 : 주변 3칸 활용
"""
"""
[자료구조]
- board: List[List[int]]
  - 목적: DP 테이블로 활용
  - 특징: 입력 배열 직접 수정
  - 의미: 각 위치의 최대 정사각형 크기

[알고리즘: Square DP]
procedure find_max_square(board):
    1. Initialize:
       - 기본 케이스 처리 (1xN, Nx1)
       - 경계 조건 확인
    
    2. For each position (i,j):
       - 현재 위치가 1인 경우
       - 좌상단, 상단, 좌측 중 최소값 + 1
       - 최대 크기 갱신
    
    3. Return 최대 크기의 제곱
"""

def solution(board):
    # 최적화 1: 행과 열 크기 저장
    rows, cols = len(board), len(board[0])
    
    # 최적화 2: 기본 케이스 처리
    if rows <= 1 or cols <= 1:
        return max(max(row) for row in board)
    
    # 최적화 3: 최대 정사각형 크기 계산
    max_size = 0
    for i in range(1, rows):
        for j in range(1, cols):
            # 최적화 4: 현재 위치가 1인 경우만 처리
            if board[i][j] == 1:
                # 최적화 5: 주변 3개 위치의 최소값 + 1로 현재 크기 계산
                board[i][j] = min(
                    board[i-1][j],
                    board[i][j-1],
                    board[i-1][j-1]
                ) + 1
                max_size = max(max_size, board[i][j])
    
    return max_size * max_size  # 정사각형 넓이 반환

# 예시 실행
# print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))  # 9
# print(solution([[0,0,1,1],[1,1,1,1]]))  # 4
