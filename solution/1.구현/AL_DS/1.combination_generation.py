#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 조합 생성 알고리즘은 주어진 리스트에서 n개의 원소를 선택하는 모든 가능한 조합을 생성하는 알고리즘입니다.
# itertools 모듈의 combinations 함수를 이용하여 리스트에서 n개의 원소를 선택하는 모든 조합을 생성할 수 있습니다.

# [실생활 예시] : [알고리즘 본질]
# 1. 포커 게임에서 5장의 카드 조합 생성 : n개 중 r개를 선택하는 모든 경우의 수
# 2. 학급 내 2인 1조 팀 구성 : 순서 상관없이 n명 중 2명을 뽑는 경우의 수
# 3. 도서관 책장 배치 : n권의 책 중 한 칸에 r권을 놓는 경우의 수

# [코딩테스트 꿀팁]
# 1. combinations vs permutations
#    - combinations: 순서 상관없이 선택 (ABC = CBA)
#    - permutations: 순서가 중요 (ABC ≠ CBA)
# 2. combinations_with_replacement: 중복 허용 조합
# 3. 시간복잡도: O(nCr) = O(n! / (r! * (n-r)!))

from itertools import combinations

def generate_combinations(arr, n):
    return list(combinations(arr, n))

# 예시 사용법
arr = [1, 2, 3]
print(generate_combinations(arr, 2))  # 출력: [(1, 2), (1, 3), (2, 3)]

# 실제 활용 예시
items = ['A', 'B', 'C', 'D']
team_size = 2
teams = generate_combinations(items, team_size)
# 출력: [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]

