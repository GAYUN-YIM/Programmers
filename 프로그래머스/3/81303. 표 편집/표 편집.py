def solution(n, k, cmd):
    # 삭제된 행 저장
    deleted = []
    
    # 링크드리스트에서 각 행 위아래의 행의 인텍스 저장
    up = [i - 1 for i in range(n + 2)]
    down = [i + 1 for i in range(n + 1)]
    
    # 현재 위치
    k += 1
    
    # 명령어 처리
    for cmd_i in cmd:
        # 현재 위치 삭제 후 그 다음 위치로
        if cmd_i.startswith("C"):
            deleted.append(k)
            up[down[k]] = up[k]
            down[up[k]] = down[k]
            k = up[k] if n < down[k] else down[k]
        
        # 삭제된 행 복원
        elif cmd_i.startswith('Z'):
            restore = deleted.pop()
            down[up[restore]] = restore
            up[down[restore]] = restore
            
        # U나 D일 경우
        else:
            action, num = cmd_i.split()
            if action == "U":
                for _ in range(int(num)):
                    k = up[k]
            else:
                for _ in range(int(num)):
                    k = down[k]
    
    # 문자열 반환
    answer = ["O"] * n
    for i in deleted:
        answer[i - 1] = "X"
    return "".join(answer)