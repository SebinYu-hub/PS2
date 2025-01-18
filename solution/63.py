"""
[Input]
1. matrix1: List[List[int]]
   - 3x3 행렬
   - 제약: len(matrix1) == 3, len(matrix1[i]) == 3

2. matrix2: List[List[int]]
   - 3x3 행렬
   - 제약: len(matrix2) == 3, len(matrix2[i]) == 3

[Output]
- result: List[List[int]]
  - 행렬 곱셈 후 전치된 3x3 행렬
  - 제약: len(result) == 3, len(result[i]) == 3
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 행렬 곱셈 연산 필요 : 3중 반복문 사용
2. 전치 행렬 변환 필요 : 행/열 교환 연산
3. 3x3 고정 크기 : 최적화된 연산 가능
4. 중간 결과 저장 필요 : 임시 배열 사용
5. 독립적인 연산 처리 : 모듈화된 함수 구현
"""
"""
[자료구조]
- result: List[List[int]]
  - 목적: 연산 결과 저장
  - 특징: O(1) 인덱스 접근

[알고리즘: Matrix Operations]
procedure matrix_multiply_transpose(matrix1, matrix2):
    procedure multiply(A, B):
        1. 결과 행렬 초기화 (3x3)
        2. 행렬 곱셈 수행:
           result[i][j] = sum(A[i][k] * B[k][j])
        3. 곱셈 결과 반환

    procedure transpose(matrix):
        1. 행과 열 교환:
           result[i][j] = matrix[j][i]
        2. 전치 행렬 반환

    1. 행렬 곱셈 수행
    2. 결과 행렬 전치
    3. 최종 결과 반환
"""

def multiply_matrices(A, B):
    # 최적화 1: list comprehension으로 결과 행렬 초기화
    # @reference/list_comprehension.py 참조
    result = [[0] * 3 for _ in range(3)]
    
    # 최적화 2: 3x3 행렬 곱셈 최적화
    for i in range(3):
        for j in range(3):
            # 최적화 3: 행렬 곱셈 계산을 sum으로 간소화
            result[i][j] = sum(A[i][k] * B[k][j] for k in range(3))
    
    return result

def transpose_matrix(matrix):
    # 최적화 4: list comprehension으로 전치 행렬 생성
    return [[matrix[j][i] for j in range(3)] for i in range(3)]

def solution(matrix1, matrix2):
    # 최적화 5: 행렬 곱셈 후 전치 행렬 계산
    multiplied = multiply_matrices(matrix1, matrix2)
    return transpose_matrix(multiplied)

# 예시 실행
# matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
# print(solution(matrix1, matrix2))
