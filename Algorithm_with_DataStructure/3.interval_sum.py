#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 구간 합 알고리즘은 배열이 주어졌을 때 특정 구간의 원소들의 합을 구하는 알고리즘입니다.
# itertools 모듈의 combinations 함수를 이용하여 리스트에서 n개의 원소를 선택하는 모든 조합을 생성할 수 있습니다.

# [실생활 예시] : [알고리즘 본질]
# 1. 월별 매출 누적액 계산 : 특정 기간의 매출 합계 구하기
# 2. 학생 성적 구간별 평균 : 특정 범위 학생들의 평균 점수
# 3. 센서 데이터 분석 : 특정 시간대의 측정값 합계

# [코딩테스트 꿀팁]
# 1. 누적 합(prefix sum) 배열 활용
#    - 구간 합을 O(1)에 계산 가능
#    - prefix[i] = arr[0] + arr[1] + ... + arr[i]
# 2. 2차원 배열에서도 활용 가능
#    - 2차원 누적 합으로 직사각형 영역의 합 계산
# 3. 슬라이딩 윈도우와 함께 사용하면 효과적

def interval_sum(arr, start, end):
    return sum(arr[start:end+1])

# 예시 사용법
arr = [1, 2, 3, 4, 5]
print(interval_sum(arr, 1, 3))  # 출력: 9

# 실제 활용 예시 - 누적 합을 이용한 최적화
def prefix_sum(arr):
    n = len(arr)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]
    return prefix

# 누적 합을 이용한 구간 합 계산 (O(1))
numbers = [1, 2, 3, 4, 5]
prefix = prefix_sum(numbers)
# 구간 [1,3]의 합 계산
result = prefix[4] - prefix[1]  # end+1 - start
print(result)  # 출력: 9
