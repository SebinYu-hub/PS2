"""
[Input]
1. n: int
   - 달팽이 배열의 크기
   - 제약: n > 0

[Output]
- result: List[List[int]]
  - n x n 크기의 달팽이 모양 배열
  - 제약: len(result) == n, len(result[i]) == n
  - 제약: 1부터 n*n까지의 숫자가 달팽이 모양으로 채워짐
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 방향 전환이 필요한 순회 : 방향 벡터 배열 사용
2. 범위 체크가 필요한 이동 : 경계 조건 검사
3. 이미 방문한 칸 체크 필요 : 방문 여부로 방향 전환
4. 순차적 숫자 채우기 : 증가하는 카운터 사용
5. 2차원 배열 조작 필요 : 인덱스 기반 접근
"""
"""
[자료구조]
- snail: List[List[int]]
  - 목적: 달팽이 모양 숫자 저장
  - 특징: O(1) 인덱스 접근
- directions: List[Tuple[int, int]]
  - 목적: 이동 방향 벡터 저장
  - 특징: 순환적 방향 전환 용이

[알고리즘: Spiral Traversal]
procedure fill_snail(n):
    1. Initialize:
       - n x n 배열 생성
       - 방향 벡터 정의 (우,하,좌,상)
       - 시작 위치 (0,0)과 방향 설정
    
    2. While 숫자 < n*n:
       - 현재 위치에 숫자 채움
       - 다음 위치 계산
       - if 다음 위치가 유효하지 않거나 이미 채워짐:
           - 방향 전환
           - 다음 위치 재계산
       - 위치 이동
    
    3. Return 완성된 배열
"""

def solution(n):
    # 최적화 1: list comprehension으로 결과 배열 초기화
    # @reference/list_comprehension.py 참조
    snail = [[0] * n for _ in range(n)]
    
    # 최적화 2: 방향 벡터 정의 (우,하,좌,상)
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    
    # 최적화 3: 초기 위치와 방향 설정
    r = c = d = 0  # 행, 열, 방향
    num = 1  # 채울 숫자
    
    # 최적화 4: 모든 칸을 채울 때까지 반복
    while num <= n * n:
        # 현재 위치에 숫자 채우기
        snail[r][c] = num
        num += 1
        
        # 다음 위치 계산
        nr, nc = r + dr[d], c + dc[d]
        
        # 최적화 5: 방향 전환 조건 검사
        if not (0 <= nr < n and 0 <= nc < n and snail[nr][nc] == 0):
            d = (d + 1) % 4  # 방향 전환
            nr, nc = r + dr[d], c + dc[d]
        
        r, c = nr, nc
    
    return snail

# 예시 실행
# print(solution(3))  # [[1,2,3],[8,9,4],[7,6,5]]
# print(solution(4))  # [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]
