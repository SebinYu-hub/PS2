"""
[Input]
1. numbers: List[int]
   - 0 또는 양의 정수로 이루어진 배열
   - 제약: 1 <= len(numbers) <= 100,000
          0 <= numbers[i] <= 1,000

[Output]
- result: str
  - 가장 큰 수를 만드는 문자열
  - 제약: 모든 숫자를 사용해야 함
         결과가 0인 경우 "0" 반환
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 숫자를 문자열로 비교해야 함 : 문자열 비교로 정렬 기준 설정
2. 모든 숫자 조합 고려 필요 : 커스텀 비교 함수로 정렬
3. 특별한 비교 로직 필요 : functools.cmp_to_key 활용
4. 예외 케이스 처리 필요 : 모든 숫자가 0인 경우 처리
5. 문자열 연결 최적화 필요 : join 메서드로 효율적 연결
"""
"""
[자료구조]
1. Sorted Array
   - 목적: 특별한 규칙으로 정렬된 숫자 저장
   - 특징: 커스텀 비교 함수 적용

[알고리즘: Custom Sort]
procedure find_largest_number(numbers):
    define compare function(a, b):
        return int(b+a) - int(a+b)
    
    sort numbers using compare function
    join sorted numbers to string
    
    if result starts with '0':
        return "0"
    return result
"""

import functools

def solution(numbers):
    # 최적화 1: 비교 함수를 내부에 정의하여 변수 접근 최적화
    def compare(a, b):
        # 최적화 2: 문자열 결합으로 직접 비교
        t1, t2 = str(a) + str(b), str(b) + str(a)
        # 최적화 3: 삼항 연산자로 비교 결과 반환
        return (int(t1) > int(t2)) - (int(t1) < int(t2))
    
    # 최적화 4: functools.cmp_to_key로 커스텀 정렬 구현
    # @reference/sorting_methods_comparison.py 참조
    sorted_nums = sorted(numbers, key=functools.cmp_to_key(compare), reverse=True)
    
    # 최적화 5: 문자열 결합과 예외 처리를 한 번에 처리
    # @performance/string_concatenation_performance.py 참조
    answer = ''.join(map(str, sorted_nums))
    return '0' if answer[0] == '0' else answer

# 예시 실행
# print(solution([6, 10, 2]))  # "6210"
# print(solution([3, 30, 34, 5, 9]))  # "9534330"
