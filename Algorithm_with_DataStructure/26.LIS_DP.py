#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################    
# 1. 알고리즘의 개념:
#    LIS(Longest Increasing Subsequence) 알고리즘은 주어진 배열에서 가장 긴 증가하는 부분 수열의 길이를 찾는 알고리즘이다.
#    동적 프로그래밍 방법을 사용하여 이전에 계산한 부분 문제의 결과를 저장하고 재사용함으로써 효율적으로 문제를 해결한다.

# [실생활 예시] : [알고리즘 본질]
# 1. 주식 가격 분석 : 상승 추세 구간 찾기
# 2. 신호 처리 : 증가하는 신호 패턴 탐지
# 3. 생물학적 서열 : 진화 과정의 증가 패턴
# 4. 시계열 데이터 : 증가 트렌드 분석

# [코딩테스트 꿀팁]
# 1. DP 배열 초기화
#    dp = [1] * n  # 모든 원소는 길이 1의 LIS
# 
# 2. 이진 탐색 최적화
#    from bisect import bisect_left
#    temp = [arr[0]]
#    for x in arr[1:]:
#        if x > temp[-1]: temp.append(x)
#        else: temp[bisect_left(temp, x)] = x
#    return len(temp)  # O(nlogn)
#
# 3. 경로 복원
#    path = []
#    max_len = max(dp)
#    for i in range(n-1, -1, -1):
#        if dp[i] == max_len:
#            path.append(arr[i])
#            max_len -= 1
#    return path[::-1]

# 2. 예시 입력 / 출력:
#    입력: [10, 22, 9, 33, 21, 50, 41, 60]
#    출력: 5 (해당 수열에서 LIS의 길이)

# 3. 알고리즘의 시간 복잡도:
#    이 알고리즘의 시간 복잡도는 O(n^2)이다.

# 4. 해당 알고리즘으로 풀 수 있는 문제 예시:
#    - 주어진 배열에서 최장 증가 부분 수열의 길이를 찾는 문제
#    - 시퀀스 정렬 문제에서 최적 부분 구조 찾기 등

# 5. 상세 과정:
#    - DP 배열을 모두 1로 초기화한다 (각 요소 자체가 길이 1의 LIS를 형성).
 #    - 배열의 각 요소에 대해, 그 이전의 모든 요소들과 비교하여 증가하는 부분 수열을 찾고, DP 배열을 업데이트한다.
#    - DP 배열의 최대값을 찾아 그것이 최장 증가 부분 수열의 길이가 된다.

def lis(arr):
    n = len(arr)

    # DP 배열 초기화: 모든 요소가 자기 자신만을 포함하는 길이 1의 LIS를 형성한다.
    dp = [1] * n

    # DP 배열이 의미하는 바: dp[i]는 arr[i]를 마지막으로 하는 LIS의 길이를 나타낸다.
    
    # 배열의 각 요소에 대해
    for i in range(1, n):
        for j in range(i):
            # 증가하는 부분 수열을 찾으면 DP 배열 업데이트
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

    # DP 배열의 최대값을 찾아 반환
    return max(dp)

# 예제:
input_arr = [10, 22, 9, 33, 21, 50, 41, 60]
print(lis(input_arr))  # 출력: 5
