def inspection(s):
    stack = []
    
    for mem in s:
        if mem in '({[':
            stack.append(mem)
        elif mem in ')}]':
            if not stack:
                return 0
            top = stack.pop()
            if (mem == ')' and top != '(') or \
               (mem == '}' and top != '{') or \
               (mem == ']' and top != '['):
                return 0
    
    return 0 if stack else 1
    
    
def solution(s):
    answer = 0
    
    # s의 길이만큼 왼쪽으로 회전하며 올바른 문자열인지 검사
    for i in range(len(s)):
        new = s[i:] + s[:i]
        ans = inspection(new)
        if ans == 1:
            answer += 1
        elif ans == 0:
            continue
        
    return answer