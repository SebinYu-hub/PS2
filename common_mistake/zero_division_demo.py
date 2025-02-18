# 실수 예: 0으로 나누기
# result = 10 / 0  # ZeroDivisionError: division by zero

# 파이썬에서 숫자를 0으로 나누려고 하면 ZeroDivisionError가 발생합니다.

# 실수 예: 변수를 사용하여 나누기를 수행하되, 변수 값이 0인 경우
denominator = 0
if denominator is not 0:
    result = 10 / denominator  # 이 줄도 ZeroDivisionError를 발생시킵니다.

# 올바른 사용법: 나눗셈을 수행하기 전에 분모가 0인지 확인
if denominator != 0:
    result = 10 / denominator
    print(result)
else:
    print("Cannot divide by zero!")

# 특히 복잡한 계산이나 사용자 입력을 처리할 때는 이러한 오류가 발생할 수 있으므로 주의가 필요합니다.
# 사용자 입력을 받아서 나눗셈을 수행하는 경우:

# user_input = float(input("Enter a number to divide 10 by: "))
# if user_input != 0:
#     print(10 / user_input)
# else:
#     print("Cannot divide by zero!")




import random

# Clear separation between examples
print("\n=== 가위바위보 게임 ===\n")

try:
    user_input = input("가위~ 바위~ 보! ").strip()  # Added strip() to remove whitespace
    
    # 컴퓨터의 선택을 랜덤하게 생성
    computer_choice = random.choice(["가위", "바위", "보"])

    # 승패 판정
    if user_input not in ["가위", "바위", "보"]:
        print("잘못된 입력입니다. '가위', '바위', '보' 중에서 입력해주세요.")
    else:
        print(f"컴퓨터의 선택: {computer_choice}")
        
        if user_input == computer_choice:
            print("비겼습니다!")
        elif (user_input == "가위" and computer_choice == "보") or \
             (user_input == "바위" and computer_choice == "가위") or \
             (user_input == "보" and computer_choice == "바위"):
            print("이겼습니다!")
        else:
            print("졌습니다!")
except Exception as e:
    print("오류가 발생했습니다:", e)


