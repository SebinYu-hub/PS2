"""
[Input]
1. phone_book: List[str]
   - 전화번호 문자열들의 배열
   - 1 ≤ len(phone_book) ≤ 1,000,000
   - 각 전화번호 길이는 1 이상 20 이하
   - 숫자로만 구성

[Output]
- result: bool
  - 어떤 번호가 다른 번호의 접두어인 경우 False
  - 그렇지 않으면 True
"""

"""
[문제 특징] : [알고리즘 선택 이유]
1. 접두어 검사 필요 : 문자열 정렬로 유사 접두어 인접
2. 효율적 비교 필요 : 인접한 두 문자열만 비교
3. 문자열 처리 : startswith 메서드 활용
4. 전체 순회 필요 : O(N) 시간복잡도
5. 메모리 제약 : 추가 공간 최소화
"""

"""
[자료구조]
1. sorted_phones: List[str]
   - 정렬된 전화번호 목록
   - 접두어 관계 확인을 위한 정렬

[알고리즘: String Prefix Check]
procedure check_prefixes(phone_book):
    1. Initialize:
       - 전화번호 목록 정렬
    
    2. For each adjacent pair:
       - 현재 번호가 다음 번호의 접두어인지 확인
       - True면 False 반환
    
    3. Return True if no prefix found
"""


def solution(phone_book):
    # 최적화 1: 정렬을 통한 비교 횟수 최소화
    # ["119", "97674223", "1195524421"]  # 정렬 전
    # ["119", "1195524421", "97674223"]  # 정렬 후
    phone_book.sort()
    
    # 최적화 2: zip을 활용한 인접 요소 비교
    # range와 인덱싱 대신 zip으로 더 파이썬스러운 코드
    for curr, next in zip(phone_book, phone_book[1:]):
        if next.startswith(curr):
            return False
            
    return True

# TEST 코드입니다
# print(solution(["119", "97674223", "1195524421"]))  # False
# print(solution(["123","456","789"]))  # True
# print(solution(["12","123","1235","567","88"]))  # False
