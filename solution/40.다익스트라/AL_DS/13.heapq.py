#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################

# [실생활 예시] : [알고리즘 본질]
# 1. 응급실 환자 대기열 : 우선순위 기반 처리 순서
# 2. 프린터 작업 대기열 : 중요도 기반 인쇄 순서
# 3. OS 작업 스케줄러 : 우선순위 기반 프로세스 관리
# 4. 네트워크 패킷 처리 : QoS 기반 패킷 우선순위

"""
-- heap(힙)은 주로 다음과 같은 상황에서 유용하게 사용됩니다:
본질적인 특징: 자동 정렬 특성

_최대/최소값을 빠르게 찾아야 할 때
K번째 큰/작은 수 찾기
중앙값 찾기 (최대힙과 최소힙 동시 사용)

_우선순위 큐가 필요한 작업
작업 스케줄링
프로세스 관리
다익스트라 알고리즘

_실시간으로 데이터가 추가/삭제되며 정렬이 필요할 때
실시간 랭킹 시스템
스트리밍 데이터의 중앙값 계산
"""


# [코딩테스트 꿀팁]
# 1. 최소/최대 힙 전환
#    최대힙: -item으로 부호 변경
#    heapq.heappush(heap, -item)
#    -heapq.heappop(heap)
# 
# 2. 튜플 활용
#    heapq.heappush(heap, (priority, item))
#    우선순위가 같을 때는 두 번째 값으로 정렬
#
# 3. 힙 정렬
#    sorted_list = []
#    while heap:
#        sorted_list.append(heapq.heappop(heap))

import heapq

# 초기 리스트 정의. 현재 힙 속성을 만족하지 않음
# 힙 속성: 부모 노드가 자식 노드보다 항상 작은 이진 트리
lst = [4, 15, 7, 3, 2, 8]
print("초기 리스트: ", lst) #출력값 : [4, 15, 7, 3, 2, 8]
# 현재 트리:
#      4
#    /   \
#   15    7
#  /  \  /
# 3    2 8 

# heapq.heapify(iterable): 리스트를 in-place로 힙 속성을 만족하도록 변환, 반환값은 None
# 시간 복잡도: O(N)
heapq.heapify(lst)
print("heapify(lst) 후 리스트: ", lst) #출력값 : [2, 3, 7, 4, 15, 8]
# 변환된 트리:
#      2
#    /   \
#   3     7
#  /  \  /
# 4   15 8 

# heapq.heappush(heap, elem): 힙에 원소를 추가
# 시간 복잡도: O(log N)
heapq.heappush(lst, 1)
print("heappush(lst, 1) 후 리스트: ", lst)  #출력값 : [1, 3, 2, 4, 15, 8, 7]

# heapq.heappop(heap): 힙에서 가장 작은 원소를 제거하고 그 원소를 반환
# 시간 복잡도: O(log N)
print("heappop(lst) 출력: ", heapq.heappop(lst))  #출력값 : 1
print("heappop(lst) 후 리스트: ", lst)  #출력값 : [2, 3, 7, 4, 15, 8]

# ... (여기에 추가 메서드 및 설명을 넣어주세요)

# heappushpop(heap, ele): 힙 heap에 요소 ele를 푸시하고, 힙에서 가장 작은 요소를 팝하고 반환
# 시간 복잡도: O(log N)
print("heappushpop(lst, 0) 실행 결과:", heapq.heappushpop(lst, 0))  #출력값 :  0
print("heappushpop(lst, 0) 후 리스트:", lst)  #출력값 :  [2, 3, 7, 4, 15, 8]

# heapreplace(heap, ele): 힙에서 가장 작은 요소를 팝하고, 요소 ele를 푸시
# 시간 복잡도: O(log N)
print("heapreplace(lst, 0) 실행 결과:", heapq.heapreplace(lst, 0))  #출력값 :  2
print("heapreplace(lst, 0) 후 리스트:", lst)  #출력값 :  [0, 3, 7, 4, 15, 8]
