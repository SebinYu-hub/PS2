#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 순열 생성 알고리즘은 주어진 리스트의 모든 가능한 순서의 조합을 생성하는 알고리즘입니다.
# itertools 모듈의 permutations 함수를 이용하여 리스트의 모든 순열을 생성할 수 있습니다.

# [실생활 예시] : [알고리즘 본질]
# 1. 자물쇠 비밀번호 : 가능한 모든 숫자 조합 생성
# 2. 여행 경로 계획 : 방문할 도시들의 모든 가능한 순서
# 3. 주차 공간 배치 : 차량들의 모든 가능한 주차 순서

# [코딩테스트 꿀팁]
# 1. permutations vs combinations
#    - permutations: 순서가 중요 (ABC ≠ CBA)
#    - combinations: 순서 무관 (ABC = CBA)
# 2. product: 중복 순열
#    - product('ABC', repeat=2): AA,AB,AC,BA,BB,BC,CA,CB,CC
# 3. 시간복잡도: O(n!)
#    - n이 커지면 매우 빠르게 증가, n ≤ 10 정도가 적당

from itertools import permutations

def generate_permutations(arr):
    return list(permutations(arr))

# 예시 사용법
arr = [1, 2, 3]
print(generate_permutations(arr))  # 출력: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

# 실제 활용 예시 - 다양한 순열 생성
from itertools import product

# 1. 특정 길이의 순열만 생성
items = ['A', 'B', 'C']
r = 2
partial_perm = list(permutations(items, r))
print(partial_perm)  # 출력: [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# 2. 중복 순열 생성
repeat_perm = list(product(items, repeat=2))
print(repeat_perm)  # 출력: [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
