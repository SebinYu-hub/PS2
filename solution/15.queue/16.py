"""
[Input]
1. progresses: list[int]
   - 각 작업의 진도율
   - 제약: 1 ≤ len(progresses) ≤ 100
   - 제약: 0 ≤ progresses[i] ≤ 99

2. speeds: list[int]
   - 각 작업의 개발 속도
   - 제약: len(speeds) == len(progresses)
   - 제약: 1 ≤ speeds[i] ≤ 100

[Output]
- result: list[int]
  - 각 배포마다 배포되는 기능의 수를 담은 배열
  - 제약: 배포는 하루에 한 번만 가능
  - 제약: 뒤의 기능이 먼저 개발되어도 앞의 기능이 배포될 때 함께 배포
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 작업 완료일 계산 필요 : 올림 연산(math.ceil) 활용
2. 묶음 처리 필요 : deque로 순차 처리
3. 효율적 연산 필요 : list comprehension 활용
4. 순서 의존성 필요 : 앞 작업 기준 배포
5. 그룹화 필요 : 배포 가능한 작업 묶기
"""
"""
[자료구조]
1. days: deque
   - 목적: 각 작업의 완료 소요일 저장
   - 특징: 순차적 처리 가능
   - 연산: popleft(), append()

2. answer: list
   - 목적: 각 배포별 기능 수 저장
   - 특징: 배포 단위로 그룹화
   - 연산: append()

[알고리즘: Feature Development]
procedure solution(progresses, speeds):
    1. Calculate days:
       - 각 작업별 완료 소요일 계산
       - 올림 연산으로 정확한 일수 계산
    
    2. Group deployments:
       - 첫 작업 기준으로 함께 배포 가능한 작업 그룹화
       - 이전 작업보다 일찍 끝나면 함께 배포
    
    3. Return result:
       - 각 배포별 기능 수 반환
"""

import math
from collections import deque

def solution(progresses, speeds):
    # 각 작업의 배포 가능일 계산 (list comprehension과 zip 활용)
    days = deque([math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)])
    answer = []
    
    while days:
        # 현재 그룹의 기준이 되는 배포일
        current = days.popleft()
        count = 1
        
        # 현재 기준 배포일보다 일찍 끝나는 작업들을 한 번에 처리
        while days and days[0] <= current:
            days.popleft()
            count += 1
            
        answer.append(count)
    
    return answer

# 예시 실행
# print(solution([93, 30, 55], [1, 30, 5]))  # [2, 1]
# print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))  # [1, 3, 2]
