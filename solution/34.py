"""
[Input]
1. nums: List[int]
   - N마리의 폰켓몬 종류 번호
   - 길이는 항상 짝수
   - 1 ≤ 번호 ≤ 200,000

[Output]
- result: int
  - 선택할 수 있는 폰켓몬 종류 수의 최댓값
  - N/2마리만 선택 가능
"""

"""
[문제 특징] : [알고리즘 선택 이유]
1. 중복 제거 필요 : set 자료구조 활용
2. 최대 선택 제한 : min 함수로 제한 조건 처리
3. 종류 수 계산 : set의 길이로 유니크 값 계산
4. 입력 크기 제한 : O(N) 시간복잡도 필요
5. 메모리 효율성 : set으로 중복 제거하여 공간 최적화
"""

"""
[자료구조]
1. unique_nums: Set[int]
   - 중복 제거된 폰켓몬 종류
   - set으로 O(1) 탐색/삽입

[알고리즘: Set-based Selection]
procedure find_max_types(nums):
    1. Initialize:
       - nums를 set으로 변환하여 중복 제거
    
    2. Calculate:
       - 선택 가능한 수 = len(nums) // 2
       - 실제 종류 수 = len(set(nums))
    
    3. Return min(선택 가능한 수, 실제 종류 수)
"""

def solution(nums):
    # 최적화 1: set comprehension으로 한 번에 중복 제거
    # 최적화 2: 중간 변수 할당 없이 직접 계산
    return min(len(nums) // 2, len({x for x in nums}))

# TEST 코드입니다
# print(solution([3,1,2,3]))  # 2
# print(solution([3,3,3,2,2,4]))  # 3
# print(solution([3,3,3,2,2,2]))  # 2