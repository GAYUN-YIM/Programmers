def solution(prices):
    n = len(prices)
    answer = [0] * n
    
    # 스택 초기화
    stack = [0]
    
    # 가격 떨어진 경우
    for i in range(1, n):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    
    # 스택에 남아있을 경우 (가격이 떨어지지 않은 경우)
    while stack:
        j = stack.pop()
        answer[j] = n - 1 - j
    
    return answer