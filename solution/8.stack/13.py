"""
[Input]
1. board: list[list[int]]
   - N x N 크기의 인형뽑기 기계 상태
   - 제약: 5 ≤ N ≤ 30
   - 제약: board[i][j]는 0(빈칸) 또는 1~100(인형 번호)

2. moves: list[int]
   - 크레인 작동 위치가 담긴 배열
   - 제약: 1 ≤ len(moves) ≤ 1,000
   - 제약: moves의 원소는 1 이상 N 이하

[Output]
- result: int
  - 사라진 인형의 개수
  - 제약: 같은 인형 두 개가 연속으로 쌓이면 사라짐
  - 제약: 사라진 인형은 2개씩 카운트
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 열 단위 접근 필요 : 2차원 배열 전처리
2. 인형 쌓기 필요 : 스택 자료구조 활용
3. 효율적 연산 필요 : deque로 최적화
4. 상태 관리 필요 : 바구니 스택으로 관리
5. 중복 제거 필요 : 스택의 top 비교
"""
"""
[자료구조]
1. columns: list[deque]
   - 목적: 각 열의 인형 상태 저장
   - 특징: 위에서부터 접근 가능
   - 연산: pop(), append()

2. basket: deque
   - 목적: 뽑은 인형 저장
   - 특징: LIFO 구조
   - 연산: pop(), append()

[알고리즘: Crane Game]
procedure solution(board, moves):
    1. Preprocess:
       - board를 열 단위로 재구성
       - 빈 칸 제외하고 deque로 변환
    
    2. Process moves:
       - 각 move에 대해:
         a) 해당 열에서 인형 뽑기
         b) 바구니 top과 비교
         c) 같으면 제거하고 카운트 증가
    
    3. Return result:
       - 제거된 인형 수 반환
"""

from collections import deque

def solution(board, moves):
    # 예시 입력값: board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    #            moves = [1,5,3,5,1,2,1,4]
    
    n = len(board)
    # 각 열의 인형을 스택으로 변환 (전처리)
    # list comprehension과 deque를 활용하여 최적화
    columns = [deque(board[i][j] for i in range(n-1, -1, -1) if board[i][j])
              for j in range(n)]
    result = 0
    basket = deque()  # 바구니 스택
    
    # 크레인 이동 처리
    for move in moves:
        col = move - 1  # 0-based 인덱스로 변환
        
        # 해당 열에 인형이 있는 경우
        if columns[col]:
            doll = columns[col].pop()  # 인형 뽑기
            
            # 바구니가 비어있지 않고, 마지막 인형과 같은 경우
            if basket and basket[-1] == doll:
                basket.pop()  # 인형 터트리기
                result += 2   # 터진 인형 개수 추가
            else:
                basket.append(doll)  # 새 인형 추가
    
    return result

# 예시 실행과 과정 설명
# board = [
#     [0,0,0,0,0],
#     [0,0,1,0,3],
#     [0,2,5,0,1],
#     [4,2,4,4,2],
#     [3,5,1,3,1]
# ]
# moves = [1,5,3,5,1,2,1,4]
# 실행 과정:
# 1. 전처리: 각 열을 스택으로 변환
#    col1: [3,4], col2: [5,2,2], col3: [1,4,5,1], col4: [3,4], col5: [1,2,3]
# 2. moves 순회:
#    1번 열(4) -> basket: [4]
#    5번 열(1) -> basket: [4,1]
#    3번 열(1) -> basket: [4,1,1]
#    5번 열(2) -> basket: [4,1,1,2]
#    1번 열(3) -> basket: [4,1,1,2,3]
#    2번 열(2) -> basket: [4,1,1,2,3,2]
#    1번 열() -> basket: [4,1,1,2,3,2]
#    4번 열(4) -> basket: [4,1,1,2,3,2,4]
# 결과: 4 (2쌍의 인형이 터짐)
# print(solution(board, moves))  # 4
