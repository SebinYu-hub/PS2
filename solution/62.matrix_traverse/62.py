"""
[Input]
1. arr: List[List[int]]
   - N x N 2차원 배열
   - 제약: N > 0

2. n: int
   - 회전할 횟수
   - 제약: n >= 0

[Output]
- result: List[List[int]]
  - 회전된 2차원 배열
  - 제약: len(result) == len(arr)
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 2차원 배열의 회전 연산 : 인덱스 매핑 필요
2. 회전 횟수에 따른 반복 : 회전 연산 재사용
3. 원본 배열 보존 필요 : 깊은 복사 사용
4. 정사각 행렬 처리 : N x N 크기 활용
5. 인덱스 변환 필요 : 수학적 공식 적용
"""
"""
[자료구조]
- result: List[List[int]]
  - 목적: 회전된 배열 저장
  - 특징: O(1) 인덱스 접근

[알고리즘: Matrix Rotation]
procedure rotate_matrix(arr, n):
    procedure rotate_90(matrix):
        1. 결과 배열 초기화 (N x N)
        2. 각 위치별 회전 인덱스 계산:
           - new_col = N-1-row
           - new_row = col
        3. 회전된 배열 반환
    
    1. 입력 배열 복사
    2. n회 만큼 rotate_90 호출
    3. 최종 결과 반환
"""

def solution(arr, n):
    # 최적화 1: 회전 함수를 내부에 정의하여 변수 접근 최적화
    def rotate_90(matrix):
        N = len(matrix)
        # 최적화 2: list comprehension으로 결과 배열 초기화
        # @reference/list_comprehension.py 참조
        result = [[0] * N for _ in range(N)]
        
        # 최적화 3: 90도 회전을 위한 인덱스 매핑
        for i in range(N):
            for j in range(N):
                # 최적화 4: 회전 공식 적용 (i,j) -> (j,N-1-i)
                result[j][N-1-i] = matrix[i][j]
        
        return result
    
    # 최적화 5: 입력 배열 복사하여 원본 보존
    # @reference/mutable_immutable.py 참조
    result = arr.copy()
    
    # 최적화 6: 지정된 횟수만큼 회전
    for _ in range(n):
        result = rotate_90(result)
    
    return result

# 예시 실행
# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]
# print(solution(matrix, 1))  # 90도 회전
# print(solution(matrix, 2))  # 180도 회전
