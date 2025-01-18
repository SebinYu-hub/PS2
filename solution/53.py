"""
[Input]
1. board: List[List[int]]
   - 게임판 정보 (0: 빈칸, 1: 발판)
   - 제약: 1 <= len(board) <= 5
          1 <= len(board[0]) <= 5

2. aloc: List[int]
   - A의 초기 위치 [r, c]
   - 제약: 0 <= r < len(board)
          0 <= c < len(board[0])

3. bloc: List[int]
   - B의 초기 위치 [r, c]
   - 제약: 동일

[Output]
- result: int
  - 두 플레이어가 최적의 플레이를 했을 때 턴의 수
  - 제약: result >= 0
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 두 플레이어의 최적 전략 필요 : 게임 이론(Minimax)으로 최적해 탐색
2. 상하좌우 이동 가능 : 방향 벡터로 이동 처리
3. 발판이 사라지는 효과 : 방문 처리로 상태 관리
4. 이전 상태가 다음 결정에 영향 : 메모이제이션으로 중복 계산 방지
5. 승패 여부와 턴 수 모두 중요 : 상태값을 (승패, 턴수)로 관리
"""
"""
[자료구조]
1. Cache Dictionary
   - 목적: 상태별 결과 저장
   - 특징: O(1) 접근, 메모이제이션

2. Visited Set
   - 목적: 발판 사라짐 관리
   - 특징: O(1) 검색, 상태 추적

[알고리즘: Minimax with Memoization]
procedure play_game(board, aloc, bloc):
    initialize cache, directions
    
    procedure play(curr_pos, other_pos, visited):
        if current_state in cache:
            return cached_result
            
        calculate possible moves
        if no valid moves:
            return (lose, 0)
            
        wins = []
        loses = []
        
        for next_move in possible_moves:
            1. 다음 상태 결과 계산
            2. 승패 여부에 따라 결과 저장
            3. 최적의 결과 선택
        
        cache result
        return optimal_result
    
    return play(aloc, bloc, empty_set)
"""

def solution(board, aloc, bloc):
    # 최적화 1: 상수로 방향과 크기 정의
    ROW, COL = len(board), len(board[0])
    DR, DC = [-1, 0, 1, 0], [0, 1, 0, -1]  # 상우하좌
    
    # 최적화 2: 메모이제이션을 위한 캐시 추가
    # 상태를 (현재 위치, 상대 위치, 방문 상태)로 저장
    cache = {}
    
    # 최적화 3: 유효성 검사와 게임 종료 조건 통합
    def is_valid_move(r, c, visited):
        return (0 <= r < ROW and 
                0 <= c < COL and 
                board[r][c] and 
                (r, c) not in visited)
    
    # 최적화 4: 재귀 함수를 내부에 정의하여 변수 접근 최적화
    def play(curr_pos, other_pos, visited):
        # 최적화 5: 캐시 키 생성
        state = (tuple(curr_pos), tuple(other_pos), tuple(sorted(visited)))
        if state in cache:
            return cache[state]
            
        r, c = curr_pos
        
        # 최적화 6: 현재 위치가 유효하지 않으면 패배
        if not is_valid_move(r, c, visited):
            return False, 0
            
        # 최적화 7: 가능한 모든 이동 미리 계산
        next_moves = [
            (r + dr, c + dc) for dr, dc in zip(DR, DC)
            if is_valid_move(r + dr, c + dc, visited)
        ]
        
        # 최적화 8: 이동할 수 없으면 패배
        if not next_moves:
            return False, 0
            
        # 최적화 9: 승패 결과와 턴 수 계산
        win_turns = []
        lose_turns = []
        
        for next_r, next_c in next_moves:
            # 최적화 10: 다음 상태에서의 결과 계산
            opponent_win, turns = play(
                other_pos,
                [next_r, next_c],
                visited | {(r, c)}
            )
            
            if not opponent_win:
                win_turns.append(turns + 1)
            else:
                lose_turns.append(turns + 1)
        
        # 최적화 11: 최적의 결과 선택
        if win_turns:  # 이길 수 있는 경우
            result = True, min(win_turns)
        else:  # 질 수밖에 없는 경우
            result = False, max(lose_turns) if lose_turns else 0
            
        # 최적화 12: 결과 캐싱
        cache[state] = result
        return result
    
    # 최적화 13: 초기 호출 및 결과 반환
    _, turns = play(aloc, bloc, frozenset())
    return turns

# 예시 실행
# print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]))  # 5
# print(solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [1, 0], [1, 2]))  # 4
