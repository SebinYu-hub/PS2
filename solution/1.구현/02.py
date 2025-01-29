"""
[Input]
1. lst: list
   - 중복 제거할 리스트
   - 제약: 임의의 요소 포함 가능
2. list1, list2: list
   - 집합 연산을 수행할 두 리스트
   - 제약: 임의의 요소 포함 가능

[Output]
1. remove_duplicates():
   - result: list
     - 중복이 제거된 정렬된 리스트
     - 제약: 모든 요소가 유일함

2. set_operations():
   - intersection, union, difference: tuple(set, set, set)
     - 교집합, 합집합, 차집합 결과
     - 제약: 각 집합은 중복 없는 요소들의 모음
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 중복 제거 필요 : Set 자료구조 활용
2. 빠른 검색 필요 : 해시 테이블 기반 O(1) 연산
3. 집합 연산 필요 : Set의 &, |, - 연산자 활용
4. 정렬 필요 : sorted() 함수 활용
5. 예외 처리 필요 : try-except 구문 사용
"""
"""
[자료구조]
1. set: Set
   - 목적: 중복 없는 요소 저장
   - 특징: 해시 테이블 기반 O(1) 검색
   
2. sorted_list: List
   - 목적: 정렬된 결과 저장
   - 특징: 순서가 있는 컬렉션

[알고리즘: Set Operations]
procedure remove_duplicates(lst):
    1. Convert to set:
       - 리스트를 set으로 변환하여 중복 제거
    
    2. Sort results:
       - set을 정렬된 리스트로 변환
    
    3. Return sorted unique list

procedure set_operations(list1, list2):
    1. Convert to sets:
       - 두 리스트를 set으로 변환
    
    2. Perform set operations:
       - 교집합(&) 계산
       - 합집합(|) 계산
       - 차집합(-) 계산
    
    3. Return operation results
"""

def remove_duplicates(lst):
      # set으로 변환하여 중복 제거 후 리스트로 변환
      unique_lst = sorted(set(lst), reverse=True)
      return unique_lst


def set_operations(list1, list2):
    try:    
        # set으로 변환하여 연산 수행
        set1 = set(list1)
        set2 = set(list2)
        
        # 집합 연산 수행
        intersection = set1 & set2  # 교집합
        union = set1 | set2        # 합집합
        difference = set1 - set2    # 차집합
        
        return intersection, union, difference
        
    except Exception as e:
        print(f"Error performing set operations: {e}")
        return set(), set(), set()

# 예시 실행
# result1 = remove_duplicates([3, 1, 2, 3, 2, 1])
# print(result1)  # [3, 2, 1]
result2 = set_operations([1, 2, 2, 3], [2, 3, 4])
print(result2)  # ({2, 3}, {1, 2, 3, 4}, {1}) 