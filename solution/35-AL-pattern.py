"""
[알고리즘 패턴들이 실생활에서 어떻게 쓰이는지 예시]
이메일 주소 중복 가입 방지 : 해시셋으로 O(1) 시간에 중복 검사
교대 근무 스케줄 관리 : 모듈로 연산으로 순환 패턴 조회
두 사람이 양쪽에서 책장 정리하기: 양끝에서 중앙으로 수렴하며 효율적 탐색 - 투 포인터
주식의 이동평균 계산 : 고정 크기 윈도우를 이동하며 연속된 데이터 처리 - 슬라이딩 윈도우

[자주 사용되는 파이썬 문법]
1. 집합 연산
   seen = set()  # 빈 집합 생성
   seen.add(item)  # O(1) 추가
   item in seen  # O(1) 검색

2. 모듈로 연산
   index % total  # 순환 인덱스
   (index + 1) % total  # 다음 순환 위치

3. 데크 활용
   from collections import deque
   window = deque(maxlen=k)  # 고정 크기 윈도우

[핵심 알고리즘 패턴 수도코드]

# 중복 검사
def check_duplicates(items):
    seen = set()
    for item in items:
        if item in seen:
            return True
        seen.add(item)
    return False

# 순환 구조
def get_circular_index(current, total):
    return current % total

# 투 포인터
def two_pointer_search(array):
    left, right = 0, len(array) - 1
    while left < right:
        # 조건에 따라 포인터 이동
        if condition():
            left += 1
        else:
            right -= 1

# 슬라이딩 윈도우
def sliding_window(array, k):
    window = deque(maxlen=k)
    for item in array:
        window.append(item)
        if len(window) == k:
            process_window(window)
"""

# 기존 코드는 유지... 