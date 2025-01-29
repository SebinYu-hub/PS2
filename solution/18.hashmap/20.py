"""
[Input]
1. participant: list[str]
   - 참가자 이름 배열
   - 제약: 1 ≤ len(participant) ≤ 100,000
   - 제약: 1 ≤ len(participant[i]) ≤ 20

2. completion: list[str]
   - 완주자 이름 배열
   - 제약: len(completion) == len(participant) - 1
   - 제약: completion의 모든 이름은 participant에 있음

[Output]
- result: str
  - 완주하지 못한 선수의 이름
  - 제약: 단 한 명만 완주하지 못함
  - 제약: 결과는 participant에 있는 이름
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 빈도수 계산 필요 : Counter 클래스 활용
2. 차집합 연산 필요 : Counter의 subtract 활용
3. 효율적 연산 필요 : 해시 테이블 기반 처리
4. 메모리 효율성 필요 : Counter 객체 사용
5. 결과 추출 필요 : most_common() 메서드 활용
"""
"""
[자료구조]
1. participant_count: Counter
   - 목적: 참가자별 등장 횟수 저장
   - 특징: 해시 테이블 기반
   - 연산: subtract(), most_common()

[알고리즘: Find Incomplete Player]
procedure solution(participant, completion):
    1. Initialize:
       - participant를 Counter로 변환
    
    2. Process completion:
       - completion으로 Counter 감소
       - subtract() 메서드 활용
    
    3. Find result:
       - 빈도수가 1인 참가자 찾기
       - most_common(1) 활용
"""

from collections import Counter

def solution(participant, completion):
    # Counter로 참가자 이름 빈도수 계산
    # Counter({'leo': 1, 'kiki': 1, 'eden': 1})
    participant_count = Counter(participant)
    
    # 완주자 목록으로 빈도수 감소
    # Counter({'leo': 1, 'eden': 0, 'kiki': 0})
    participant_count.subtract(completion)
    
    # 빈도수가 1인(완주하지 못한) 참가자 찾기
    # most_common(1)은 빈도수가 가장 높은 1개 원소를 반환
    return participant_count.most_common(1)[0][0]

# 예시 실행
# print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))  # "leo"
# print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], 
#               ["josipa", "filipa", "marina", "nikola"]))  # "vinko"
