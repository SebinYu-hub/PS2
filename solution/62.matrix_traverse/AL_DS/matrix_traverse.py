"""
[Matrix Traverse의 핵심 개념 정리]

1. 기본 패턴
- 순차적 접근: 2차원 배열을 행/열 기준으로 순회
- 인덱스 매핑: (i,j) 좌표를 활용한 위치 접근  
- 방향 벡터: dx, dy (또는 dr, dc) 배열을 통한 이동 제어

2. 주요 연산 패턴
a) 회전 (Rotation) - @62.py
   # 90도 회전 공식
   new_row = j
   new_col = N-1-i

b) 행렬 곱셈 (Multiplication) - @63.py
   # 행렬 곱셈 핵심
   result[i][j] = sum(A[i][k] * B[k][j] for k in range(N))

c) 나선형 순회 (Spiral) - @64.py
   # 방향 벡터를 통한 이동
   dr = [0, 1, 0, -1]  # 우,하,좌,상
   dc = [1, 0, -1, 0]

3. 핵심 최적화 기법
a) 메모리 최적화
   - List comprehension을 활용한 2차원 배열 초기화
   - 불필요한 중간 배열 생성 최소화

b) 연산 최적화
   - 방향 전환: d = (d + 1) % 4
   - 경계 조건 검사: 0 <= nx < N and 0 <= ny < N
   - 인덱스 매핑 공식 활용

c) 코드 구조 최적화
   - 내부 함수 정의로 변수 접근 최적화
   - 모듈화된 함수 구현으로 재사용성 확보

4. 시간 복잡도
- 기본 순회: O(N²)
- 행렬 곱셈: O(N³) 
- 회전/전치: O(N²)
"""

# 예시 코드 구현
def matrix_traverse_example():
    # 1. 기본 순회
    def basic_traverse(matrix):
        N = len(matrix)
        for i in range(N):
            for j in range(N):
                # 행/열 기준 순차 접근
                process(matrix[i][j])
    
    # 2. 방향 벡터를 이용한 순회
    def direction_traverse(matrix):
        dr = [0, 1, 0, -1]  # 방향 벡터 정의
        dc = [1, 0, -1, 0]
        r = c = d = 0  # 현재 위치와 방향
        
        # 다음 위치 계산 및 이동
        nr, nc = r + dr[d], c + dc[d]
    
    # 3. 회전 연산
    def rotate_90(matrix):
        N = len(matrix)
        result = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                result[j][N-1-i] = matrix[i][j]
        return result

    # 4. 행렬 곱셈
    def multiply(A, B):
        N = len(A)
        result = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                result[i][j] = sum(A[i][k] * B[k][j] for k in range(N))
        return result

    return "Matrix traverse examples implemented" 