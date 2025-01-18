"""
[Input]
1. nums: List[int]
   - 정수 배열
   - 제약: len(nums) >= 0
   - 제약: 각 원소는 정수

[Output]
- result: int
  - 최장 증가 부분 수열의 길이
  - 제약: result >= 0
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 부분 수열 찾기 필요 : 이진 탐색 활용
2. 증가하는 순서 유지 : LIS 알고리즘
3. O(N log N) 요구 : 이진 탐색으로 최적화
4. 메모리 효율성 중요 : 단일 배열로 관리
5. 동적인 수열 갱신 : 탐색 위치에 값 갱신
"""
"""
[자료구조]
- lis: List[int]
  - 목적: 현재까지의 LIS 저장
  - 특징: 정렬된 상태 유지

[알고리즘: Binary Search LIS]
procedure find_lis(nums):
    1. Initialize:
       - LIS 배열 생성
       - 첫 원소 추가
    
    2. For each num in nums:
       if num > lis[-1]:
          - LIS에 추가
       else:
          - 이진탐색으로 삽입위치 찾기
          - 해당 위치 값 갱신
    
    3. Return LIS 길이
"""

def solution(nums):
    # 최적화 1: 이진 탐색을 위한 배열 초기화
    # @reference/binary_search_mistake.py 참조
    if not nums:
        return 0
        
    # 최적화 2: LIS를 저장할 배열
    # @performance/list_vs_set_in.py 참조
    lis = [nums[0]]
    
    # 최적화 3: 이진 탐색으로 삽입 위치 찾기
    def binary_search(target):
        left, right = 0, len(lis)
        while left < right:
            mid = (left + right) // 2
            if lis[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
    
    # 최적화 4: O(N log N) 시간 복잡도로 LIS 구성
    for num in nums[1:]:
        if num > lis[-1]:  # 현재 수가 LIS 마지막 값보다 크면 추가
            lis.append(num)
        else:  # 그렇지 않으면 적절한 위치에 삽입
            pos = binary_search(num)
            lis[pos] = num
    
    return len(lis)  # LIS의 길이 반환

# 예시 실행
# print(solution([1, 4, 2, 3, 1, 5, 7, 3]))  # 5
# print(solution([3, 2, 1]))  # 1
