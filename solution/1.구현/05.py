"""
[Input]
1. arr1: list[list[int]]
   - 첫 번째 행렬
   - 제약: 2 ≤ len(arr1) ≤ 100
   - 제약: arr1의 모든 행의 길이는 동일
   - 제약: -10 ≤ arr1[i][j] ≤ 20

2. arr2: list[list[int]]
   - 두 번째 행렬
   - 제약: arr1의 열 수 = arr2의 행 수
   - 제약: 2 ≤ len(arr2[0]) ≤ 100
   - 제약: -10 ≤ arr2[i][j] ≤ 20

[Output]
- result: list[list[int]]
  - 두 행렬의 곱셈 결과
  - 제약: result[i][j]는 정수
  - 제약: result의 크기는 arr1의 행 수 × arr2의 열 수
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 행렬 곱셈 연산 필요 : zip() 함수로 열 단위 접근
2. 중첩 반복 처리 필요 : list comprehension으로 최적화
3. 행/열 변환 필요 : zip(*matrix)로 전치 행렬 생성
4. 내적 계산 필요 : sum과 zip으로 효율적 계산
5. 다차원 데이터 처리 필요 : 중첩 list comprehension 활용
"""
"""
[자료구조]
1. matrix_rows: list[list[int]]
   - 목적: 첫 번째 행렬의 행들 저장
   - 특징: 2차원 리스트로 행 단위 접근

2. matrix_cols: zip object
   - 목적: 두 번째 행렬의 열들 저장
   - 특징: zip 객체로 메모리 효율적 접근

[알고리즘: Matrix Multiplication]
procedure solution(arr1, arr2):
    1. Transform arr2:
       - arr2를 전치하여 열 단위 접근 준비
       - zip(*arr2) 활용
    
    2. Calculate products:
       - 각 행과 열의 내적 계산
       - sum(a*b for a,b in zip(row,col))
    
    3. Build result matrix:
       - 중첩 list comprehension으로 결과 행렬 생성
       - 각 위치의 내적 결과 저장
"""

def solution(arr1, arr2):
    # 예시 입력값: arr1 = [[1, 2], [3, 4]], arr2 = [[5, 6], [7, 8]]
    
    # zip(*arr2)로 arr2의 열을 쉽게 추출
    # arr2: [[5, 6], [7, 8]] -> zip(*arr2): [(5, 7), (6, 8)]
    
    return [[sum(a * b for a, b in zip(row, col)) 
            for col in zip(*arr2)]    # 각 열과의 곱셈 합 계산
            for row in arr1]          # 각 행에 대해 반복
    
    # 계산 과정:
    # row = [1, 2]일 때:
    #   col = (5, 7) -> 1*5 + 2*7 = 19
    #   col = (6, 8) -> 1*6 + 2*8 = 22
    # row = [3, 4]일 때:
    #   col = (5, 7) -> 3*5 + 4*7 = 43
    #   col = (6, 8) -> 3*6 + 4*8 = 50
    # 최종 결과: [[19, 22], [43, 50]]

# 예시 실행
print(solution([[1, 2], [3, 4]], [[5, 6], [7, 8]]))  # [[19, 22], [43, 50]]