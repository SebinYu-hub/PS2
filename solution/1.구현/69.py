"""
[Input]
1. keyinput: List[str]
   - 방향키 입력 배열 ("up", "down", "left", "right")
   - 제약: len(keyinput) >= 0
   - 제약: 각 원소는 유효한 방향키 문자열

2. board: List[int]
   - [가로 크기, 세로 크기]
   - 제약: len(board) == 2
   - 제약: board[i] > 0

[Output]
- result: List[int]
  - [x좌표, y좌표]
  - 제약: -width//2 <= x <= width//2
  - 제약: -height//2 <= y <= height//2
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 방향별 이동 처리 필요 : 방향 벡터 매핑
2. 경계 체크 필요 : 범위 검증 로직
3. 상태 누적 필요 : 좌표 갱신
4. 중앙 기준 좌표계 : 원점 중심 이동
5. 유효성 검사 필요 : 이동 전 검증
"""
"""
[자료구조]
- moves: Dict[str, List[int]]
  - 목적: 방향별 이동 벡터 매핑
  - 특징: O(1) 접근
- position: List[int]
  - 목적: 현재 위치 저장
  - 특징: 2차원 좌표 표현

[알고리즘: Direction Movement]
procedure process_movement(keyinput, board):
    1. Initialize:
       - 방향별 이동 벡터 정의
       - 시작 위치 (0,0)
       - 경계값 계산
    
    2. For each key in keyinput:
       - 다음 위치 계산
       - 경계 체크
       - 유효한 경우 위치 갱신
    
    3. Return 최종 위치
"""

def solution(keyinput, board):
    # 최적화 1: 방향별 이동 벡터를 딕셔너리로 관리
    # @reference/mutable_immutable.py 참조
    moves = {
        "up": [0, 1], 
        "down": [0, -1], 
        "left": [-1, 0], 
        "right": [1, 0]
    }
    
    # 최적화 2: 게임 경계 좌표 계산
    width, height = board[0] // 2, board[1] // 2
    x = y = 0  # 초기 위치
    
    # 최적화 3: 경계 체크 함수 분리
    def is_valid_move(nx, ny):
        return -width <= nx <= width and -height <= ny <= height
    
    # 최적화 4: 각 방향키에 대한 이동 처리
    for key in keyinput:
        dx, dy = moves[key]
        if is_valid_move(x + dx, y + dy):
            x += dx
            y += dy
    
    return [x, y]

# 예시 실행
# print(solution(["left", "right", "up", "right", "right"], [11, 11]))  # [2, 1]
# print(solution(["down", "down", "down", "down", "down"], [7, 9]))    # [0, -4]
