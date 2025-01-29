"""
[Input]
1. array: List[int]
   - 정수 배열
   - 제약: 1 <= len(array) <= 100
          1 <= array[i] <= 100

2. commands: List[List[int]]
   - 명령어 배열 [[i,j,k], ...]
   - i,j: 부분 배열 범위
   - k: 선택할 위치
   - 제약: 1 <= len(commands) <= 50
          각 command는 [i,j,k] 형태

[Output]
- result: List[int]
  - 각 명령어 실행 결과 배열
  - 제약: len(result) == len(commands)
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 부분 배열 추출 필요 : 슬라이싱으로 효율적 추출
2. 추출한 배열 정렬 필요 : 정렬 후 k번째 원소 선택
3. 여러 명령어 처리 필요 : 리스트 컴프리헨션으로 간단 처리
4. 인덱스 변환 필요 : 1-based를 0-based로 변환
5. 결과 모음 필요 : 각 명령어 결과를 리스트로 수집
"""
"""
[자료구조]
1. Result Array
   - 목적: 각 명령어의 결과 저장
   - 특징: 순차적 결과 수집

[알고리즘: Array Slicing + Sort]
procedure process_commands(array, commands):
    initialize result array
    
    for each command [i,j,k]:
        1. 부분 배열 추출 (i-1 ~ j-1)
        2. 추출한 배열 정렬
        3. k번째 원소 선택 (k-1 인덱스)
        4. 결과 배열에 추가
    
    return result
"""

def solution(array, commands):
    # 최적화 1: list comprehension으로 결과 리스트 생성
    # @reference/list_comprehension.py 참조
    return [
        # 최적화 2: 각 명령어에 대한 처리를 한 줄로 구현
        sorted(array[i-1:j])[k-1]  # i~j까지 자르고 정렬한 후 k번째 수 선택
        for i, j, k in commands
    ]
    # 성능 개선:
    # - 불필요한 임시 변수 제거
    # - 내장 sorted() 함수의 최적화 활용
    # - 리스트 슬라이싱으로 메모리 효율 향상
    # - 인덱스 계산 간소화

# 예시 실행
# print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))  # [5, 6, 3]
# print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3]]))  # [5]
