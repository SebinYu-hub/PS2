"""
[투 포인터가 실생활에서 어떻게 쓰이는지 예시]

1. 물 담기
실생활: 두 벽 사이에 담을 수 있는 물의 양 계산
알고리즘 본질: 양끝에서 더 낮은 벽 쪽을 이동하며 최대값 탐색

2. 회문 검사
실생활: 문장이 앞뒤로 동일한지 확인
알고리즘 본질: 양끝에서 중앙으로 이동하며 문자 비교

3. 두 배열 병합
실생활: 정렬된 두 카드 덱을 하나로 합치기
알고리즘 본질: 두 배열의 포인터를 이동하며 순서대로 병합

[자주 사용되는 파이썬 문법]
1. 포인터 초기화
   left, right = 0, len(array) - 1

2. 포인터 이동
   left += 1  # 왼쪽 포인터 전진
   right -= 1  # 오른쪽 포인터 후진

3. 슬라이싱
   array[left:right+1]  # 포인터 범위 추출

[핵심 알고리즘 패턴 수도코드]

# 기본 투 포인터
def two_pointer_basic(array):
    left, right = 0, len(array) - 1
    while left < right:
        # 처리 로직
        if condition():
            left += 1
        else:
            right -= 1

# 합계 찾기
def find_sum(array, target):
    left, right = 0, len(array) - 1
    while left < right:
        current_sum = array[left] + array[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []

# 윈도우 이동
def sliding_two_pointer(array, window_size):
    left = right = 0
    while right < len(array):
        # 윈도우 확장
        right += 1
        # 윈도우 축소
        if right - left > window_size:
            left += 1
"""

# 기존 코드는 유지... 