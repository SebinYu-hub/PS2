#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 계수 정렬(Counting Sort)은 정수 배열을 정렬하는 비교 없는 알고리즘입니다.
# 시간 복잡도: O(n + k) (n은 배열의 크기, k는 최댓값과 최솟값의 차이)
# 계수 정렬은 입력 데이터의 분포가 정해져 있을 때 매우 효율적입니다.

# 계수 정렬의 동작 과정:
# 1. 입력 배열을 순회하며 각 숫자의 개수를 센다.
# 2. 개수를 기반으로 숫자를 정렬된 위치에 배치한다.
# 3. 정렬된 결과를 반환한다.

# 예시:
# 입력 배열: [4, 2, 2, 8, 3, 3, 1]
# 최댓값: 8
# count 배열: [0, 1, 2, 2, 1, 0, 0, 0, 1] (각 숫자의 개수)

# count 배열은 입력 배열의 숫자를 카운트한 결과를 저장합니다.
# 인덱스는 숫자를 나타내며, 값은 해당 숫자가 몇 번 등장했는지를 나타냅니다.

# 각 인덱스별로 숫자와 그 숫자의 개수를 나타내는 도식화:
# 0: 0번 등장
# 1: 1번 등장
# 2: 2번 등장
# 3: 2번 등장
# 4: 1번 등장
# 5: 0번 등장
# 6: 0번 등장
# 7: 0번 등장
# 8: 1번 등장

# 정렬된 결과 배열은 count 배열의 인덱스에 따라 해당 숫자를 순서대로 배치합니다.
# 0, 1, 2, 2, 3, 3, 4, 8 순서대로 나열됩니다.

def counting_sort(arr):
    # 입력 배열에서 최댓값을 찾아서 count 배열의 크기를 설정합니다.
    max_val = max(arr)
    count = [0] * (max_val + 1)
    
    # 입력 배열의 각 원소를 센다.
    for num in arr:
        count[num] += 1
    
    # 정렬된 결과를 담을 배열을 초기화합니다.
    sorted_arr = []
    
    # count 배열을 기반으로 정렬된 배열을 생성합니다.
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    
    return sorted_arr

arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print(sorted_arr)



# 파이썬 내장 라이브러리를 사용한 정렬 방법들:

# 1. sorted() 함수 사용
# sorted()는 새로운 정렬된 리스트를 반환합니다.
sorted_list = sorted(arr)
print("sorted():", sorted_list)  # [1, 2, 2, 3, 3, 4, 8]

# 2. list.sort() 메서드 사용
# sort()는 리스트를 직접 정렬하고 None을 반환합니다.
arr_copy = arr.copy()  # 원본 보존을 위해 복사
arr_copy.sort()
print("list.sort():", arr_copy)  # [1, 2, 2, 3, 3, 4, 8]

# 3. 내림차순 정렬
desc_sorted = sorted(arr, reverse=True)
print("내림차순 정렬:", desc_sorted)  # [8, 4, 3, 3, 2, 2, 1]

# 4. key 함수를 사용한 정렬
# 절대값 기준으로 정렬하는 예시
arr_with_negative = [-4, 2, -2, 8, -3, 3, 1]
abs_sorted = sorted(arr_with_negative, key=abs)
print("절대값 기준 정렬:", abs_sorted)  # [1, 2, -2, -3, 3, -4, 8]

