# 좌표평면 벗어나는지 여부 확인
def is_valid_move(nx, ny):
    return 0 <= nx < 11 and 0 <= ny < 11

# 다음 좌표 결정
def update_location(x, y, dir):
    if dir == 'U':
        nx, ny = x, y + 1
    elif dir == 'D':
        nx, ny = x, y - 1
    elif dir == 'L':
        nx, ny = x - 1, y
    elif dir == 'R':
        nx, ny = x + 1, y
    return nx, ny

def solution(dirs):
    x, y = 5, 5
    ans = set() # 겹치는 좌표 1개로 설정
    for dir in dirs:
        nx, ny = update_location(x, y, dir)
        if not is_valid_move(nx, ny):
            continue
        ans.add((x, y, nx, ny))
        ans.add((nx, ny, x, y)) # 양방향 저장
        x, y = nx, ny
    return len(ans) / 2