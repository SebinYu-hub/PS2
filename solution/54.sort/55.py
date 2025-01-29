"""
[Input]
1. arr1: List[int]
   - 첫 번째 정렬된 배열
   - 제약: 1 <= len(arr1) <= 1,000,000
          각 원소는 정수

2. arr2: List[int]
   - 두 번째 정렬된 배열
   - 제약: 1 <= len(arr2) <= 1,000,000
          각 원소는 정수

[Output]
- result: List[int]
  - 두 배열을 병합한 정렬된 배열
  - 제약: len(result) == len(arr1) + len(arr2)
         result는 오름차순 정렬됨
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 이미 정렬된 두 배열 병합 : 병합 정렬의 merge 과정 활용
2. 순서 유지하며 병합 필요 : 투 포인터로 순차 비교
3. 원소 순서 보존 필요 : 안정 정렬 특성 활용
4. 메모리 효율성 중요 : 추가 공간 O(N+M) 사용
5. 한 번의 순회로 해결 : O(N+M) 시간 복잡도 보장
"""
"""
[자료구조]
1. Result Array
   - 목적: 병합된 결과 저장
   - 특징: 순차적 추가, 정렬 상태 유지

[알고리즘: Two Pointers]
procedure merge_arrays(arr1, arr2):
    initialize result array
    i, j = 0, 0
    
    while both arrays have elements:
        compare current elements:
            append smaller element
            advance corresponding pointer
    
    append remaining elements from either array
    
    return result
"""

def solution(arr1, arr2):
    # 최적화 1: 결과 리스트를 미리 할당
    # @reference/list_comprehension.py 참조
    merged = []
    
    # 최적화 2: 투 포인터 초기화
    i = j = 0
    len1, len2 = len(arr1), len(arr2)
    
    # 최적화 3: 두 배열의 원소를 순차적으로 비교하며 병합
    while i < len1 and j < len2:
        # 최적화 4: 더 작은 값을 선택하여 추가
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    
    # 최적화 5: 남은 원소들을 extend로 한 번에 추가
    # @performance/append_vs_plus_performance.py 참조
    if i < len1:
        merged.extend(arr1[i:])
    if j < len2:
        merged.extend(arr2[j:])
    
    return merged

# 예시 실행
# print(solution([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]
# print(solution([1, 2, 3], [4, 5, 6]))  # [1, 2, 3, 4, 5, 6]
