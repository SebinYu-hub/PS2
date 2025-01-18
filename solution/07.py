"""
[Input]
1. dirs: str
   - 이동 명령어들의 나열
   - 제약: 1 ≤ len(dirs) ≤ 500
   - 제약: dirs는 'U', 'D', 'R', 'L'로만 구성

[Output]
- result: int
  - 처음 걸어본 길의 길이
  - 제약: 좌표평면의 경계를 넘어가는 명령어는 무시
  - 제약: 이미 걸었던 길은 중복 카운트하지 않음
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 경로 중복 제거 필요 : set 자료구조 활용
2. 양방향 경로 처리 필요 : 시작점과 도착점 모두 저장
3. 좌표 이동 필요 : 방향 벡터(dx, dy) 활용
4. 범위 검사 필요 : 좌표 유효성 검증
5. 경로 저장 필요 : 튜플로 경로 표현
"""
"""
[자료구조]
1. visited: set
   - 목적: 방문한 경로 저장
   - 특징: 중복 경로 자동 제거
   - 형태: {(x1,y1,x2,y2), ...}

2. moves: dict
   - 목적: 방향별 이동 벡터 저장
   - 특징: O(1) 시간 접근
   - 형태: {'U': (dx,dy), ...}

[알고리즘: Path Tracking]
procedure solution(dirs):
    1. Initialize:
       - 시작 위치 설정
       - 방향별 이동 벡터 정의
       - 방문 경로 set 생성
    
    2. Process commands:
       - 각 명령어에 대해:
         a) 다음 위치 계산
         b) 범위 검증
         c) 유효한 경우 양방향 경로 저장
    
    3. Calculate result:
       - 중복 제거된 경로 수 반환
       - visited 크기의 절반 (양방향 고려)
"""

def solution(dirs):
    # 예시 입력값: dirs = "ULURRDLLU"
    
    # 방향별 이동 매핑
    moves = {
        'U': (0, 1),
        'D': (0, -1),
        'L': (-1, 0),
        'R': (1, 0)
    }
    
    # 방문한 경로를 저장할 set (시작점, 도착점)
    visited = set()
    x, y = 0, 0  # 현재 위치
    
    for direction in dirs:
        # 다음 위치 계산
        dx, dy = moves[direction]
        nx, ny = x + dx, y + dy
        
        # 범위 체크 (좌표평면은 -5에서 5까지)
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            # 양방향 경로를 모두 저장 (A->B와 B->A는 같은 경로)
            visited.add((x, y, nx, ny))
            visited.add((nx, ny, x, y))
            x, y = nx, ny  # 위치 업데이트
    
    # 총 경로의 개수는 중복을 제거한 후 절반으로 나눔
    return len(visited) // 2

# 예시 실행
# print(solution("ULURRDLLU"))  # 7
# print(solution("LULLLLLLU"))  # 7
