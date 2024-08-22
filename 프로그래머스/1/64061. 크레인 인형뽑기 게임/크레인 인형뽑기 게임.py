def solution(board, moves):
    # 각 열에 대한 스택 생성
    stack = [[] for _ in range(len(board[0]))]
    
    # 역순으로 board 탐색 후 인형 추가
    for i in range(len(board) - 1, -1, -1):
        for j in range(len(board[0])):
            if board[i][j]:
                stack[j].append(board[i][j])
    
    bucket = [] # 바구니 스택
    answer = 0  # 사라진 인형 개수
    
    # moves 순회하며 인형 바구니에 추가
    for m in moves:
        # 해당 열에 인형 있을 경우
        if stack[m - 1]:
            doll = stack[m - 1].pop()
            # 바구니에 인형 있고 같은 인형일 경우
            if bucket and bucket[-1] == doll:
                bucket.pop()
                answer += 2
            # 바구니에 인형 없거나 다른 인형일 경우
            else:
                bucket.append(doll)
                
    return answer

'''
# 초기코드

def solution(board, moves):
    result = 0
    stack = []
    
    # 각 위치에 쌓인 인형의 개수 저장
    ran = len(board)
    num = [0] * ran
    for i in range(ran):
        for j in range(ran):
            if board[j][i] != 0:
                num[i] += 1
                
    # moves에 따른 인형 스택으로 이동 과정
    for m in moves:
        # 위치에 인형이 없으면 아무것도 하지 않고 건너뜀
        if num[m-1] == 0:
            continue
        # 처음, 스택이 비어있을 경우 추가
        elif not stack:
            stack.append(board[ran-num[m-1]][m-1])
            num[m-1] -= 1
        # 스택이 비어있지 않고 인형이 일치하지 않을 경우 스택에 추가
        elif stack and (stack[-1] != board[ran-num[m-1]][m-1]):
            stack.append(board[ran-num[m-1]][m-1])
            num[m-1] -= 1
        # 현재 집어 올린 인형과 스택 가장 위의 인형이 일치할 경우 삭제
        elif stack and (stack[-1] == board[ran-num[m-1]][m-1]):
            result += 2
            stack.pop()
            num[m-1] -= 1
        
    return result
'''