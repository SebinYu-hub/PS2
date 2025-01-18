"""
[Input]
1. n: int
   - 정수
   - 제약: 1 <= n <= 8,000,000,000
          자연수

[Output]
- result: int
  - 각 자릿수를 내림차순으로 정렬한 정수
  - 제약: result는 n의 자릿수를 재배열한 수
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 각 자릿수를 분리해야 함 : 문자열 변환으로 자릿수 접근
2. 내림차순 정렬 필요 : 정렬 후 역순 배치
3. 결과를 다시 숫자로 변환 : int 변환으로 최종 결과 생성
4. 자릿수 순서 변경 가능 : 모든 자릿수를 독립적으로 처리
5. 정렬 방향이 고정됨 : 단순 내림차순 정렬 사용
"""
"""
[자료구조]
1. Digit Array
   - 목적: 각 자릿수 저장 및 정렬
   - 특징: 문자열/리스트 변환으로 처리

[알고리즘: String Sort]
procedure sort_digits(n):
    convert number to string
    convert string to list of digits
    sort digits in descending order
    join digits
    convert back to integer
    return result
"""

def solution(n):
    # 최적화 1: 정수를 문자열로 변환하고 리스트로 분리
    # @reference/list_comprehension.py 참조
    digits = list(str(n))
    
    # 최적화 2: 내림차순 정렬로 가장 큰 수 생성
    # @performance/sorting_methods_comparison.py 참조
    digits.sort(reverse=True)
    
    # 최적화 3: join으로 문자열 결합 후 정수로 변환
    # @performance/string_concatenation_performance.py 참조
    return int(''.join(digits))

# 예시 실행
# print(solution(118372))  # 873211
# print(solution(12345))   # 54321
