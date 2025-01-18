#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 리스트 원소의 합은 주어진 리스트의 모든 원소들의 합을 계산하는 알고리즘이니다.
# Python의 내장 함수 sum을 이용하여 리스트의 모든 원소의 합을 손쉽게 계산할 수 있습니다.

# [실생활 예시] : [알고리즘 본질]
# 1. 장바구니 총액 계산 : 각 상품 가격의 총합
# 2. 학급 평균 점수 계산 : 모든 학생 점수의 합계 구하기
# 3. 월간 지출 합계 : 일별 지출액의 총합

# [코딩테스트 꿀팁]
# 1. sum() vs reduce()
#    - sum(): 숫자 리스트 합계에 최적화
#    - reduce(): 복잡한 연산에 활용
# 2. 조건부 합계는 sum()과 조건식 활용
#    - sum(x for x in arr if x > 0)
# 3. numpy.sum() 활용
#    - 대용량 데이터나 다차원 배열에 효과적

def list_element_sum(arr):
    return sum(arr)

# 예시 사용법
arr = [1, 2, 3, 4, 5]
print(list_element_sum(arr))  # 출력: 15

# 실제 활용 예시 - 조건부 합계
numbers = [-1, 2, -3, 4, -5, 6]
positive_sum = sum(x for x in numbers if x > 0)  # 양수의 합
print(positive_sum)  # 출력: 12

# 다차원 리스트 합계
matrix = [[1, 2], [3, 4], [5, 6]]
total = sum(sum(row) for row in matrix)
print(total)  # 출력: 21
