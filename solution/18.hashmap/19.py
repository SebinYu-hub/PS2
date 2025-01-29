"""
[Input]
1. strings: list[str]
   - 문자열 배열
   - 제약: 1 ≤ len(strings) ≤ 100,000
   - 제약: 1 ≤ len(strings[i]) ≤ 100

2. queries: list[str]
   - 검색할 문자열 배열
   - 제약: 1 ≤ len(queries) ≤ 100,000
   - 제약: 1 ≤ len(queries[i]) ≤ 100

[Output]
- result: list[bool]
  - 각 쿼리 문자열이 strings에 있는지 여부
  - 제약: len(result) == len(queries)
  - 제약: 대소문자 구분
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 문자열 검색 필요 : 해시 함수 활용
2. 빠른 검색 필요 : 해시 테이블 O(1) 검색
3. 충돌 회피 필요 : 다항식 해시 함수 사용
4. 대규모 데이터 처리 필요 : 모듈러 연산 활용
5. 메모리 효율성 필요 : 해시값만 저장
"""
"""
[자료구조]
1. hash_list: set
   - 목적: 문자열의 해시값 저장
   - 특징: O(1) 시간 검색
   - 연산: add(), in

[알고리즘: String Hashing]
procedure solution(strings, queries):
    1. Initialize:
       - 해시 함수 정의 (다항식 해시)
       - strings의 해시값 계산 및 저장
    
    2. Process queries:
       - 각 쿼리 문자열에 대해:
         a) 해시값 계산
         b) 해시값이 hash_list에 있는지 확인
    
    3. Return result:
       - 각 쿼리의 검색 결과 반환
"""

def polynomial_hash(string):
    """
    다항식 해시 함수 구현
    - p: 31 (소수, 알파벳 26개보다 큰 소수 선택)
    - m: 10^9 + 7 (큰 소수로 모듈로 연산)
    """
    p = 31  # 알파벳 26개보다 큰 소수
    m = 1_000_000_007  # 모듈로 연산에 사용할 큰 소수
    hash_value = 0
    
    # 각 문자를 순회하며 해시값 계산
    # hash = (s[0]*p^(n-1) + s[1]*p^(n-2) + ... + s[n-1]) mod m
    for char in string:
        hash_value = (hash_value * p + ord(char)) % m
        
    return hash_value

def solution(strings, queries):
    # 문자열 배열의 해시값을 미리 계산
    hash_list = {polynomial_hash(s) for s in strings}
    
    # 각 쿼리 문자열에 대해 해시값을 계산하고 존재 여부 확인
    result = [polynomial_hash(query) in hash_list for query in queries]
    
    return result

# 예시 실행
# print(solution(["apple", "banana", "cherry"], ["banana", "kiwi", "melon", "apple"]))
# 출력: [True, False, False, True]
