"""
[Input]
1. id_list: list[str]
   - 유저 ID 배열
   - 제약: 2 ≤ len(id_list) ≤ 1,000
   - 제약: 1 ≤ len(id_list[i]) ≤ 10

2. report: list[str]
   - 신고 기록 배열
   - 제약: 1 ≤ len(report) ≤ 200,000
   - 제약: "신고자 피신고자" 형식의 문자열

3. k: int
   - 정지 기준이 되는 신고 횟수
   - 제약: 1 ≤ k ≤ 200

[Output]
- result: list[int]
  - 각 유저별 처리 결과 메일 수신 횟수
  - 제약: len(result) == len(id_list)
  - 제약: 동일한 유저의 신고는 1회로 처리
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 중복 제거 필요 : set으로 신고 기록 관리
2. 관계 추적 필요 : defaultdict로 신고자-피신고자 매핑
3. 카운팅 필요 : defaultdict로 신고 횟수 관리
4. 순서 유지 필요 : id_list 순서대로 결과 생성
5. 효율적 검색 필요 : 해시 테이블 O(1) 조회
"""
"""
[자료구조]
1. reporters: defaultdict(set)
   - 목적: 신고자별 신고한 사용자 집합
   - 특징: 중복 신고 자동 제거
   - 연산: add, in

2. reported_count: defaultdict(int)
   - 목적: 사용자별 신고당한 횟수
   - 특징: 신고 횟수 누적
   - 연산: 증감 연산

[알고리즘: Report Result]
procedure solution(id_list, report, k):
    1. Process reports:
       - 신고 기록 파싱
       - 중복 신고 제거하며 카운트
    
    2. Count mails:
       - k번 이상 신고된 유저 확인
       - 신고자별 처리 결과 카운트
    
    3. Generate result:
       - id_list 순서대로 메일 수 반환
"""

from collections import defaultdict

def solution(id_list, report, k):
    # 신고자별 신고한 사용자 집합
    reporters = defaultdict(set)
    # 사용자별 신고당한 횟수
    reported_count = defaultdict(int)
    # 처리 결과 메일 수신 횟수
    mail_count = defaultdict(int)
    
    # 신고 기록 처리 (중복 신고는 set으로 자동 처리)
    for r in report:
        reporter, reported = r.split()
        # 이전에 신고하지 않은 경우에만 처리
        if reported not in reporters[reporter]:
            reporters[reporter].add(reported)
            reported_count[reported] += 1
    
    # 메일 발송 처리
    for reporter in reporters:
        # 해당 신고자가 신고한 사용자들 중
        # k번 이상 신고된 사용자 수만큼 메일 받음
        mail_count[reporter] = sum(
            1 for reported in reporters[reporter]
            if reported_count[reported] >= k
        )
    
    # id_list 순서대로 메일 수신 횟수 반환
    return [mail_count[user_id] for user_id in id_list]

# 예시 실행
# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# k = 2
# print(solution(id_list, report, k))  # [2,1,1,0]
