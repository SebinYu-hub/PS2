"""
[Input]
1. numbers: list[int]
   - 정수 배열
   - 제약: 0 ≤ numbers[i] ≤ 100
   - 제약: 1 ≤ len(numbers) ≤ 100

[Output]
- result: list[int]
  - 두 수의 합으로 만들 수 있는 모든 수를 오름차순으로 정렬한 배열
  - 제약: 중복된 값 없음
  - 제약: 오름차순 정렬
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 모든 조합 생성 필요 : itertools.combinations 활용
2. 중복 제거 필요 : set 자료구조 활용
3. 정렬 필요 : sorted() 함수 활용
4. 두 수의 합 계산 필요 : set comprehension으로 최적화
5. 메모리 효율성 필요 : generator 활용 가능
"""
"""
[자료구조]
1. pairs: iterator
   - 목적: 두 수의 모든 조합 저장
   - 특징: combinations 객체로 메모리 효율적

2. sums: set
   - 목적: 중복 없는 합계 저장
   - 특징: 해시 테이블 기반 O(1) 검색

[알고리즘: Sum Combinations]
procedure solution(numbers):
    1. Generate combinations:
       - numbers에서 2개씩 조합 생성
       - combinations(numbers, 2) 활용
    
    2. Calculate sums:
       - 각 조합의 합 계산
       - set comprehension으로 중복 제거
    
    3. Sort results:
       - 합계를 오름차순 정렬
    
    4. Return sorted unique sums
"""

from itertools import combinations

def solution(numbers):
    # 예시 입력값: numbers = [2, 1, 3, 4, 1]
    
    # 최적화 1: combinations 활용하여 모든 2개 조합 생성
    pairs = combinations(numbers, 2)
    
    # 최적화 2: set comprehension으로 합 계산 및 중복 제거
    sums = {x + y for x, y in pairs}
    
    # 최적화 3: sorted()로 한 번에 정렬
    return sorted(sums)

# TEST 코드입니다
print(solution([2, 1, 3, 4, 1])) # 반환값 : [2, 3, 4, 5, 6, 7]
print(solution([5, 0, 2, 7])) # 반환값 : [2, 5, 7, 9, 12]