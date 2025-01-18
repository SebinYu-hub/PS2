"""
[Input]
1. maps: List[str]
   - 게임 맵을 나타내는 문자열 배열
   - 'S': 시작 지점
   - 'E': 출구
   - 'L': 레버
   - 'O': 이동 가능
   - 'X': 벽

[Output]
- result: int
  - 시작->레버->출구까지의 최단 시간
  - 도달 불가능: -1 반환
"""

"""
[문제 특징] : [알고리즘 선택 이유]
1. 최단 경로 탐색 필요 : BFS 알고리즘 선택
2. 중간 경유 지점 존재 : 3차원 방문 배열로 레버 상태 관리
3. 격자 기반 이동 : 상하좌우 방향 배열 활용
4. 경로 유효성 검사 : 범위/벽 체크 함수 분리
5. 상태 전이 존재 : 레버 작동 여부에 따른 상태 관리
"""

"""
[자료구조]
1. visited: bool[N][M][2]
   - 3차원 방문 배열
   - [y][x][lever_state]
   - lever_state: 0(미작동), 1(작동)

2. queue: Deque[(y, x, state, time)]
   - BFS를 위한 상태 큐
   - y, x: 현재 위치
   - state: 레버 상태
   - time: 소요 시간

[알고리즘: Multi-state BFS]
procedure find_shortest_path(maps):
    1. Initialize:
       - 시작점, 레버, 출구 위치 찾기
       - 방문 배열과 큐 초기화
    
    2. BFS:
       - 현재 위치에서 4방향 탐색
       - 레버 도달시 상태 변경
       - 출구 도달시 레버 상태 확인
    
    3. Return 최단 시간 or -1
"""

from collections import deque

# 방향 이동을 딕셔너리로 관리하여 가독성과 유지보수성 향상
DIRECTIONS = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

def find_points(maps):
    """시작점, 도착점, 레버 위치를 한 번의 순회로 찾기
    
    Args:
        maps (List[str]): 맵을 나타내는 문자열 리스트
        
    Returns:
        Tuple[Tuple[int, int]]: (시작점, 도착점, 레버) 좌표
    """
    points = {'S': None, 'E': None, 'L': None}
    
    # 리스트 컴프리헨션과 enumerate 활용
    points.update({
        maps[i][j]: (i, j)
        for i, row in enumerate(maps)
        for j, cell in enumerate(row)
        if cell in points
    })
    
    return points['S'], points['E'], points['L']

def is_valid_move(ny, nx, n, m, maps):
    """이동 가능한 좌표인지 판단하는 함수"""
    return 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != "X"

def append_to_queue(ny, nx, k, time, visited, q):
    """방문한 적이 없으면 큐에 넣고 방문 여부 표시"""
    if not visited[ny][nx][k]:
        visited[ny][nx][k] = True
        q.append((ny, nx, k, time + 1))

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
    
    # 시작점, 도착점, 레버 위치를 한 번에 찾기
    start, end, lever = find_points(maps)
    if not all((start, end, lever)):
        return -1  # 필요한 지점이 없는 경우
    
    q = deque([(start[0], start[1], 0, 0)])  # y, x, 레버상태, 시간
    visited[start[0]][start[1]][0] = True

    while q:
        y, x, k, time = q.popleft()
        
        if y == end[0] and x == end[1] and k == 1:
            return time

        # 방향 이동을 더 명확하게 표현
        for dy, dx in DIRECTIONS.values():
            ny, nx = y + dy, x + dx
            
            if not is_valid_move(ny, nx, n, m, maps):
                continue

            # 레버 위치 도달 여부를 좌표 비교로 변경
            if (ny, nx) == lever:
                append_to_queue(ny, nx, 1, time, visited, q)
            else:
                append_to_queue(ny, nx, k, time, visited, q)

    return -1  # 도착 불가능

# 예시 실행
# maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
# print(solution(maps))  # 16
