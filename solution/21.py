"""
[Input]
1. want: list[str]
   - 원하는 제품 목록
   - 제약: 1 ≤ len(want) ≤ 10
   - 제약: 1 ≤ len(want[i]) ≤ 10

2. number: list[int]
   - 각 제품의 원하는 수량
   - 제약: len(number) == len(want)
   - 제약: 1 ≤ number[i] ≤ 10

3. discount: list[str]
   - 할인 제품 목록
   - 제약: 10 ≤ len(discount) ≤ 100,000
   - 제약: discount[i]는 want의 요소들로만 구성

[Output]
- result: int
  - 원하는 제품을 모두 할인 받을 수 있는 회원등록 날짜의 수
  - 제약: 연속된 10일 동안의 할인 제품으로 판단
  - 제약: 0 ≤ result ≤ len(discount) - 9
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 연속 구간 처리 필요 : 슬라이딩 윈도우 활용
2. 빈도수 계산 필요 : Counter 클래스 활용
3. 효율적 비교 필요 : defaultdict로 자동 초기화
4. 윈도우 이동 필요 : Counter 연산 최적화
5. 상태 관리 필요 : 현재 윈도우 상태 추적
"""
"""
[자료구조]
1. want_dict: defaultdict
   - 목적: 원하는 제품과 수량 저장
   - 특징: 키 없을 때 자동 0 할당
   - 연산: 딕셔너리 연산

2. current_items: Counter
   - 목적: 현재 윈도우의 제품 수량
   - 특징: 해시 테이블 기반
   - 연산: 증감 연산

[알고리즘: Discount Window]
procedure solution(want, number, discount):
    1. Initialize:
       - want_dict 생성 및 초기화
       - 첫 10일 윈도우 카운트
    
    2. Process windows:
       - 각 윈도우에 대해:
         a) 현재 상태가 want_dict와 일치하는지 확인
         b) 윈도우 한 칸 이동
         c) Counter 업데이트
    
    3. Return result:
       - 조건을 만족하는 날짜 수 반환
"""

from collections import Counter, defaultdict

def solution(want, number, discount):
    # 최적화 1: 원하는 제품과 수량을 defaultdict로 관리
    want_dict = defaultdict(int)
    for w, n in zip(want, number):
        want_dict[w] = n
    
    answer = 0
    # 처적화 2: 처음 10일간의 할인 상품 카운트
    current_items = Counter(discount[:10])
    
    # 최적화 3: 첫 10일 검사
    if current_items == Counter(want_dict):
        answer += 1
    
    # 최적화 4: 슬라이딩 윈도우로 다음 날짜들 확인
    for i in range(len(discount) - 10):
        # 최적화 5: 윈도우의 첫 상품은 제거하고 새 상품 추가
        current_items[discount[i]] -= 1
        if current_items[discount[i]] == 0:
            del current_items[discount[i]]
        current_items[discount[i + 10]] += 1
        
        # 최적화 6: 현재 할인 상품이 원하는 제품과 수량이 일치하는지 확인
        if current_items == Counter(want_dict):
            answer += 1
    
    return answer

# 예시 실행
# print(solution(["banana", "apple", "rice", "pork", "pot"], 
#               [3, 2, 2, 2, 1], 
#               ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))  # 3
