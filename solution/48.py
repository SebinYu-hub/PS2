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
BackTracking with Constraints:
1. State Space: 2D Matrix
2. Constraints: Row, Column, Sub-grid rules
3. Solution Finding:
    - Find empty space
    - Try valid values
    - Recursively solve
    - Backtrack if invalid

def solve(state):
    if state is complete:
        return solution
    
    space = find_next_empty(state)
    for value in possible_values:
        if is_valid(state, space, value):
            apply(state, space, value)
            if solve(state):
                return solution
            undo(state, space)
    
    return failure
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





