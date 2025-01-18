"""
[Input]
1. s: str
   - 튜플을 표현하는 문자열
   - 제약: 5 <= len(s) <= 1,000,000
          s는 숫자와 {}, , 로만 구성
          숫자는 1 이상 100,000 이하
          중복된 원소 없음

[Output]
- result: List[int]
  - 튜플을 배열로 변환한 결과
  - 제약: 원소 순서는 집합의 크기 순서대로
         중복 없음
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 문자열 파싱 필요 : 문자열 처리로 집합 추출
2. 집합 크기 순서대로 처리 : 길이 기준 정렬
3. 중복 제거 필요 : 집합(Set) 자료구조 활용
4. 순서 보존 필요 : 등장 순서대로 결과 생성
5. 숫자 변환 필요 : 문자열을 정수로 변환
"""
"""
[자료구조]
1. Set
   - 목적: 중복 원소 제거
   - 특징: O(1) 검색, 중복 방지

2. Sorted Array
   - 목적: 집합 크기 순서로 정렬
   - 특징: 길이 기준 정렬

[알고리즘: String Parsing + Set]
procedure parse_tuple(s):
    remove outer braces
    split into individual sets
    parse each set into numbers
    sort sets by length
    
    initialize seen = empty set
    initialize result = empty list
    
    for each set in sorted sets:
        for number in set:
            if number not in seen:
                add to result
                add to seen
    
    return result
"""

def solution(s):
    # 최적화 1: 문자열 파싱 최적화
    # @reference/string.py 참조
    elements = s[2:-2].split('},{')
    
    # 최적화 2: 각 집합을 파싱하여 숫자 리스트로 변환
    # @performance/for_loop_vs_list_comprehension.py 참조
    parsed = [list(map(int, x.split(','))) for x in elements]
    
    # 최적화 3: 길이 기준 정렬로 순서 결정
    # @reference/sorting_methods_comparison.py 참조
    parsed.sort(key=len)
    
    # 최적화 4: 집합으로 이미 처리한 원소 관리
    seen = set()
    result = []
    
    # 최적화 5: 새로운 원소만 결과에 추가
    for numbers in parsed:
        for num in numbers:
            if num not in seen:
                result.append(num)
                seen.add(num)
    
    return result

# 예시 실행
# print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))  # [2, 1, 3, 4]
# print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))  # [2, 1, 3, 4]
