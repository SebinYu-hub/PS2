"""
[Input]
1. strings: List[str]
   - 문자열 배열
   - 제약: 1 <= len(strings) <= 50
          1 <= len(strings[i]) <= 100

2. n: int
   - 정렬 기준이 되는 인덱스
   - 제약: 0 <= n < len(strings[i])

[Output]
- result: List[str]
  - n번째 문자를 기준으로 정렬된 문자열 배열
  - 제약: len(result) == len(strings)
         n번째 문자가 같은 문자열은 사전순으로 정렬
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 특정 인덱스 기준 정렬 : 커스텀 정렬 키 함수 사용
2. 동일 문자일 때 사전순 정렬 : 튜플로 다중 정렬 조건 구현
3. 문자열 비교 연산 필요 : 파이썬 문자열 비교 활용
4. 원본 배열 순서 변경 : 안정 정렬 특성 활용
5. 정렬 기준이 두 가지 : 정렬 키를 (n번째 문자, 전체 문자열)로 구성
"""
"""
[자료구조]
1. Sorted Array
   - 목적: 정렬된 결과 저장
   - 특징: 다중 정렬 조건 적용

[알고리즘: Custom Sort]
procedure sort_strings(strings, n):
    define key function:
        return (string[n], string)
    
    return sorted(strings, key=key_function)
"""

def solution(strings, n):
    # 최적화 1: sorted()와 lambda를 활용하여 다중 조건 정렬 구현
    # 1. n번째 문자를 첫 번째 정렬 기준으로
    # 2. 전체 문자열을 두 번째 정렬 기준으로 사용
    return sorted(strings, key=lambda x: (x[n], x))
    # 성능 개선: 
    # - 튜플 키로 한 번의 정렬로 두 조건 모두 처리
    # - 불필요한 임시 리스트 생성 방지
    # - 내장 sorted() 함수의 최적화된 정렬 알고리즘 활용

# 예시 실행
# print(solution(["sun", "bed", "car"], 1))  # ["car", "bed", "sun"]
# print(solution(["abce", "abcd", "cdx"], 2))  # ["abcd", "abce", "cdx"]