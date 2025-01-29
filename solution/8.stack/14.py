from collections import deque

def solution(n, k, cmd):
    """
    [Input]
    1. n: int
       - 표의 행 개수
       - 제약: 5 ≤ n ≤ 1,000,000

    2. k: int
       - 현재 선택된 행의 위치
       - 제약: 0 ≤ k < n

    3. cmd: list[str]
       - 명령어들의 배열
       - 제약: 1 ≤ len(cmd) ≤ 200,000
       - 제약: cmd는 "U X", "D X", "C", "Z" 형식

    [Output]
    - result: str
      - 표의 최종 상태를 나타내는 문자열
      - 제약: 길이가 n인 문자열
      - 제약: 삭제된 행은 'X', 남아있는 행은 'O'
    """
    """
    [문제 특징] : [알고리즘 선택 이유]
    1. 행 삭제/복구 필요 : 링크드 리스트 구조 활용
    2. 이력 관리 필요 : 스택으로 삭제 기록 저장
    3. 효율적 이동 필요 : 배열로 링크드 리스트 구현
    4. 상태 추적 필요 : up/down 배열로 연결 관리
    5. 메모리 효율성 필요 : 배열 기반 구현
    """
    """
    [자료구조]
    1. deleted: deque
       - 목적: 삭제된 행 인덱스 저장
       - 특징: LIFO로 최근 삭제 복구
       - 연산: append(), pop()

    2. up/down: list
       - 목적: 각 행의 이전/다음 행 저장
       - 특징: 링크드 리스트 구현
       - 크기: n+2 (경계 처리용)

    [알고리즘: Table Editor]
    procedure solution(n, k, cmd):
        1. Initialize:
           - up/down 배열 생성
           - 삭제 스택 생성
           - 현재 위치 설정
        
        2. Process commands:
           - 각 명령어 처리:
             a) U X: X칸 위로 이동
             b) D X: X칸 아래로 이동
             c) C: 현재 행 삭제
             d) Z: 최근 삭제 행 복구
        
        3. Build result:
           - 삭제된 행은 'X'로 표시
           - 남은 행은 'O'로 표시
    """
    
    # 삭제된 행의 인덱스를 저장하는 스택
    deleted = deque()
    
    # 링크드 리스트 구현을 위한 up/down 배열
    # 각 인덱스의 이전/다음 인덱스를 저장
    up = [i - 1 for i in range(n + 2)]
    down = [i + 1 for i in range(n + 1)]
    
    # 현재 위치 (1-based 인덱싱)
    k += 1
    
    # 명령어 처리
    for c in cmd:
        if c.startswith("C"):  # 현재 행 삭제
            deleted.append(k)
            up[down[k]] = up[k]
            down[up[k]] = down[k]
            k = up[k] if n < down[k] else down[k]
            
        elif c.startswith("Z"):  # 가장 최근 삭제된 행 복구
            restore = deleted.pop()
            down[up[restore]] = restore
            up[down[restore]] = restore
            
        else:  # 커서 이동
            direction, count = c.split()
            count = int(count)
            if direction == "U":
                for _ in range(count):
                    k = up[k]
            else:  # direction == "D"
                for _ in range(count):
                    k = down[k]
    
    # 결과 문자열 생성
    result = ["O"] * n
    while deleted:  # 삭제된 행 표시
        result[deleted.pop() - 1] = "X"
    return "".join(result)

# 예시 실행
# print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))  # "OOOOXOOO"
