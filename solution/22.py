"""
[Input]
1. record: list[str]
   - 채팅방 기록 배열
   - 제약: 1 ≤ len(record) ≤ 100,000
   - 제약: 각 기록은 "Enter/Leave/Change uid nickname" 형식

[Output]
- result: list[str]
  - 최종 닉네임으로 변환된 메시지 배열
  - 제약: len(result)는 Enter/Leave 개수와 동일
  - 제약: 각 메시지는 정해진 형식을 따름
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 상태 관리 필요 : 딕셔너리로 최신 닉네임 관리
2. 메시지 생성 필요 : 문자열 템플릿 활용
3. 2단계 처리 필요 : 닉네임 갱신 후 메시지 생성
4. 효율적 접근 필요 : 해시 테이블의 O(1) 조회
5. 순서 유지 필요 : 입력 순서대로 메시지 생성
"""
"""
[자료구조]
1. user_names: dict
   - 목적: 유저ID와 최종 닉네임 매핑
   - 특징: O(1) 시간 접근
   - 연산: 갱신/조회

[알고리즘: Chat Room Log]
procedure solution(record):
    1. Update nicknames:
       - 모든 기록을 순회하며 최신 닉네임 갱신
       - Enter/Change 명령어만 처리
    
    2. Generate messages:
       - 다시 기록을 순회하며 메시지 생성
       - Enter/Leave 명령어만 처리
       - 최신 닉네임으로 메시지 생성
    
    3. Return result:
       - 생성된 메시지 배열 반환
"""

def solution(record):
    # 메시지 템플릿 (f-string 사용)
    ENTER_MSG = "{}님이 들어왔습니다."
    LEAVE_MSG = "{}님이 나갔습니다."
    
    # 유저 ID와 닉네임 매핑
    user_names = {}
    messages = []
    
    # 첫 번째 순회: 최종 닉네임 결정
    for cmd in record:
        data = cmd.split()
        action = data[0]
        
        if action != "Leave":  # Enter 또는 Change인 경우
            user_id, nickname = data[1], data[2]
            user_names[user_id] = nickname
    
    # 두 번째 순회: 메시지 생성
    for cmd in record:
        data = cmd.split()
        action, user_id = data[0], data[1]
        
        if action == "Enter":
            messages.append(ENTER_MSG.format(user_names[user_id]))
        elif action == "Leave":
            messages.append(LEAVE_MSG.format(user_names[user_id]))
    
    return messages

# 예시 실행
# record = [
#     "Enter uid1234 Muzi",
#     "Enter uid4567 Prodo",
#     "Leave uid1234",
#     "Enter uid1234 Prodo",
#     "Change uid4567 Ryan"
# ]
# print(solution(record))
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
