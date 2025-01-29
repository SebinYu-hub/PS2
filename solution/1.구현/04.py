"""
[Input]
1. answers: list[int]
   - 정답이 순서대로 들어있는 배열
   - 제약: 1 ≤ answers[i] ≤ 5
   - 제약: 1 ≤ len(answers) ≤ 10,000

[Output]
- result: list[int]
  - 가장 많은 문제를 맞힌 사람의 번호를 담은 배열
  - 제약: 오름차순 정렬
  - 제약: 최고점을 받은 사람이 여럿일 경우 모두 포함
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 주기적 답안 비교 필요 : 모듈로(%) 연산으로 패턴 순환
2. 점수 계산 필요 : list comprehension으로 최적화
3. 최대값 필터링 필요 : max() + list comprehension 활용
4. 여러 패턴 비교 필요 : 패턴을 리스트로 관리
5. 인덱스 순환 필요 : 모듈로 연산으로 패턴 반복
"""
"""
[자료구조]
1. patterns: list[list[int]]
   - 목적: 각 수포자의 찍기 패턴 저장
   - 특징: 2차원 리스트로 패턴 관리

2. scores: list[int]
   - 목적: 각 수포자의 점수 저장
   - 특징: 인덱스로 수포자 식별

[알고리즘: Pattern Matching Score]
procedure solution(answers):
    1. Initialize patterns:
       - 각 수포자의 반복 패턴 정의
       
    2. Calculate scores:
       - 각 수포자별 정답 수 계산
       - 패턴 매칭에 모듈로 연산 활용
       
    3. Find max score:
       - 최고 점수 찾기
       
    4. Filter winners:
       - 최고 점수와 같은 점수를 받은 수포자 번호 추출
       - 오름차순 정렬
"""

def solution(answers):
    patterns = [
        [1, 2, 3, 4, 5],                    # 패턴 1: [1,2,3,4,5,1,2,3,4,5,...]
        [2, 1, 2, 3, 2, 4, 2, 5],          # 패턴 2: [2,1,2,3,2,4,2,5,2,1,...]
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]     # 패턴 3: [3,3,1,1,2,2,4,4,5,5,...]
    ]
    
    # 각 수포자별 점수 계산 - list comprehension 활용
    scores = [sum(1 for i, ans in enumerate(answers) if ans == pattern[i % len(pattern)]) 
             for pattern in patterns]
    # 예: answers = [1,2,3,4,5]일 때
    # scores = [5, 0, 0] (첫 번째 수포자만 모두 맞힘)
    
    # 최고 점수와 동일한 점수를 받은 수포자 번호 반환
    max_score = max(scores)  # 5
    return [i + 1 for i, score in enumerate(scores) if score == max_score]  # [1]

# 예시 실행
# print(solution([1,2,3,4,5]))  # [1]
# print(solution([1,3,2,4,2]))  # [1,2,3]
