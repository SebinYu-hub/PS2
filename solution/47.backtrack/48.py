"""
Input:
- board: List[List[int]]
  - 9x9 2D array
  - 0: 빈 칸
  - 1-9: 이미 채워진 숫자

Output:
- board: List[List[int]]
  - 완성된 스도쿠 보드
  - 모든 0이 유효한 1-9 숫자로 채워짐
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 모든 빈 칸을 채워야 함 : 백트래킹으로 모든 가능한 숫자 시도
2. 행/열/박스 제약조건 검사 필요 : 유효성 검사 함수로 제약 확인
3. 이전 선택이 이후 선택에 영향 : 재귀적 접근으로 상태 관리
4. 유일한 해를 찾아야 함 : 완전탐색으로 유효한 해 보장
5. 잘못된 선택 취소 필요 : 백트래킹으로 상태 복구
"""
"""
[자료구조]
1. 2D Array (board)
   - 목적: 스도쿠 보드 상태 관리
   - 특징: O(1) 접근, 상태 변경 용이

[알고리즘: Backtracking]
procedure solve_sudoku(board):
    initialize board state
    
    procedure solve():
        if board is complete:
            return True
            
        find next empty cell
        for number in 1-9:
            if valid placement:
                1. 숫자 배치
                2. 재귀적으로 다음 빈 칸 해결
                3. 실패시 배치 취소
                
        return False
    
    return solve()

"""

def solution(board):
    def is_valid(num, row, col):
        # 행 검사
        if num in board[row]:
            return False
            
        # 열 검사
        for i in range(9):
            if board[i][col] == num:
                return False
                
        # 3x3 박스 검사
        box_row, box_col = (row // 3) * 3, (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[box_row + i][box_col + j] == num:
                    return False
                    
        return True

    def find_empty():
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    return row, col
        return None
        
    def solve():
        empty = find_empty()
        if not empty:
            return True
            
        row, col = empty
        for num in range(1, 10):
            if is_valid(num, row, col):
                board[row][col] = num
                if solve():
                    return True
                board[row][col] = 0
                
        return False

    solve()
    return board

# 예시 실행
# board = [
#     [5,3,0,0,7,0,0,0,0],
#     [6,0,0,1,9,5,0,0,0],
#     [0,9,8,0,0,0,0,6,0],
#     [8,0,0,0,6,0,0,0,3],
#     [4,0,0,8,0,3,0,0,1],
#     [7,0,0,0,2,0,0,0,6],
#     [0,6,0,0,0,0,2,8,0],
#     [0,0,0,4,1,9,0,0,5],
#     [0,0,0,0,8,0,0,7,9]
# ]
# print(solution(board))





