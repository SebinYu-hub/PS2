from collections import defaultdict

"""
[Input]
1. enroll: List[str]
   - 판매원들의 이름 목록
   - 순서: 조직에 참여한 순서
   
2. referral: List[str]
   - 각 판매원의 추천인 목록
   - "-": 민호(root)를 의미
   
3. seller: List[str]
   - 판매 기록의 판매원 이름
   
4. amount: List[int]
   - 판매 기록의 판매량
   - 100원 단위로 환산 필요

[Output]
- result: List[int]
  - 각 판매원이 얻은 총 수익
  - enroll 순서와 동일하게 반환
"""

"""
[문제 특징] : [알고리즘 선택 이유]
1. 트리 구조의 상향식 탐색 필요 : 부모 노드 참조가 필요하므로 parent 딕셔너리 사용
2. 수익 분배 규칙이 재귀적 : Bottom-up 방식으로 구현
3. 판매원별 누적 수익 관리 : defaultdict로 합산 관리
4. 빈번한 조회/갱신 연산 : 해시 테이블(딕셔너리) 사용으로 O(1) 접근
5. 정확한 소수점 계산 필요 : 정수 연산으로 변환하여 처리
"""

"""
[자료구조]
1. parent: Dict[str, str]
   - key: 현재 노드(판매원)
   - value: 부모 노드(추천인)
   예) {"john": "-", "mary": "john"}

2. total: DefaultDict[str, int]
   - key: 노드(판매원)
   - value: 누적 수익
   예) {"john": 360, "mary": 100}

[알고리즘: Bottom-up Revenue Distribution]
procedure distribute_revenue(seller, amount):
    1. Initialize:
       - parent 관계 구축
       - 수익 누적용 defaultdict 생성
    
    2. For each sale record:
       - 현재 노드부터 시작
       - 수익의 10%를 상위로 전달
       - 루트까지 반복 or 금액이 1 미만
    
    3. Return 각 판매원의 누적 수익
"""

def solution(enroll, referral, seller, amount):
    
    # 부모 노드 관계를 딕셔너리로 구성
    parent = dict(zip(enroll, referral))
    
    # 각 판매원의 총 수익을 저장할 defaultdict
    total = defaultdict(int)
    
    # 판매 기록을 순회하며 수익 분배
    for seller_name, sales_amount in zip(seller, amount):
        money = sales_amount * 100
        current = seller_name
        
        # 루트("-")에 도달하거나 분배할 금액이 없을 때까지 반복
        while current != "-" and money > 0:
            commission = money // 10  # 상위 노드에 줄 금액
            total[current] += money - commission  # 현재 노드가 가질 금액
            current = parent[current]  # 상위 노드로 이동
            money = commission  # 다음 분배할 금액
    
    # 등록된 판매원 순서대로 수익 반환
    return [total[name] for name in enroll]

# 예시 실행
# enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
# referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
# seller = ["young", "john", "tod", "emily", "mary"]
# amount = [12, 4, 2, 5, 10]
# print(solution(enroll, referral, seller, amount))

