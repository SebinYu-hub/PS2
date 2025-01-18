#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 조합(combinations)은 주어진 리스트 내에서 특정 개수 r의 원소를 선택하는 모든 가능한 조합을 생성합니다.
# 예를 들어, [1, 2, 3]에서 2개의 원소를 선택하는 경우: [(1, 2), (1, 3), (2, 3)]
# 시간 복잡도: O(len(lst)Ccomb_cnt) = len(lst)! / (comb_cnt! * (len(lst)-comb_cnt)!) (모든 조합을 생성하므로)
# 이 코드는 재귀적으로 조합을 생성하고 그 결과를 리스트에 저장합니다.

# lst=[1,2,3]인 경우, 아래 주석과 맞춰서 보면 됩니다.
# 현재 원소를 선택하는 경우
        # e.g., lst = [1, 2, 3], comb_cnt = 2
        # |-> 1을 선택: 
        # |       |
        # |       |-> 2를 선택: (1, 2) 완성

# 현재 원소를 선택하지 않는 경우
        # e.g., lst = [1, 2, 3], comb_cnt = 2
        # |       |
        # |       |-> 2를 선택 X:
        # |               |
        # |               |-> 3를 선택: (1, 3) 완성

#초기 호출
        # e.g., lst = [1, 2, 3], comb_cnt = 2
        # |-> 1을 선택 X:
        #         |
        #         |-> 2를 선택: 
        #         |       |
        #         |       |-> 3를 선택: (2, 3) 완성


from itertools import combinations

lst = [1, 2, 3]
comb_cnt = 2
result = list(combinations(lst, comb_cnt))
print(result)  # [(1, 2), (1, 3), (2, 3)]
print(combinations(lst, comb_cnt))