import math

def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    
    # 각 작업의 배포 가능일 계산하기
    days_left = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(n)]
    
    count = 0 # 배포될 작업 개수
    max_day = days_left[0] # 배포될 작업 중 가장 늦게 배포될 작업의 가능일
    
    for i in range(n):
        # 배포 가능일이 max_day보다 빠르면
        if days_left[i] <= max_day:
            count += 1
        # 배포 예정일이 기준 배포일보다 느리면
        else:
            answer.append(count)
            count = 1
            max_day = days_left[i]
            
    answer.append(count)
    return answer